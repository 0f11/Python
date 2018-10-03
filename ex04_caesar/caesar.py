def encode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    kood = ""
    if shift > 26:
        shift = shift % 26
    for x1 in message:
        if x1 in alphabet:
            if x1.isupper():
                alphabet3 = alphabet.index(x1) + shift
                if alphabet3 > len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood += alphabet[alphabet3]
                else:
                    kood += alphabet[alphabet3]
            elif x1.islower():
                alphabet3 = alphabet.index(x1) + shift
                if alphabet3 > len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood += alphabet[alphabet3]
                else:
                    kood += alphabet[alphabet3]
            elif x1.isnumeric():
                alphabet3 = alphabet.index(x1) + shift
                if alphabet3 > len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood += alphabet[alphabet3]
                else:
                    kood += alphabet[alphabet3]
            else:
                kood += x1
        else:
            kood += x1
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
    if shift > 26:
        shift = shift % 26
    for x1 in message:
        if x1 in alphabet:
            if x1.isupper():
                alphabet3 = alphabet.index(x1) - shift
                if alphabet3 > len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood2 += alphabet[alphabet3]
                else:
                    kood2 += alphabet[alphabet3]
            elif x1.islower():
                alphabet3 = alphabet.index(x1) - shift
                if alphabet3 > len(str(alphabet)):
                    alphabet3 = alphabet3 % len(str(alphabet))
                    kood2 += alphabet[alphabet3]
                else:
                    kood2 += alphabet[alphabet3]
            elif x1.isnumeric():
                alphabet3 = alphabet.index(x1) - shift
                if alphabet3 > len(str(alphabet)):
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
