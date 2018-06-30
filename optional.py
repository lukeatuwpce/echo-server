#!/usr/bin/env python3
import socket
"""
Simple:

Write a python function that lists the services provided by a given range of ports.

accept the lower and upper bounds as arguments
provide sensible defaults
Ensure that it only accepts valid port numbers (0-65535)
"""

def _getservbyports(begin, end):
    if begin < 0 or end > 65525 or begin > end:
        print(f"Usage: {__name__}(begin, end) with begin > 0, "
              f"end < 65535, and begin > end")
        return None

    out = ''

    while begin <= end:
        try:
            out += (f"tcp port {begin}: {socket.getservbyport(begin, 'tcp')}\n")
        except OSError:
            out += (f"tcp port {begin}: (none)\n")
        try:
            out += (f"udp port {begin}: {socket.getservbyport(begin, 'udp')}\n")
        except OSError:
            out += (f"udp port {begin}: (none)\n")
        begin += 1

    return out

def getservbyports(begin, end):
    out = _getservbyports(begin, end)
    if out:
        print(out)


if __name__ == "__main__":
    assert(not _getservbyports(-1,1))
    assert(not _getservbyports(1,65536))
    assert(not _getservbyports(10, 5))
    assert(_getservbyports(1,10))
    eighteen = """tcp port 18: msp
udp port 18: msp
"""
    assert(_getservbyports(18,18) == eighteen)
