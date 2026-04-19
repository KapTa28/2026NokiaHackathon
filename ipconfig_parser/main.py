from pathlib import Path
from json import dumps

def parse_property(line):
    line = line.strip()

    parts = line.split(" :")

    if (len(parts) == 1):
        return [parts[0]]

    name = parts[0].split(".")[0].strip().lower().replace(" ", "_")
    value = parts[1].strip()

    return [name, value]

def parse_adapter(lines):
    adapter = dict()
    adapter["name"] = lines[0].replace(":", "")

    previous_part_name = ""
    for property_line in lines[1:]:
        parts = parse_property(property_line)

        if (len(parts) == 1):
            adapter[previous_part_name] = [adapter[previous_part_name], parts[0]]
            continue

        adapter[parts[0]] = parts[1]
        previous_part_name = parts[0]

    return adapter

def parse_file(path):
    adapters = []

    result = {
        "file_name": "ipconfig.log"
    }

    data = Path(path).read_text(encoding="utf-16 le")
    
    parts = data.split("\n\n")

    if (parts[1][0] == " "):
        for line in parts[1].splitlines():
            config_data = parse_property(line)
            result[config_data[0]] = config_data[1]
        parts = parts[2:]
    else:
        parts = parts[1:]

    new_parts = []
    for i in range(0, len(parts) - 1, 2):
        new_parts.append(str.join("\n", [parts[i], parts[i+1]]))

    for part in new_parts:
        adapters.append(parse_adapter(part.strip().split("\n")))

    result["adapters"] = adapters

    return result

def main():

    results = []
    for path in sorted(Path(".").glob("*.txt")):
        results.append(parse_file(path))
    print(dumps(results, indent=2))

if __name__ == "__main__":
    main()
