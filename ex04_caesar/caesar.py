"""Caesar cipher."""


def encode(message: str, shift: int, alphabet="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    kood = ""
    if shift >= 52 or shift <= -52:
        shift = shift % 52
    for x1 in message:
        if x1 in alphabet:
            if x1.isprintable():
                if len(str(alphabet)) > 26:
                    alphabet3 = alphabet.find(x1) + shift * 2
                else:
                    alphabet3 = alphabet.find(x1) + shift
                if abs(alphabet3) >= len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood += alphabet[alphabet3]
                else:
                    kood += alphabet[alphabet3]
        else:
            kood += x1
    return kood


def decode(message: str, shift: int, alphabet="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") -> str:
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    kood2 = ""
    if shift >= 52 or shift <= -52:
        shift = shift % 52
    for x1 in message:
        if x1 in alphabet:
            if x1.isprintable():
                if len(str(alphabet)) > 26:
                    alphabet3 = alphabet.find(x1) - shift * 2
                else:
                    alphabet3 = alphabet.find(x1) - shift
                if abs(alphabet3) >= len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood2 += alphabet[alphabet3]
                else:
                    kood2 += alphabet[alphabet3]

        else:
            kood2 += x1
    return kood2
    pass


if __name__ == "__main__":
    # simple tests

    print(encode("HeLLO", 1))
    print(encode("maakera", 11, "ax"))  # ifmmp
    print(encode("$%dSs¤324D#1", 1, ")(/&%¤#"))  # $¤dSs#324D)1
    print(decode("iFmmp", 1))  # hello

    print(decode("ifmmp", 51))

    print(encode("hello", 50))
    print(decode("ifmmp", -3))
    print(encode("hello", -4))
    print(decode("ifmmp", 30))
    print(encode("hello", 27))
    print(decode("iFMmP", 1))
    print(encode("HEllO", 1))
    print(decode("iFM3::134;", 3))
    print(encode("H::13EllO", 1))
