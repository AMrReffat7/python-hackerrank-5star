if __name__ == "__main__":
    data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])

    unique_scores = sorted(set([score for name, score in data]))
    second_lowest = unique_scores[1]

    names = [name for name, score in data if score == second_lowest]
    names.sort()

    for name in names:
        print(name)
