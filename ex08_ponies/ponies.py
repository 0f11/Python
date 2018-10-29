"""Ponies.py."""
import base64


def decode(line: str) -> str:
    """
    Decode.

    :param line:
    :return:
    """
    decoded = base64.b64decode(line).decode('UTF-8')
    return str(decoded)


def extract_information(line: str) -> dict:
    """
    Extract.

    :param line:
    :return:
    """
    d1 = {}
    new_list = line.split(" ")
    for i in new_list:
        d1["name"] = str(new_list[0:2]).replace("[", '').replace("]", '').replace(",", "").replace("'", "")
        d1["kind"] = new_list[2]
        d1["coat_color"] = new_list[3]
        d1["mane_color"] = new_list[4]
        d1["eye_color"] = new_list[5]
        d1["location"] = str(new_list[6:9]).replace("[", '').replace("]", '').replace(",", "").replace("'", "")
    return d1


def header():
    """
    Header.

    :return:
    """
    line = f"{'PLACE':<{10}}" \
           f"{'POINTS':<{10}}" \
           f"{'NAME':<{20}}" \
           f"{'KIND':<{20}}" \
           f"{'COAT COLOR':<{20}}" \
           f"{'MANE COLOR':<{20}}" \
           f"{'EYE COLOR':<{20}}" \
           f"{'LOCATION':<{20}}"
    line2 = "-" * 128
    return line + "\n" + line2


def read(read_file: str) -> list:
    """
    Read.

    :param read_file:
    :return:
    """
    try:
        list1 = []
        with open(read_file, encoding="UTF-8") as f:
            lines = f.readlines()[2:]
            for line in lines:
                x = decode(line)
                x = x.strip("b'").strip("-").strip("\n")
                if len(x) > 0:
                    x = extract_information(x)
                    list1.append(x)
        return list1
    except FileNotFoundError:
        raise Exception("File not found!")


def filtered_by_location(ponies: list):
    """
    Filtered by loc.

    :param ponies:
    :return:
    """
    list1 = []
    for x in ponies:
        if x['location'] != "None":
            list1.append(x)
    return list1


def filtered_by_kind(ponies, kind):
    """
    Filtered by kind.

    :param ponies:
    :param kind:
    :return:
    """
    list1 = []
    for z in ponies:
        if ponies['kind'] == kind:
            list1.append(z)
    return list1


def get_points_for_color(color):
    """
    Get points for color.

    :param color:
    :return:
    """
    list1 = ['magenta', 'pink', 'purple', 'orange', 'red', 'yellow', 'cyan', 'blue', 'brown', 'green']
    if color in list1:
        pos = list1.index(color)
        points = 10 - pos
    else:
        return None
    return points


def add_points(pony):
    """
    Add points.

    :param pony:
    :return:
    """
    d1 = {
        'coat_color': ['Town Hall', 'Theater', 'School of Friendship'],
        'mane_color': ['Schoolhouse', 'Crusaders Clubhouse', 'Golden Oak Library'],
        'eye_color': ['Train station', 'Castle of Friendship', 'Retirement Village']
    }
    if pony['location'] in d1['coat_color']:
        pony['points'] = get_points_for_color(pony['coat_color'])
    elif pony['location'] in d1['mane_color']:
        pony['points'] = get_points_for_color(pony['mane_color'])
    elif pony['location'] in d1['eye_color']:
        pony['points'] = get_points_for_color(pony['eye_color'])

    return pony


def evaluate_points(ponies):
    """
    Evaluate.

    :param ponies:
    :return:
    """
    list1 = []
    for x in ponies:
        list1.append(add_points(x))
    return list1


def sort_by_name(ponies):
    """
    Sort by name.

    :param ponies:
    :return:
    """
    return sorted(ponies, key=lambda x: x['name'])


def sort_by_points(ponies):
    """
    Sort by points.

    :param ponies:
    :return:
    """
    list1 = []
    for x in ponies is not None:
        if x['points']:
            list1.append(x)
    return sorted(list1, key=lambda x: x['points'], reverse=True)


def format_line(pony, place):
    """
    Format line.

    :param pony:
    :param place:
    :return:
    """
    return f'{place:<{10}}' \
           f"{pony['points']:<{10}}" \
           f"{pony['name']:<{20}}" \
           f"{pony['kind']:<{20}}" \
           f"{pony['coat_color']:<{20}}" \
           f"{pony['mane_color']:<{20}}" \
           f"{pony['eye_color']:<{20}}" \
           f"{pony['location']:<{20}}"


def write(input_file, kind):
    """
    write.

    :param input_file:
    :param kind:
    :return:
    """
    ponies = read(input_file)
    ponies = filtered_by_location(ponies)
    ponies = filtered_by_kind(ponies, kind)
    ponies = evaluate_points(ponies)
    ponies = sort_by_name(ponies)
    ponies = sort_by_points(ponies)
    file_name = "results_for_" + kind + ".txt"
    with open(file_name, "w", encoding="utf-8", newline="\n") as f:
        f.write(header())
        if ponies == []:
            f.write("\n")
        for place, poni in enumerate(ponies):
            f.write("\n" + format_line(poni, place + 1))
