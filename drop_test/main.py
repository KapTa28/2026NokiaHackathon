from pathlib import Path

def calculate_last_part(part_count, height):
    base = int(height / part_count)
    if (part_count % 2 == 0):
        return int(base - part_count + 1)
    return int(base - (part_count - 1) / 2)

def calculate_min_drops_with_parts(part_count, height):
    part_size = int(height / part_count)

    if (part_size < height - part_count * part_size):
        return height

    if (part_count % 2 == 0):
        return part_size + part_count - 1

    return part_size + (part_count - 1) / 2

def max_num_of_drops(object_count, height):
    if (object_count == 1): return height

    part_count = 1
    min_drop_count = height
    if (object_count == 2):
        while (part_count <= min_drop_count):
            min_drop_count = min(min_drop_count, 
                                 calculate_min_drops_with_parts(part_count, height))
            part_count += 1
        #print(f"Part size: {height}, min drop {int(min_drop_count)}")

    else:
        while (part_count <= min_drop_count):
            min_drop_count = min(min_drop_count, 
                                 part_count + max_num_of_drops(object_count - 1, 
                                                               calculate_last_part(part_count, height)) - 1)
            part_count += 1
            # print(f"Total min drop count: {min_drop_count}")
    return int(min_drop_count)

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        parts = line.split(", ")
        print(max_num_of_drops(int(parts[0]), int(parts[1])))

    # print(max_num_of_drops(3, 100))



if __name__ == "__main__":
    main()
