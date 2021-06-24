#!/usr/bin/env python3
import random

def random_hex(digits = 12):
    """Generate a string of random hexadecimal digit and return as a string.
    
    Arguments:
    digits: the number of hexadecimal digits to create
    """
    str_hex = ''.join([''.join(random.choice("0123456789ABCDEF")) for _ in range(digits)])
    return str_hex


def format_mac(str_hex):
    """Accept a string of hexadecimal digits and return a string of MAC address format.
    
    Arguments:
    str_hex: a string of hexadecimal digits
    """
    i = 1
    str_mac = ':'.join([str_hex[i:i+2] for i in range(0, 12, 2)])
    return str_mac

# Print a random MAC address
print(format_mac(random_hex()))



