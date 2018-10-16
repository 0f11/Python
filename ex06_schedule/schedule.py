"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    file = open(input_filename)
    data = file.read()
    file.close()
    data = data.replace(",", ":").replace("-", ":").replace(".", ":")
    test = create_schedule_string(data)
    return test


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    schedule_dict = {}

    for match in re.finditer(r"(\d{1,2}[:,-.]\d{1,2})+\s([a-zA-Z]+)", input_string):
        schedule_dict[match.group(1)] = match.group(2)
    print(((len(match.group(1)) + len(match.group(2)))*2+3) * "-")
    print("|", (" " * (len(match.group(1)) + 4)), "time | items", (((len(match.group(2)))-2) * " "), "|")
    print(((len(match.group(1)) + len(match.group(2))) * 2 + 3) * "-")
    for x in schedule_dict:
        if int(x.replace(":", "")) > 1200:
            print(f"| {x:>10} PM | {schedule_dict[x]:>17} |")
        elif int(x.replace(":", "")) < 1200:
            print(f"| {x:>10} AM | {schedule_dict[x]:>17} |")
    print(((len(match.group(1)) + len(match.group(2))) * 2 + 3) * "-")

if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
