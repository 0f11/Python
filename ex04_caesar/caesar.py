def encode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    kood = ""
    for x in message:
        if x.isalpha():
            alphabet = ord(x) + shift
            if alphabet > ord('z'):
                alphabet -= 26
            viimane = chr(alphabet)
            kood += viimane
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
    kood2 = ""
    for y in message:
        if y.isalpha():
            alphabet = ord(y) - shift

        if alphabet > ord('z'):
            alphabet += 26
        viimane2 = chr(alphabet)
        kood2 += viimane2
    return kood2
    pass


if __name__ == "__main__":
    # simple tests
    print(encode("hello", 1))  # ifmmp
    print(decode("ifmmp", 1))  # hello

    # WRITE THE REMAINING EXAMPLES YOURSELF!

    # larger shift

    # negative shift

    # shift > alphabet.length

    # case sensitivity

    # misc symbols (.,:; etc.)

    # ...
