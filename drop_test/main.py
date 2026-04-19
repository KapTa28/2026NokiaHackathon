from pathlib import Path
from math import ceil

def drops_with_two_objects(height):
    part_count = 1
    min_drop_count = height
    while (part_count < min_drop_count):
        min_drop_count = min(min_drop_count, 
                             ceil(part_count / 2) + int(height / part_count))
        part_count += 1
    return min_drop_count
    
def max_num_of_drops(object_count, height):
    if (object_count == 1): return height

    min_drop_count = drops_with_two_objects(height)
    height = min_drop_count
    for i in range(2, object_count):
        min_drop_count -= drops_with_two_objects(height)
        height = min_drop_count

    return int(min_drop_count)

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        parts = line.split(", ")
        print(max_num_of_drops(int(parts[0]), 
                               int(parts[1])))
    # print(max_num_of_drops(2, 30))

if __name__ == "__main__":
    main()

