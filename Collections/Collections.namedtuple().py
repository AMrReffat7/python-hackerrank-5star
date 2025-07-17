from collections import namedtuple

if __name__ == "__main__":
    n, fields = int(input()), input().split()
    Student = namedtuple("Student", fields)
    print("%.2f" % (sum(int(Student(*input().split()).MARKS) for _ in range(n)) / n))
