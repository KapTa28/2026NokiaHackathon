from pathlib import Path
from math import ceil

def max_num_of_drops(object_count, height):
    if (object_count == 1): return height

    part_count = 1
    min_drop_count = height
    while (part_count < min_drop_count):
        min_drop_count = min(min_drop_count, 
                             ceil(part_count * (object_count - 1) / object_count) + max_num_of_drops(object_count - 1, 
                                                                     ceil(height / part_count) - 1))
        part_count += 1
    return int(min_drop_count)

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        parts = line.split(", ")
        print(max_num_of_drops(int(parts[0]), 
                               int(parts[1])))

if __name__ == "__main__":
    main()
