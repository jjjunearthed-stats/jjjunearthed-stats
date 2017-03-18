import json
import pandas
import File


class ArtistStats:
    def __init__(self, a):
        self.artists = a

    @staticmethod
    def flatten(items, column):
        result = []
        for i in items:
            result.extend(i[column])
        return result

    @staticmethod
    def flatten_append(items, column):
        result = []
        for i in items:
            result.append(i[column].strip())
        return result

    @staticmethod
    def per_capita_by_location(location, number):
        json_data = json.loads(open("data/locationPopulations.json").read())
        for l in json_data:
            if l.get("location") == location:
                population = l.get("population")
                return round(number / population * 100000)

        return None

    def by_location(self):
        group_by_location = pandas.DataFrame(self.artists).groupby(["location"])

        data = [["City", "Number of artists"]]
        for name, group in group_by_location:
            data.append([name, len(group)])

        return data

    def per_capita(self):
        group_by_location = pandas.DataFrame(self.artists).groupby(["location"])

        data = [["Location", "Artists per 100000 people"]]
        for name, group in group_by_location:
            location_per_capita = self.per_capita_by_location(name, len(group))

            if location_per_capita is not None:
                data.append([name, location_per_capita])

        return data

    def location_table(self):
        group_by_location = pandas.DataFrame(self.artists).groupby(["location"])

        data = []
        for name, group in group_by_location:
            data.append([name, len(group), self.per_capita_by_location(name, len(group))])

        return data

    def hierarchial_graph(self):
        data = []
        df = pandas.DataFrame(self.artists)
        for artist in self.artists:
            if artist["name"] is not None:
                data.append({
                    "name": artist["url"].strip(),
                    "size": 10000,
                    "imports": self.flatten_append(artist["likes"], "url")
                })

        # Add missing liked artist todo: this is slow
        for artist in data:
            for like in artist["imports"]:
                if not any(a["url"] == like for a in self.artists) and not any(d["name"] == like for d in data):
                    data.append({
                        "name": like,
                        "size": 10000,
                        "imports": []
                    })

        return data

    def stats(self):
        tracks = pandas.DataFrame(self.flatten(self.artists, "tracks"))
        return {
            "TotalNumberOfArtists": len(self.artists),
            "TotalNumberOfTracks": len(tracks),
            "FromDate": tracks["date"].min(),
            "ToDate": tracks["date"].max()
        }


with open("artists.json") as artists_file:
    stats = ArtistStats(json.load(artists_file))

File.write_file("docs/data/artistsByLocation.json", stats.by_location())
File.write_file("docs/data/artistsPerCapita.json", stats.per_capita())
File.write_file("docs/data/artistsLocationTable.json", stats.location_table())
File.write_file("docs/_data/stats.json", stats.stats())
File.write_file("docs/data/artistHierarchialGraph.json", stats.hierarchial_graph())
