from pathlib import Path
from math import ceil


def construct_magic_num(half, length):
    half = str(half)

    if ((length + 1) / 2 < len(half)):
        half = half[:-1]

    if (length % 2 == 0):
        return int(half + half[::-1])
    
    return int(half + half[::-1][1:])

def parse_num(string):
    if ("^" not in string):
        return string
    
    parts = string.split("^")

    return str(pow(int(parts[0]), int(parts[1])))

def next_magic_num(num_string):
    length = len(num_string)
    inspected_num = int(num_string[:ceil(length / 2)])
    inspected_length = len(str(inspected_num))

    next_num = construct_magic_num(inspected_num, length)
    while(next_num <= int(num_string)):
        inspected_num += 1
        new_length = len(str(inspected_num))
        if (new_length > inspected_length):
            length += 1
            inspected_length = new_length
        next_num = construct_magic_num(inspected_num, length)

    return next_num

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for num_string in data.splitlines():
        print(next_magic_num(parse_num(num_string)))


if __name__ == "__main__":
    main()
