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
    if lat > 0:
        tagasitee.append("S"*abs(lat))
    elif lat < 0:
        tagasitee.append("N"*abs(lat))
    elif long > 0:
        tagasitee.append("W"*abs(long))
    elif long < 0:
        tagasitee.append("E"*abs(long))
    return "".join(tagasitee)
    # while True:
    #     if lat > 0:
    #         lat = lat + d["S"][0]
    #         tagasitee.append("S")
    #
    #     elif lat < 0:
    #         lat = lat + d["N"][0]
    #         tagasitee.append("N")
    #
    #     if long > 0:
    #         long = long + d["W"][1]
    #         tagasitee.append("W")
    #
    #     elif long < 0:
    #         long = long + d["E"][1]
    #         tagasitee.append("E")
    #
    #     if lat == 0 and long == 0:
    #         break

    # return "".join(tagasitee)


if __name__ == '__main__':
    shortest_way_back("NNN")  # == "SSS"
    shortest_way_back("SS")  # == "NN"
    shortest_way_back("E")  # == "W"
    shortest_way_back("WWWW")  # == "EEEE"
    shortest_way_back("")  # == ""
    shortest_way_back("NESW")# == ""
    shortest_way_back("NNEESEW") in ["SWW", "WSW", "WWS"]
