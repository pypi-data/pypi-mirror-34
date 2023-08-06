# Safe Netrc

This package provides a subclass of the Python standard library
[`netrc.netrc` class](https://docs.python.org/3/library/netrc.html) to add some
custom behaviors.

1.   If the ``NETRC`` environment variable is defined, then use it as
     the default netrc file path.

2.   Backport permissions checks that were added in Python 3.1
     (see https://bugs.python.org/issue14984).

3.   Apply permissions checks whether or or not we are reading from the
     default netrc file, and whether or not the file contains passwords.

## Installation

    pip install safe-netrc

## Usage

    >>> from safe_netrc import netrc
