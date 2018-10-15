"""Collect story parts from a messy text."""
import re


def read_file(file) -> str:
    """
    Read the text from given file into string.

    :param file: file path
    :return: string
    """
    file = open(file)
    messy_text = file.read()
    messy_text = get_clean_text(messy_text)
    file.close()
    return messy_text


def get_clean_text(messy_text: str) -> str:
    """
    Process given text, remove unneeded symbols and retrieve a story.

    :param messy_text: string
    :return: clean string
    """
    cypher = "1234567890&@#$%^()_+|><~"
    messy_text = messy_text.replace("*", '"')
    messy_text = messy_text.replace("/", ',')
    messy_text = messy_text.replace(".", '.')
    messy_text = messy_text.replace("!", "?")
    messy_text = messy_text.replace("?", "!")
    for i in messy_text:

        if i in cypher:
            messy_text = messy_text.replace(i, "")

    return re.sub("(^|[.?!\"])\\s*([a-zA-Z])", lambda p: p.group(0).upper(), messy_text)


if __name__ == "__main__":
    print(get_clean_text("82jo2e$ _wa9^&it3ed _^f6o^+&r^(7|0 ~t>h_e4 21&614t)r(34a00(i|n.1_ t<3he@$36) "
                         ">t0(+>>rai1n7^ w_a#65s l~a4t<(e><?6 d&2((|i6_9d 5Ma7r>@++y #an04(@@3d "
                         "<9Samantha t#ake6>8 9t_h#e@ )b77#5+12<us! *)ye9s|/4 80t8hey|^38 1(_##&di++18#d<)?69*/ "
                         "480sa^i1d|0 J2|9&4~oe3&>0."))  # -> Joe waited for the train. The train was late! Did Mary and
    # Samantha take the bus? "Yes, they did!",, said Joe.
