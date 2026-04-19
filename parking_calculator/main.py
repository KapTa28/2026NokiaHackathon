from pathlib import Path
from datetime import datetime, timedelta

ERROR_PATH = "error.log"
RESULTS_PATH = "output.txt"

def clear_file(path):
    with open(path, "w") as f:
            f.write("")

def write_to_file(result):
    with open(RESULTS_PATH, "a") as f:
        f.write(result + "\n")

def log_error(message):
    with open(ERROR_PATH, "a") as f:
        f.write(message + "\n")

def get_timespan_string(start, end):
    timespan: timedelta = end - start
    total_minutes = calculate_total_minutes(timespan)

    if (total_minutes < 60):
        return f"{total_minutes} perc"
    
    return f"{int(total_minutes / 60)} óra"

def calculate_total_minutes(timespan: timedelta):
    return int(timespan.total_seconds() / 60) + 1 

def parse_datetime(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    except BaseException:
        raise BaseException("Could not parse datetime")

def calculate_parking_fee(start, end):
    timespan = end - start

    if (calculate_total_minutes(timespan) < 0):
        raise BaseException("Time span is negative")

    fee = timespan.days * 10000

    timespan -= timedelta(days=timespan.days)
    
    total_minutes = calculate_total_minutes(timespan)

    if (total_minutes < 30):
        return fee

    remaining_hours = int((total_minutes - 30) / 60)
    if (remaining_hours < 3):
        fee += (remaining_hours + 1) * 300
    else:
        fee += 3 * 300 + (remaining_hours - 3) * 500

    return fee

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    lines = data.split("=\n")[1].splitlines()

    clear_file(ERROR_PATH)
    clear_file(RESULTS_PATH)

    for line in lines:
        try:
            parts = line.split("\t\t")
            start = parse_datetime(parts[1])
            end = parse_datetime(parts[2])
            fee = calculate_parking_fee(start, end)
            print(f"{get_timespan_string(start, end)} parkolás -> {fee} forint")
            write_to_file(f"{parts[0]}: {fee} forint")
        except BaseException as e:
            log_error(f"{parts[0]}: {e}")


if __name__ == "__main__":
    main()
