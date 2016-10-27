#!/usr/bin/env python

"""Calculate Shannon entropy for a file or stdin"""

# Python 2.x backwards compatibility
from __future__ import division, print_function

import sys
import math

def byte_count(input_file):
    """Count the frequency of distinct bytes in a file descriptor"""
    counts = [0] * 256
    with input_file as file_h:
        byte = file_h.read(1)
        while byte:
            counts[ord(byte)] += 1
            byte = file_h.read(1)
    return counts

def shannon_entropy(counts):
    """Calculate Shannon entropy from an array of frequencies"""
    bytes_total = sum(counts)
    byte_frequency = [count / bytes_total for count in counts]
    return abs(sum(feq * math.log(feq, 2) if feq else 0 for feq in byte_frequency))

def print_entropy_info(file_handle):
    """Calculate and print Shannon entropy information"""
    file_byte_count = byte_count(file_handle)
    entropy_per_byte = shannon_entropy(file_byte_count)
    print('bytes        : %d' % sum(file_byte_count))
    print('entropy      : %d' % (entropy_per_byte * sum(file_byte_count)))
    print('entropy/byte : %f' % entropy_per_byte)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_entropy_info(open(sys.argv[1], 'rb'))
    elif sys.version_info.major > 2:
        # Read from buffer to access binary data in python 3
        print_entropy_info(sys.stdin.buffer)
    else:
        print_entropy_info(sys.stdin)
