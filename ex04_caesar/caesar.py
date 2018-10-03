def encode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    kood = ""
    if shift >= 26 or shift <= -26:
        shift = shift % 26

    for x1 in message:
        if x1 in alphabet:
            if x1.islower():
                alphabet3 = alphabet.index(x1) + shift
                if alphabet3 >= len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood += alphabet[alphabet3]
                else:
                    kood += alphabet[alphabet3]
            elif x1.isupper():
                alphabet3 = alphabet.index(x1) + shift
                if alphabet3 >= len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood += alphabet[alphabet3]
                else:
                    kood += alphabet[alphabet3]
            elif x1.isnumeric():
                alphabet3 = alphabet.index(x1) + shift
                if alphabet3 >= len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood += alphabet[alphabet3]
                else:
                    kood += alphabet[alphabet3]
            elif x1.isprintable():
                alphabet3 = alphabet.index(x1) + shift
                if alphabet3 >= len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood += alphabet[alphabet3]
                else:
                    kood += alphabet[alphabet3]
            else:
                kood += x1
        else:
            kood += x1
    return kood


def decode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    kood2 = ""
    if shift >= 26 or shift <= -26:
        shift = shift % 26
    for x1 in message:
        if x1 in alphabet:
            if x1.isupper():
                alphabet3 = alphabet.index(x1) - shift
                if alphabet3 >= len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood2 += alphabet[alphabet3]
                else:
                    kood2 += alphabet[alphabet3]
            elif x1.islower():
                alphabet3 = alphabet.index(x1) - shift
                if alphabet3 >= len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood2 += alphabet[alphabet3]
                else:
                    kood2 += alphabet[alphabet3]
            elif x1.isnumeric():
                alphabet3 = alphabet.index(x1) - shift
                if alphabet3 >= len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood2 += alphabet[alphabet3]
                else:
                    kood2 += alphabet[alphabet3]
            elif x1.isprintable():
                alphabet3 = alphabet.index(x1) - shift
                if alphabet3 >= len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood2 += alphabet[alphabet3]
                else:
                    kood2 += alphabet[alphabet3]
            else:
                kood2 += x1
        else:
            kood2 += x1
    return kood2

    pass


if __name__ == "__main__":
    # simple tests
    print(encode("maakera", -27, "ax"))  # ifmmp
    print(encode("$%dSs¤324D#1", 1, ")(/&%¤#"))  # $¤dSs#324D)1
    """
    print(decode("ifmmp", 1))  # hello
    print(decode("ifmmp", 50))
    print(encode("hello", 50))
    print(decode("ifmmp", -3))
    print(encode("hello", -4))
    print(decode("ifmmp", 30))
    print(encode("hello", 27))
    print(decode("iFMmP", 1))
    print(encode("HEllO", 1))
    print(decode("iFM3::134;", 3))
    print(encode("H::13EllO", 1))
    # WRITE THE REMAINING EXAMPLES YOURSELF!

    # larger shift

    # negative shift

    # shift > alphabet.length

    # case sensitivity

    # misc symbols (.,:; etc.)

    # ...
    """
