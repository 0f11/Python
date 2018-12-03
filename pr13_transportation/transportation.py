"""Retrieve stops and departures info from REST service."""

import requests

API_BASE = "https://public-transport-api.herokuapp.com"
REGION = "tallinn"


def get_nearby_stops(api_base, lat, lng):
    """
    Get nearby stops.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: List of all nearby stops
    """
    stops = requests.get(api_base + f"/stops/{lat}/{lng}").json()
    return stops


def get_nearest_stop(api_base, lat, lng):
    """
    Get nearest stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: Nearest stop
    """
    stops = requests.get(api_base + f"/stops/{lat}/{lng}").json()
    answer = min(stops, key=lambda d: d['distance'])
    return answer


def get_next_departures(api_base, region, stop_id):
    """
    Get next departures from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: List of next departures from stop
    """
    return requests.get(api_base + f"/departures/{region}/{stop_id}").json()['departures']


def get_next_departure(api_base, region, stop_id):
    """
    Get next departure, from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: Next departure from stop
    """
    departures = requests.get(api_base + f"/departures/{region}/{stop_id}").json()['departures']
    answer = min(departures, key=lambda d: d['timeLocal'])
    return answer


if __name__ == '__main__':
    print(get_nearby_stops(API_BASE, 59.3977111, 24.660198))
    print(get_nearest_stop(API_BASE, 59.3977111, 24.660198))
    print(get_next_departures(API_BASE, REGION, get_nearest_stop(API_BASE, 59.3977111, 24.660198)["id"]))
    print(get_next_departure(API_BASE, REGION, get_nearest_stop(API_BASE, 59.3977111, 24.660198)["id"]))
