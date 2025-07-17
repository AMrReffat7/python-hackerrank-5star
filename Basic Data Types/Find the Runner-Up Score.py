if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    uniuqe = list(set(arr))
    uniuqe.sort(reverse=True)
    print(uniuqe[1])
