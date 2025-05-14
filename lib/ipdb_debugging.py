#!/usr/bin/env python3

import ipdb

def incorrect_sum(a, b):
    result = a + b  # <-- Fixed: Use addition instead of multiplication
    ipdb.set_trace()
    return result

x = 3
y = 4
print("The result is:", incorrect_sum(x, y))
