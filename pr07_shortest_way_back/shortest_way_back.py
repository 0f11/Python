"""Find the shortest way back in a taxicab geometry."""


def shortest_way_back(path: str) -> str:
    """
    Find the shortest way back in a taxicab geometry.

    :param path: string of moves, where moves are encoded as follows:.
    N - north -  (1, 0)
    S - south -  (-1, 0)
    E - east  -  (0, 1)
    W - west  -  (0, -1)
    (first coordinate indicates steps towards north,
    second coordinate indicates steps towards east)

    :return: the shortest way back encoded the same way as :param path:.
    """
    d = {
        "N": (1, 0),
        "S": (-1, 0),
        "E": (0, 1),
        "W": (0, -1)}

    lat = 0
    long = 0

    for direction in path:
        if direction == "N":
            lat = lat + d["N"][0]

        elif direction == "S":
            lat = lat + d["S"][0]

        elif direction == "E":
            long = long + d["E"][1]

        elif direction == "W":
            long = long + d["W"][1]
    tagasitee = []

    while True:
        if lat > 0:
            tagasitee.append(lat * "S")
            lat = lat + (lat * d["S"][0])
        elif lat < 0:
            tagasitee.append(abs(lat) * "N")
            lat = lat + (abs(lat) * d["N"][0])
        if long > 0:
            tagasitee.append(abs(long) * "W")
            long = long + (abs(long) * d["W"][1])
        elif long < 0:
            tagasitee.append(abs(long) * "E")
            long = long + (abs(long) * d["E"][1])
        if lat == 0 and long == 0:
            break

    print("".join(tagasitee))

if __name__ == '__main__':
    shortest_way_back("NNN")  # == "SSS"
    shortest_way_back("SS")  # == "NN"
    shortest_way_back("E")  # == "W"
    shortest_way_back("WWWW")  # == "EEEE"
    shortest_way_back("")  # == ""
    shortest_way_back("NESW")  # == ""
    shortest_way_back("NNEESEW") in ["SWW", "WSW", "WWS"]
