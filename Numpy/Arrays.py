import numpy


def arrays(arr):
    arr_r = numpy.array(arr[::-1]).astype(float)
    return arr_r


arr = input().strip().split(" ")
result = arrays(arr)
print(result)
