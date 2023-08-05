#!/usr/bin/env python3

'''
Copyright (c) 2018 Modul 9/HiFiBerry

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import logging
import argparse
import os
import time
import sys
import urllib.request
import socket

from zeroconf import ServiceInfo, Zeroconf, ServiceBrowser

from hifiberrydsp.hardware.adau145x import Adau145x
from hifiberrydsp.server.sigmatcp import SigmaTCP
from hifiberrydsp.filtering.biquad import Biquad
from hifiberrydsp.filtering.volume import *
from hifiberrydsp.datatools import parse_int
from hifiberrydsp.xmlprofile import  \
    ATTRIBUTE_VOL_CTL, ATTRIBUTE_VOL_LIMIT, \
    ATTRIBUTE_BALANCE, ATTRIBUTE_SAMPLERATE, \
    ATTRIBUTE_IIR_FILTER_LEFT, ATTRIBUTE_IIR_FILTER_RIGHT, \
    ATTRIBUTE_FIR_FILTER_LEFT, ATTRIBUTE_FIR_FILTER_RIGHT, \
    ATTRIBUTE_MUTE_REG

from hifiberrydsp.server.sigmatcp import COMMAND_PROGMEM, \
    COMMAND_PROGMEM_RESPONSE, COMMAND_XML, COMMAND_XML_RESPONSE, \
    COMMAND_STORE_DATA, COMMAND_RESTORE_DATA, \
    ZEROCONF_TYPE

from hifiberrydsp import datatools


MODE_BOTH = 0
MODE_LEFT = 1
MODE_RIGHT = 2

DISPLAY_FLOAT = 0
DISPLAY_INT = 1
DISPLAY_HEX = 2
DISPLAY_BIN = 2

GLOBAL_REGISTER_FILE = "/etc/dspparameter.dat"
GLOBAL_PROGRAM_FILE = "/etc/dspprogram.xml"


class REW():

    def __init__(self):
        pass

    @staticmethod
    def readfilters(filename, fs=48000):
        filters = []

        with open(filename) as file:
            for line in file.readlines():
                if line.startswith("Filter"):
                    parts = line.split()
                    if len(parts) >= 12 and parts[2] == "ON" and \
                            parts[4] == "Fc" and parts[6] == "Hz" and \
                            parts[7] == "Gain" and parts[9] == "dB" and \
                            parts[10] == "Q":

                        fc = float(parts[5])
                        gain = float(parts[8])
                        q = float(parts[11])
                        logging.info("Filter fc=%s, q=%s, gaion=%s, fs=%s",
                                     fc, q, gain, fs)
                        filters.append(
                            Biquad.peaking_eq(fc, q, gain, fs))

            return filters


class DSPError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class DSPToolkit():

    def __init__(self,
                 ip="127.0.0.1",
                 dsp=Adau145x()):
        self.dsp = dsp
        self.ip = ip
        self.sigmatcp = SigmaTCP(self.dsp, self.ip)
        self.resetgpio = None

    def set_ip(self, ip):
        self.ip = ip
        self.sigmatcp = SigmaTCP(self.dsp, self.ip)

    def set_volume(self, volume):
        volctl = datatools.parse_int(
            self.sigmatcp.request_metadata(ATTRIBUTE_VOL_CTL))

        if volctl is not None:
            self.sigmatcp.write_decimal(volctl, volume)
            return True
        else:
            logging.info("%s is undefined", ATTRIBUTE_VOL_CTL)
            return False

    def set_limit(self, volume):
        volctl = datatools.parse_int(
            self.sigmatcp.request_metadata(ATTRIBUTE_VOL_LIMIT))

        if volctl is not None:
            self.sigmatcp.write_decimal(volctl, volume)
            return True
        else:
            logging.info("%s is undefined", ATTRIBUTE_VOL_LIMIT)
            return False

    def get_volume(self):
        volctl = datatools.parse_int(
            self.sigmatcp.request_metadata(ATTRIBUTE_VOL_CTL))

        if volctl:
            return self.sigmatcp.read_decimal(volctl)
        else:
            logging.info("%s is undefined", ATTRIBUTE_VOL_CTL)

    def get_limit(self):
        volctl = datatools.parse_int(
            self.sigmatcp.request_metadata(ATTRIBUTE_VOL_LIMIT))

        if volctl:
            return self.sigmatcp.read_decimal(volctl)
        else:
            logging.info("%s is undefined", ATTRIBUTE_VOL_LIMIT)

    def set_balance(self, value):
        '''
        Sets the balance of left/right channels.
        Value ranges from 0 (only left channel) to 2 (only right channel)
        at balance=1 the volume setting on both channels is equal
        '''
        if (value < 0) or (value > 2):
            raise RuntimeError("Balance value must be between 0 and 2")

        balctl = datatools.parse_int(
            self.sigmatcp.request_metadata(ATTRIBUTE_BALANCE))

        if balctl is not None:
            self.sigmatcp.write_decimal(balctl, value)

    def write_biquad(self, addr, bq_params):
        self.sigmatcp.write_biquad(addr, bq_params)

    def write_fir(self, coefficients, mode=MODE_BOTH):

        (firleft, len_left) = datatools.parse_int_length(
            self.sigmatcp.request_metadata(ATTRIBUTE_FIR_FILTER_LEFT))
        (firright, len_right) = datatools.parse_int_length(
            self.sigmatcp.request_metadata(ATTRIBUTE_FIR_FILTER_RIGHT))

        if mode == MODE_BOTH or mode == MODE_LEFT:
            result = self.write_coefficients(firleft,
                                             len_left,
                                             coefficients)

        if mode == MODE_BOTH or mode == MODE_RIGHT:
            result = self.write_coefficients(firright,
                                             len_right,
                                             coefficients)

        return result

    def write_coefficients(self, addr, length, coefficients):
        if len(coefficients) > length:
            logging.error("can't deploy coefficients %s > %s",
                          len(coefficients), length)
            return False

        data = []
        for coeff in coefficients:
            x = list(self.sigmatcp.get_decimal_repr(coeff))
            data[0:0] = x

        x = list(self.sigmatcp.get_decimal_repr(0))
        for i in range(len(coefficients), length):
            data[0:0] = x

        self.sigmatcp.write_memory(addr, data)

        return True

    def get_checksum(self):
        return self.sigmatcp.program_checksum()

    def generic_request(self, request_code, response_code=None):
        return self.sigmatcp.request_generic(request_code, response_code)

    def set_filters(self, filters, mode=MODE_BOTH):

        filters_left = datatools.parse_int_list(
            self.sigmatcp.request_metadata(ATTRIBUTE_IIR_FILTER_LEFT))
        filters_right = datatools.parse_int_list(
            self.sigmatcp.request_metadata(ATTRIBUTE_IIR_FILTER_RIGHT))

        l1 = len(filters_left)
        l2 = len(filters_right)

        if mode == MODE_LEFT:
            maxlen = l1
        elif mode == MODE_RIGHT:
            maxlen = l2
        else:
            maxlen = min(l1, l2)

        if len(filters) > maxlen:
            raise(DSPError("{} filters given, but filter bank has only {} slots".format(
                len(filters), maxlen)))

        self.hibernate(True)

        logging.debug("deploying filters %s", filters)

        i = 0
        for f in filters:
            logging.debug(f)
            if mode == MODE_LEFT or mode == MODE_BOTH:
                self.sigmatcp.write_biquad(filters_left[i], f)
            if mode == MODE_RIGHT or mode == MODE_BOTH:
                self.sigmatcp.write_biquad(filters_right[i], f)
            i += 1

        self.hibernate(False)

    def clear_iir_filters(self, mode=MODE_BOTH):

        filters_left = datatools.parse_int_list(
            self.sigmatcp.request_metadata(ATTRIBUTE_IIR_FILTER_LEFT))
        filters_right = datatools.parse_int_list(
            self.sigmatcp.request_metadata(ATTRIBUTE_IIR_FILTER_RIGHT))

        self.hibernate(True)

        if mode == MODE_BOTH:
            regs = filters_left + filters_right
        elif mode == MODE_LEFT:
            regs = filters_left
        elif mode == MODE_RIGHT:
            regs = filters_right

        if regs is None:
            return

        nullfilter = Biquad.plain()
        for reg in regs:
            self.sigmatcp.write_biquad(reg, nullfilter)

        self.hibernate(False)

    def install_profile(self, xmlfile):
        return self.sigmatcp.write_eeprom_from_file(xmlfile)

    def install_profile_from_content(self, content):
        return self.sigmatcp.write_eeprom_from_xml(content)

    def mute(self, mute=True):
        mutereg = datatools.parse_int(
            self.sigmatcp.request_metadata(ATTRIBUTE_MUTE_REG))

        if mutereg is not None:
            if mute:
                self.sigmatcp.write_memory(
                    mutereg, self.sigmatcp.int_data(1))
            else:
                self.sigmatcp.write_memory(
                    mutereg, self.sigmatcp.int_data(0))
            return True
        else:
            return False

    def reset(self):
        self.sigmatcp.reset()

    def hibernate(self, hibernate=True):
        self.sigmatcp.hibernate(hibernate)
        time.sleep(0.001)

    def get_meta(self, attribute):
        return self.sigmatcp.request_metadata(attribute)

    def get_samplerate(self):
        sr = datatools.parse_int(
            self.sigmatcp.request_metadata(ATTRIBUTE_SAMPLERATE))

        if sr is None or sr == 0:
            return 48000
        else:
            return sr


class CommandLine():

    def __init__(self):
        self.command_map = {
            "store":  self.cmd_store,
            "restore": self.cmd_restore,
            "install-profile": self.cmd_install_profile,
            "set-volume": self.cmd_set_volume,
            "get-volume": self.cmd_get_volume,
            "set-limit": self.cmd_set_limit,
            "get-limit": self.cmd_get_limit,
            "set-rew-filters": self.cmd_set_rew_filters,
            "set-rew-filters-left": self.cmd_set_rew_filters_left,
            "set-rew-filters-right": self.cmd_set_rew_filters_right,
            "set-fir-filters": self.cmd_set_fir_filters,
            "set-fir-filter-right": self.cmd_set_fir_filter_right,
            "set-fir-filter-left": self.cmd_set_fir_filter_left,
            "clear-iir-filters": self.cmd_clear_iir_filters,
            "reset": self.cmd_reset,
            "read-dec": self.cmd_read,
            "loop-read-dec": self.cmd_loop_read_dec,
            "read-int": self.cmd_read_int,
            "loop-read-int": self.cmd_loop_read_int,
            "read-hex": self.cmd_read_hex,
            "loop-read-hex": self.cmd_loop_read_hex,
            "read-reg": self.cmd_read_reg,
            "loop-read-reg": self.cmd_loop_read_reg,
            "get-checksum": self.cmd_checksum,
            "write-reg": self.cmd_write_reg,
            "write-mem": self.cmd_write_mem,
            "get-xml": self.cmd_get_xml,
            "get-prog": self.cmd_get_prog,
            "get-meta": self.cmd_get_meta,
            "mute": self.cmd_mute,
            "unmute": self.cmd_unmute,
            "get-samplerate": self.cmd_samplerate,
            "check-eeprom": self.cmd_check_eeprom,
            "servers": self.cmd_servers,
        }
        self.dsptk = DSPToolkit()

    def register_file(self):
        return os.path.expanduser("~/.dsptoolkit/registers.dat")

    def string_to_volume(self, strval):
        strval = strval.lower()
        vol = 0
        if strval.endswith("db"):
            try:
                dbval = float(strval[0:-2])
                vol = decibel2amplification(dbval)
            except:
                logging.error("Can't parse db value {}", strval)
                return None
            # TODO
        elif strval.endswith("%"):
            try:
                pval = float(strval[0:-1])
                vol = percent2amplification(pval)
            except:
                logging.error("Can't parse db value {}", strval)
                return None
        else:
            vol = float(strval)

        return vol

    def cmd_set_volume(self):
        if len(self.args.parameters) > 0:
            vol = self.string_to_volume(self.args.parameters[0])
        else:
            print("Volume parameter missing")
            sys.exit(1)

        if vol is not None:
            if self.dsptk.set_volume(vol):
                print("Volume set to {}dB".format(
                    amplification2decibel(vol)))
            else:
                print("Profile doesn't support volume control")

    def cmd_set_limit(self):
        if len(self.args.parameters) > 0:
            vol = self.string_to_volume(self.args.parameters[0])
        else:
            print("Volume parameter missing")
            sys.exit(1)

        if vol is not None:
            if self.dsptk.set_limit(vol):
                print("Limit set to {}dB".format(
                    amplification2decibel(vol)))
            else:
                print("Profile doesn't support volume control")

    def cmd_get_volume(self):
        vol = self.dsptk.get_volume()
        if vol is not None:
            print("Volume: {:.4f} / {:.0f}% / {:.0f}db".format(
                vol,
                amplification2percent(vol),
                amplification2decibel(vol)))
        else:
            print("Profile doesn't support volume control")

    def cmd_get_limit(self):
        vol = self.dsptk.get_limit()
        if vol is not None:
            print("Limit: {:.4f} / {:.0f}% / {:.0f}db".format(
                vol,
                amplification2percent(vol),
                amplification2decibel(vol)))
        else:
            print("Profile doesn't support volume limit")

    def cmd_read(self, display=DISPLAY_FLOAT, loop=False, length=None):
        try:
            addr = parse_int(self.args.parameters[0])
        except:
            print("Can't parse address {}".format(self.args.parameters))
            sys.exit(1)

        while True:
            if display == DISPLAY_FLOAT:
                val = self.dsptk.sigmatcp.read_decimal(addr)
                print("{:.8f}".format(val))
            elif display == DISPLAY_INT:
                val = 0
                for i in self.dsptk.sigmatcp.read_data(addr, length):
                    val *= 256
                    val += i
                print(val)
            elif display == DISPLAY_HEX:
                val = self.dsptk.sigmatcp.read_data(addr, length)
                print(''.join(["%02X " % x for x in val]))

            if not loop:
                break

            try:
                time.sleep(float(self.args.delay) / 1000)
            except KeyboardInterrupt:
                break

    def cmd_loop_read_dec(self):
        self.cmd_read(DISPLAY_FLOAT, True)

    def cmd_read_int(self):
        self.cmd_read(DISPLAY_INT, False)

    def cmd_loop_read_int(self):
        self.cmd_read(DISPLAY_INT, True)

    def cmd_read_hex(self):
        self.cmd_read(DISPLAY_HEX, False)

    def cmd_loop_read_hex(self):
        self.cmd_read(DISPLAY_HEX, True)

    def cmd_read_reg(self):
        self.cmd_read(DISPLAY_HEX,
                      False,
                      self.dsptk.dsp.REGISTER_WORD_LENGTH)

    def cmd_loop_read_reg(self):
        self.cmd_read(DISPLAY_HEX,
                      True,
                      self.dsptk.dsp.REGISTER_WORD_LENGTH)

    def cmd_reset(self):
        self.dsptk.reset()
        print("Resetting DSP")

    def cmd_clear_iir_filters(self):
        self.dsptk.clear_iir_filters(MODE_BOTH)
        print("Filters removed")

    def cmd_set_rew_filters(self, mode=MODE_BOTH):
        if len(self.args.parameters) == 0:
            print("Missing filename argument")
            sys.exit(1)

        filters = REW.readfilters(self.args.parameters[0],
                                  self.dsptk.get_samplerate())

        self.dsptk.clear_iir_filters(mode)
        try:
            self.dsptk.set_filters(filters, mode)
            print("Filters configured on both channels:")
            for f in filters:
                print(f.description)
        except DSPError as e:
            print(e)

    def cmd_set_rew_filters_left(self):
        self.set_rew_filters(mode=MODE_LEFT)

    def cmd_set_rew_filters_right(self):
        self.set_rew_filters(mode=MODE_RIGHT)

    def cmd_set_fir_filters(self, mode=MODE_BOTH):
        if len(self.args.parameters) > 0:
            filename = self.args.parameters[0]
        else:
            print("FIR filename missing")
            sys.exit(1)

        coefficients = []
        try:
            with open(filename) as firfile:
                for line in firfile:
                    coeff = float(line)
                    coefficients.append(coeff)
                    print(coeff)
        except Exception as e:
            print("can't read filter file (%s)", e)

        self.dsptk.hibernate(True)
        if self.dsptk.write_fir(coefficients, mode):
            print("deployed filters")
        else:
            print("can't deploy FIR filters "
                  "(not FIR filter in profile or filters in file too long)")
        self.dsptk.hibernate(False)

    def cmd_set_fir_filter_left(self):
        self.cmd_set_fir_filters(MODE_LEFT)

    def cmd_set_fir_filter_right(self):
        self.cmd_set_fir_filters(MODE_RIGHT)

    def cmd_checksum(self):
        checksum = self.dsptk.sigmatcp.program_checksum()

        print(''.join(["%02X" % x for x in checksum]))

    def cmd_get_xml(self):
        xml = self.dsptk.generic_request(COMMAND_XML,
                                         COMMAND_XML_RESPONSE)
        print(xml.decode("utf-8", errors="replace"))

    def cmd_get_prog(self):
        mem = self.dsptk.generic_request(COMMAND_PROGMEM,
                                         COMMAND_PROGMEM_RESPONSE)
        print(mem.decode("utf-8", errors="replace"))

    def cmd_get_meta(self):
        if len(self.args.parameters) > 0:
            attribute = self.args.parameters[0]
        value = self.dsptk.sigmatcp.request_metadata(attribute)
        print(value)

    def cmd_mute(self):
        if self.dsptk.mute(True):
            print("Muted")
        else:
            print("Mute not supported")

    def cmd_unmute(self):
        if self.dsptk.mute(False):
            print("Unmuted")
        else:
            print("Mute not supported")

    def cmd_store(self):
        self.dsptk.generic_request(COMMAND_STORE_DATA)

    def cmd_restore(self):
        self.dsptk.generic_request(COMMAND_RESTORE_DATA)

    def cmd_samplerate(self):
        print("{}Hz".format(self.dsptk.get_samplerate()))

    def cmd_install_profile(self):
        if len(self.args.parameters) > 0:
            filename = self.args.parameters[0]
        else:
            print("profile filename missing")
            sys.exit(1)

        xmlfile = None
        if (filename.startswith("http://") or
                filename.startswith("https://")):
            # Download and store a local copy
            try:
                xmlfile = urllib.request.urlopen(filename)
            except IOError:
                print("can't download {}".format(filename))
                sys.exit(1)
        else:
            try:
                xmlfile = open(filename)
            except IOError:
                print("can't open {}".format(filename))
                sys.exit(1)

        try:
            data = xmlfile.read()
        except IOError:
            print("can't read {}".format(filename))
            sys.exit(1)

        res = self.dsptk.install_profile_from_content(data)

        if res:
            print("DSP profile {} installed".format(filename))
        else:
            print("Failed to install DSP profile {}".format(filename))

    def cmd_write_reg(self):
        if len(self.args.parameters) > 1:
            reg = parse_int(self.args.parameters[0])
            value = parse_int(self.args.parameters[1])
        else:
            print("parameter missing, need addr value")

        data = [(value >> 8) & 0xff, value & 0xff]
        self.dsptk.sigmatcp.write_memory(reg, data)
        sys.exit(1)

    def cmd_write_mem(self):
        if len(self.args.parameters) > 1:
            reg = parse_int(self.args.parameters[0])
            value = parse_int(self.args.parameters[1])
        else:
            print("parameter missing, need addr value")

        data = [(value >> 24) & 0xff,
                (value >> 16) & 0xff,
                (value >> 8) & 0xff,
                value & 0xff]
        self.dsptk.sigmatcp.write_memory(reg, data)
        sys.exit(1)

    def cmd_check_eeprom(self):
        checksum1 = self.dsptk.sigmatcp.program_checksum()
        self.dsptk.reset()
        time.sleep(2)
        checksum2 = self.dsptk.sigmatcp.program_checksum()
        cs1 = ''.join(["%02X" % x for x in checksum1])
        cs2 = ''.join(["%02X" % x for x in checksum2])

        if checksum1 == checksum2:
            print("EEPROM content matches running profile, checksum {}".format(cs1))
        else:
            print("Checksums do not match {} != {}".format(cs1, cs2))

    def cmd_servers(self):
        zeroconf = Zeroconf()
        listener = ZeroConfListener()
        ServiceBrowser(zeroconf, ZEROCONF_TYPE, listener)
        print("Looking for devices")
        time.sleep(5)
        zeroconf.close()
        for name, info in listener.devices.items():
            print("{}: {}".format(name, info))

    def main(self):

        parser = argparse.ArgumentParser(description='HiFiBerry DSP toolkit')
        parser.add_argument('--delay',
                            help='delay for loop operations in ms',
                            nargs='?',
                            type=int,
                            default=1000)
        parser.add_argument('--host',
                            help='hostname or IP address of the server to connect to',
                            nargs='?',
                            default="127.0.0.1")
        parser.add_argument('command',
                            choices=sorted(self.command_map.keys()))
        parser.add_argument('parameters', nargs='*')

        self.args = parser.parse_args()

        self.dsptk.set_ip(self.args.host)

        # Run the command
        self.command_map[self.args.command]()


if __name__ == "__main__":
    cmdline = CommandLine()
    cmdline.main()


class ZeroConfListener:

    def __init__(self):
        self.devices = {}

    def remove_service(self, _zeroconf, _type, _name):
        pass

    def add_service(self, zeroconf, service_type, name):
        if service_type == ZEROCONF_TYPE:
            info = zeroconf.get_service_info(service_type, name)
            ip = socket.inet_ntoa(info.address)
            hostinfo = "{}:{}".format(ip, info.port)
            self.devices[name] = hostinfo
