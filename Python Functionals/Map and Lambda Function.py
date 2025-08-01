cube = lambda x: x**3


def fibonacci(n):
    a, b = 0, 1
    seq = []
    for i in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
