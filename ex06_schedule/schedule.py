"""Create schedule from the given file."""
import re
from datetime import datetime


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    with open(input_filename, encoding="utf-8") as file:
        original_txt = file.read()
    with open(output_filename, 'w') as file:
        file.write(create_schedule_string(original_txt))


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    schedule_dict = {}
    for match in re.finditer(r"[ \n](\d{1,2})[^\d](\d{1,2})\s+([a-zA-z]+)", input_string):
        time = correct_time(match.group(1), match.group(2))
        if re.search(r"^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$", time):
            if time in schedule_dict:
                if match.group(3).lower() in schedule_dict[time]:
                    continue
                else:
                    schedule_dict[time].append(match.group(3).lower())
            else:
                schedule_dict[time] = [match.group(3).lower()]
    sorted_items = sorted(schedule_dict.items(), key=lambda x: x[0])
    if len(sorted_items) == 0:
        return no_items()
    return print_table(sorted_items)


def correct_time(hours, minutes):
    """For checking if the time is correct and outputting correct time."""
    if len(hours) == 1:
        hour = "0" + hours
    else:
        hour = hours
    if len(minutes) == 1:
        minute = "0" + minutes
    else:
        minute = minutes
    return hour + ":" + minute


def no_items():
    """If there is no items, display table."""
    table1 = []
    table1.append(f"{'-' * 18 }")
    table1.append(f"|  time | items  |")
    table1.append(f"{'-' * 18 }")
    table1.append(f"| No items found |")
    table1.append(f"{'-' * 18}")
    return "\n".join(table1)


def min_max_values(sorted_items):
    """
    :param sorted_items:
    :return:
    """
    max_length = 0
    max_value = 5
    for i in sorted_items:
        values = ", ".join(i[1])
        time_12h = datetime.strptime(i[0], "%H:%M")
        time_12h = time_12h.strftime("%I:%M %p")
        if time_12h[0] == "0":
            time_12h = time_12h[1:]
        if len(values) > max_value:
            max_value = len(values)
        if len(time_12h) > max_length:
            max_length = len(time_12h)
    return max_length, max_value


def print_table(sorted_items):
    """
    :param sorted_items:
    :return:
    """
    max_length = min_max_values(sorted_items)[0]
    max_value = min_max_values(sorted_items)[1]
    table1 = []
    table1.append(f"{'-' * (max_length + max_value + 7)}")
    table1.append(f"|{'time':>{max_length + 1}} | {'items':<{max_value}} |")
    table1.append(f"{'-' * (max_length + max_value + 7)}")
    for i in sorted_items:
        values = ", ".join(i[1])
        time_12h = datetime.strptime(i[0], "%H:%M")
        time_12h = time_12h.strftime("%I:%M %p")
        if time_12h[0] == "0":
            time_12h = time_12h[1:]
        table1.append(f"|{time_12h:>{max_length + 1}} | {values :<{max_value}} |")
    table1.append(f"{'-' * (max_length + max_value + 7)}")
    return "\n".join(table1)


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
