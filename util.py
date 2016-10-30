import requests
from math import *
import json
from operator import itemgetter

google_key = open('google_places_api_key.txt', 'r').read()
radius = 1000
limit = 5

test_locations = [(35.903636, -79.043628), (35.915680, -79.048175), (35.907672, -79.054301), (35.896418, -79.057854)]

def spherical_distance(long1, lat1, long2, lat2):
    long1 = long1 * pi / 180
    lat1 = lat1 * pi / 180
    long2 = long2 * pi / 180
    lat2 = lat2 * pi / 180
    return acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long2 - long1))

def geographical_midpoint(list_of_locations):
    """
    list_of_locations == [(lat, long), (lat, long), ...]
    """
    total_x = 0
    total_y = 0
    total_z = 0

    for (lat, long) in list_of_locations:
        lat = lat * pi / 180
        long = long * pi / 180
        total_x += cos(lat) * cos(long)
        total_y += cos(lat) * sin(long)
        total_z += sin(lat)

    x_ave = total_x / len(list_of_locations)
    y_ave = total_y / len(list_of_locations)
    z_ave = total_z / len(list_of_locations)
    
    long = atan2(y_ave, x_ave)
    hyp = sqrt(x_ave * x_ave + y_ave * y_ave)
    lat = atan2(z_ave, hyp)

    return (lat * 180 / pi, long * 180 / pi)

def get_list_of_locations(list_of_locations, types=[], limits=5):
    lat, long = geographical_midpoint(list_of_locations)
    print lat, long
    google_base = "https://maps.googleapis.com/maps/api/place/nearbysearch/json" 
    parameters = {
            'key': google_key,
            'location': "%s, %s" % (lat, long),
            'radius': radius,
            }

    result = []
    asciir = ""

    for type in types:
        parameters['type'] = type
        r = requests.get(google_base, params = parameters)
        asciir += r.text
        result += r.json()['results']

    result = sorted(result, key = lambda item: spherical_distance(item["geometry"]["location"]["lng"],
                                                                  item["geometry"]["location"]["lat"],
                                                                  long, lat))[:limits]

    #print asciir

    #return result

    esri_format = {"type": "FeatureCollection",
                   "features": []}

    for r in result:
        esri_format['features'].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [r["geometry"]["location"]["lng"],
                                r["geometry"]["location"]["lat"]]
            },
            "properties": r
            })
    
    return esri_format

print get_list_of_locations(test_locations, ['restaurant'])
