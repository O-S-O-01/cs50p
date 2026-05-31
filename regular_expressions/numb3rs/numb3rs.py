import re
import sys


def main():
    ip = input("IPv4 Address: ").strip()
    print(validate(ip))


def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)

    if not matches:
        return False

    parts = matches.groups()

    for part in parts:
        if int(part) > 255:
            return False

        if len(part) > 1 and part.startswith("0"):
            return False

    return True


if __name__ == "__main__":
    main()