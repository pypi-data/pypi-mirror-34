from setuptools import setup, find_packages

with open("README", "r") as fh:
    long_description = fh.read()

setup(name='hifiberrydsp',
      version='0.9',
      description='A DSP Toolkit',
      long_description=long_description,
      url='http://github.com/hifiberry/hifiberry-dsp',
      author='Daniel Matuschek',
      author_email='daniel@mhifiberry.com',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: System :: Hardware :: Hardware Drivers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5'
      ],
      packages=find_packages(),
      install_requires=['xmltodict', 'lxml',
                        'spidev', 'pyalsaaudio', 'zeroconf'],
      scripts=['bin/dsptoolkit', 'bin/sigmatcpserver'],
      keywords='audio raspberrypi dsp',
      zip_safe=False)
