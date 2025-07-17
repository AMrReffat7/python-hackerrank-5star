def transformSentence(sentence):
    words = sentence.split()
    transformed_words = []

    for word in words:
        if not word:
            transformed_words.append("")
            continue

        result = [word[0]]

        for i in range(1, len(word)):
            prev = word[i - 1]
            curr = word[i]

            if prev.lower() < curr.lower():
                result.append(curr.upper())
            elif prev.lower() > curr.lower():
                result.append(curr.lower())
            else:
                result.append(curr)

        transformed_words.append("".join(result))

    return " ".join(transformed_words)


if __name__ == "__main__":

    sentence = input()
    result = transformSentence(sentence)
    print(result)
