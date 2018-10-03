def encode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    if shift > 26:
        shift = shift % 26
    kood = ""
    for x in message:
        if x.isalpha():
            alphabet = ord(x) + shift
            if x.isupper():
                if alphabet > ord("Z"):
                    alphabet -= 26
                elif alphabet < ord("A"):
                    alphabet += 26
            if x.islower():
                if alphabet > ord("z"):
                    alphabet -= 26
                elif alphabet < ord("a"):
                    alphabet += 26
            shiffer = chr(alphabet)
            kood += shiffer
    return kood

    pass


def decode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    if shift > 26:
        shift = shift % 26
    kood2 = ""
    for y in message:
        if y.isalpha():
            alphabet = ord(y) + shift
            if y.isupper():
                if alphabet > ord("Z"):
                    alphabet -= 26
                elif alphabet < ord("A"):
                    alphabet += 26
            if y.islower():
                if alphabet > ord("z"):
                    alphabet -= 26
                elif alphabet < ord("a"):
                    alphabet += 26
            shiffer2 = chr(alphabet)
            kood2 += shiffer2
    return kood2

    pass


if __name__ == "__main__":
    # simple tests
    print(encode("Hello", 1))  # ifmmp
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
