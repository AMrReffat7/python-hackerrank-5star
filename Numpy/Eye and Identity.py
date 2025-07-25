import numpy as np

np.set_printoptions(legacy="1.13")

n, m = map(int, input().split())

arr = np.eye(n, m)

print(arr)
