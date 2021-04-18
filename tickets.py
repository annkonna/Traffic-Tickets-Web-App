import urllib.request
import json


def get_ticket_data(url):
    response = urllib.request.urlopen(url)
    content = json.loads(response.read().decode())

    loc = []
    for rec in content:
        if 'latitude' in rec and 'longitude' in rec and 'viodesc' in rec:
            loc.append(
                [float(rec['latitude']),
                 float(rec['longitude']),
                 rec['viodesc']])

    return json.dumps(loc)
