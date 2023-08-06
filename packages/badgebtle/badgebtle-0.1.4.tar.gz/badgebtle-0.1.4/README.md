# DEF CON badge bluetooth libary

[![PyPI version shields.io](https://img.shields.io/pypi/v/badgebtle.svg)](https://pypi.python.org/pypi/badgebtle/) [![PyPI license](https://img.shields.io/pypi/l/badgebtle.svg)](https://pypi.python.org/pypi/badgebtle/) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/badgebtle.svg)](https://pypi.python.org/pypi/badgebtle/)



A library based on bluepy that performs bluetooth scan for DEF CON badges.

## Usage

#### Basic
```
from badgebtle import BadgeBTLE
b = BadgeBTLE()
neighbors = b.scan()
print(neighbors)
```

## Development

#### Setup
```
$ git clone https://github.com/dczia/python-badgebtle.git
$ virtualenv-3 v
$ source ./v/bin/activate
$ pip install -r requirements.txt
```

#### Build and upload to PyPi repository
```
$ python setup.py sdist bdist_wheel
$ pip install twine
$ twine upload dist/badgebtle-x.x.x* #<-- Requires credentials.
```
