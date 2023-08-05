# Lasik service that exposes an interface to all beams of all connected lasik boards

# Installation
tested on Ubuntu 18.04 only

## From source for development
Clone the repo and in this folder run
```
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip3 install -e .
```
The `-e` switch installs with symlinks to this folder which is great during development.

## From PyPI
```
pip3 install lasikservice
```

# Usage
* to start the server: `lasikservice <host port>`
* to talk to a single board: `lasikconnect <serialdevice>` eg `lasikconnect /dev/ttyACM0`
* note: pip might install these commands in `~/.local/bin` which might not be in your path.
