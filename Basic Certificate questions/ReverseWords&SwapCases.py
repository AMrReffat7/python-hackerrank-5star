#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#


def reverse_words_order_and_swap_cases(sentence):
    reversed_words = " ".join(sentence.split()[::-1])
    swapped = reversed_words.swapcase()
    return swapped


if __name__ == "__main__":

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    print(result)
