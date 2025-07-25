import numpy as np

x, y, z = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(x + y)]

arr = np.array(data)

print(arr)
