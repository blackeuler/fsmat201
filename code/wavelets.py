"""  To calculate the Haar transform of an array of n samples:

    Treat the array as n/2 pairs called (a, b)
    Calculate (a + b) / sqrt(2) for each pair, these values will be the first half of the output array.
    Calculate (a - b) / sqrt(2) for each pair, these values will be the second half.
    Repeat the process on the first half of the array.
    (the array length should be a power of two) """

import math


def lowPass(array):
    low = []
    assert len(array)%2 == 0
    for i in range(0,len(array)-1,2):
        low.append((array[i]+array[i+1])/ math.sqrt(2))
    return low

def highPass(array):
    high = []
    assert len(array)%2 == 0
    for i in range(0,len(array)-1,2):
        high.append((array[i]-array[i+1])/ math.sqrt(2))
    return high

def haar(array):
    if len(array)%2 != 0:
        return array
    high = highPass(array)
    low = lowPass(array)
    return haar(low) + high