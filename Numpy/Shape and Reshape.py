import numpy as np

input_list = list(map(int, input().split()))

arr = np.array(input_list).reshape(3, 3)

print(arr)
