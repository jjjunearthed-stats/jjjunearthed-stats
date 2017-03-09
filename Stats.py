import json
import pandas
import File


def playsoverall(band):
    trackplays = list(map(lambda t: int(t["plays"]), band["tracks"]))
    return sum(trackplays)


def mostplayedtrack(band):
    trackplays = list(map(lambda t: int(t["plays"]), band["tracks"]))
    return max(trackplays)


def flatten(coll):
    result = []
    for i in coll:
        result.extend(i["influences"])
    return result


def artists_by_location(artists):
    group_by_location = pandas.DataFrame(artists).groupby(['location'])

    data = [["City", "Number"]]
    for name, group in group_by_location:
        data.append([name, len(group)])

    File.write_file("docs/data/artistsByLocation.json", data)


with open("artists.json") as artists_file:
    bands = json.load(artists_file)

    bandMostPlays = max(bands, key=playsoverall)
    bandmostplayedtrack = max(bands, key=mostplayedtrack)
    artists_by_location(bands)

    print("Band most played: " + bandMostPlays["name"])
    print("Band most played track: " + bandmostplayedtrack["name"])
