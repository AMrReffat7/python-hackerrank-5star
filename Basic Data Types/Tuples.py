if __name__ == '__main__':
    n = int(raw_input())
    integer_tuple = tuple(map(int, raw_input().split()))
    print hash(integer_tuple)
