"""Ponies.py."""
import base64


def decode(line: str) -> str:
    decoded = base64.b64decode(line)
    return decoded


def extract_information(line: str) -> dict:
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


def read(read_file: str) -> list:
    data = open(read_file, "r")
    decoded1 = str(data.readlines())
    decoded2 = [decode(decoded1)]
    data.close()
    return decoded2

# print(decode('TWF1ZCBQb21tZWwgICAgICAgICBVbmljb3JuICAgICAgICAgICAgIHBpbmsgICAgICAgICAgICAgICAgZ3JlZW4gICAgICAgICA'
# + 'gICAgICBjeWFuICAgICAgICAgICAgICAgIENhc3RsZSBvZiBGcmllbmRzaGlw'))
print(extract_information("Maud Pommel Unicorn pink green cyan Castle of Friendship"))
