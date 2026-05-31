def main():
    text = input("What is your message? ")
    print(shorten(text))


def shorten(word):
    result = ''
    for t in word:
        if t.lower() not in ['a', 'e', 'i', 'o', 'u']:
            result += t
    return result


if __name__ == "__main__":
    main()
