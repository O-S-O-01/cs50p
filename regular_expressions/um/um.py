import re
def main():
    text = input('Text: ')

    total = count(text)

    print (total)
    
def count(s):
    pattern = r'\bum\b'

    matches = re.findall(pattern, s, re.IGNORECASE)

    return len(matches)

if __name__ == "__main__":
    main()