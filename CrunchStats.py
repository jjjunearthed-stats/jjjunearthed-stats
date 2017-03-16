import json

import pandas

import File


def playsoverall(band):
    trackplays = list(map(lambda t: int(t["plays"]), band["tracks"]))
    return sum(trackplays)


def mostplayedtrack(band):
    trackplays = list(map(lambda t: int(t["plays"]), band["tracks"]))

    if len(trackplays) == 0:
        return 0
    return max(trackplays)


def flatten(coll):
    result = []
    for i in coll:
        result.extend(i["influences"])
    return result


def per_capita(location, number):
    json_data = json.loads(open("data/locationPopulations.json").read())
    for l in json_data:
        if l.get("location") == location:
            population = l.get("population")
            return round(number / population * 100000)

    return None


def artists_by_location(artists):
    group_by_location = pandas.DataFrame(artists).groupby(['location'])

    data = [["City", "Number of artists"]]
    for name, group in group_by_location:
        data.append([name, len(group)])

    File.write_file("docs/data/artistsByLocation.json", data)


def artists_per_capita(artists):
    group_by_location = pandas.DataFrame(artists).groupby(['location'])

    data = [["City", "Number of artists per 100000 people"]]
    for name, group in group_by_location:
        location_per_capita = per_capita(name, len(group))

        if location_per_capita is not None:
            data.append([name, location_per_capita])

    File.write_file("docs/data/artistsPerCapita.json", data)


def artist_hierarchial_graph(artists):
    File.delete_content("docs/data/artistHierarchialGraph.json")
    with open("docs/data/artistHierarchialGraph.json", "w") as file:
        for artist in artists:
            likes_json = json.dumps(artist["likes"], default=lambda o: o.__dict__)
            json.dump({"name": artist["name"], "size": 100, "imports": [likes_json]}, file)

# "" if influences is None else list(map(lambda s: s.strip(), influences.split(",")))
with open("artists.json") as artists_file:
    bands = json.load(artists_file)

    bandMostPlays = max(bands, key=playsoverall)
    bandmostplayedtrack = max(bands, key=mostplayedtrack)
    artists_by_location(bands)
    artists_per_capita(bands)
    artist_hierarchial_graph(bands)

    print("Band most played: " + bandMostPlays["name"])
    print("Band most played track: " + bandmostplayedtrack["name"])
