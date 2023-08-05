# Caissa

[![Build Status](https://travis-ci.org/ddobbelaere/caissa.svg?branch=master)](https://travis-ci.org/ddobbelaere/caissa)
[![Coverage Status](https://coveralls.io/repos/github/ddobbelaere/caissa/badge.svg?branch=master)](https://coveralls.io/github/ddobbelaere/caissa?branch=master)
[![PyPI version](https://badge.fury.io/py/caissa.svg)](https://badge.fury.io/py/caissa)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1959/badge)](https://bestpractices.coreinfrastructure.org/projects/1959)

Caissa is an intelligent voice-controlled personal assistant (still under development).

Currently she is able to play your favorite internet radio. Some of her upcoming skills include

  - play chess
  - monitor live chess games
  - help you study foreign languages

![Component Overview](https://github.com/ddobbelaere/caissa/raw/master/doc/caissa.png)

## Building and running Caissa

### Debian/Raspbian/Ubuntu

Install dependencies:

```sh
sudo apt-get update
sudo apt-get install -y espeak mbrola-en1 mbrola-nl2 mpg123 libasound2-dev libpulse-dev python3-setuptools swig
```

Optionally, if you want to talk to Caissa via remote control, install LIRC (by following [this guide](https://github.com/josemotta/IoT.Starter.Api/tree/master/gpio-base#lirc-linux-infrared-remote-control-for-raspberry-pi) for Raspbian Stretch) and the following dependencies:

```sh
sudo apt-get install -y cython gcc liblircclient-dev python3-dev
sudo pip3 install pyalsaaudio python-lirc
```

Install the latest stable release:

```sh
sudo pip3 install caissa
```

You can now type `caissa --help` and start. On Raspberry Pi `sudo caissa` is necessary to access various devices.