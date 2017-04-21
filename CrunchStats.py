import json
import pandas
import File
from datetime import datetime
from itertools import groupby


class ArtistStats:
    def __init__(self, a):
        self.artists = a

    @staticmethod
    def per_capita_by_location(location, number):
        json_data = json.loads(open("data/locationPopulations.json").read())
        for l in json_data:
            if l.get("location") == location:
                population = l.get("population")
                return round(number / population * 100000)

        return None

    @staticmethod
    def to_date(date):
        return datetime.strptime(date, "%Y-%m-%d")

    def by_location(self):
        group_by_location = pandas.DataFrame(self.artists).groupby("location").size()

        data = [["City", "Number of artists"]]
        for name, size in group_by_location.iteritems():
            data.append([name, int(size)])

        return data

    def per_capita(self):
        group_by_location = pandas.DataFrame(self.artists).groupby("location").size()

        data = [["Location", "Artists per 100000 people"]]
        for name, size in group_by_location.iteritems():
            location_per_capita = self.per_capita_by_location(name, int(size))

            if location_per_capita is not None:
                data.append([name, location_per_capita])

        return data

    def location_table(self):
        group_by_location = pandas.DataFrame(self.artists).groupby("location").size()
        data = []
        for name, size in group_by_location.iteritems():
            data.append([name, int(size), self.per_capita_by_location(name, int(size))])

        return data

    def percentage_of_artists(self, track_condition=lambda t: True):
        artists_played_on_jjj = [a for a in self.artists
                                 for t in filter(track_condition, a["tracks"])]

        percentage = len(artists_played_on_jjj) / len(self.artists) * 100
        return round(percentage, 2)

    def genre_percentages(self):
        genres = [g for a in self.artists for g in a["genre"]]
        number_of_genres = len(genres)

        data = [["Genre", "Percentage"]]
        for name, group in groupby(sorted(genres)):
            genre_percentage = len(list(group)) / number_of_genres * 100
            data.append([name, round(genre_percentage, 2)])

        return data

    def genres_per_year(self, track_condition=lambda t: True):
        genre_years = [{"genre": g, "year": self.to_date(t["date"]).year}
                       for a in self.artists for g in a["genre"]
                       for t in filter(track_condition, a["tracks"])]

        grouping = pandas.DataFrame(genre_years).groupby(["year", "genre"]).size()

        data = [["Year", "Genre", "Number Of Tracks"]]
        for group, size in grouping.iteritems():
            data.append([group[0], group[1], int(size)])
        return data

    def hierarchial_graph(self):
        data = []
        for artist in self.artists:
            if artist["name"] is not None:
                data.append({
                    "name": artist["url"],
                    "size": 1,
                    "imports": [l["url"] for a in self.artists for l in a["likes"]]
                })

        # Add missing liked artist todo: this is slow
        for artist in data:
            for like in artist["imports"]:
                if not any(a["url"] == like for a in self.artists):
                    data.append({
                        "name": like,
                        "size": 1,
                        "imports": []
                    })

        return data

    def stats(self):
        tracks = pandas.DataFrame([t for a in self.artists for t in a["tracks"]])
        return {
            "TotalNumberOfArtists": len(self.artists),
            "TotalNumberOfTracks": len(tracks),
            "FromDate": tracks["date"].min(),
            "ToDate": tracks["date"].max(),
            "PercentageOfArtistsPlayedOnJJJ": self.percentage_of_artists(lambda t: t["played_on_jjj"]),
            "PercentageOfArtistsPlayedOnUnearthed": self.percentage_of_artists(lambda t: t["played_on_unearthed"]),
        }


with open("artists.json") as artists_file:
    stats = ArtistStats(json.load(artists_file))

File.write_file("docs/data/artistsByLocation.json", stats.by_location())
File.write_file("docs/data/artistsPerCapita.json", stats.per_capita())
File.write_file("docs/data/artistsLocationTable.json", stats.location_table())
File.write_file("docs/_data/stats.json", stats.stats())
File.write_file("docs/data/genrePercentages.json", stats.genre_percentages())
File.write_file("docs/data/genresPerYear.json", stats.genres_per_year())
File.write_file("docs/data/genresPlayedOnJJJPerYear.json", stats.genres_per_year(lambda t: t["played_on_jjj"]))
File.write_file("docs/data/genresPlayedOnUnearthedPerYear.json", stats.genres_per_year(lambda t: t["played_on_unearthed"]))
