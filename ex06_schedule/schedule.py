"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    file = open(input_filename)
    data = file.read()
    file.close()
    data = data.replace(",", ":").replace("-", ":").replace(".", ":")
    test = create_schedule_string(data)
    test1 = open("schedule_output.txt", "a")
    test1.write(create_schedule_string(test))
    test1.close()


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    schedule_dict = {}
    for match in re.finditer(r"(\d{1,2})[:,-.](\d{1,2})+\s([a-zA-Z]+)", input_string):
        if match[0] not in schedule_dict:
            print(match[0])
            schedule_dict[match[1] + match[2].zfill(2)] = match.group(3)
        else:
            print(schedule_dict[0])

    time_length = len(match.group(1))
    text_length = len(match.group(3))
    for x in schedule_dict:
        if int(x.replace(":", "")) > 1200:
            print(f"| {x:>{time_length}}PM| {schedule_dict[x]:>{text_length}} |")
        elif int(x.replace(":", "")) < 1200:
            print(f"| {x:>{time_length}}AM| {schedule_dict[x]:>{text_length}} |")


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    # create_schedule_file("schedule_input.txt", "schedule_output.txt")
