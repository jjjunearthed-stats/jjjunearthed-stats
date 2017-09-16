import json
import pandas
import Date
import re
import gender_guesser.detector as gender
from itertools import groupby


class ArtistStats:
    def __init__(self):
        with open("data/artists.json") as f:
            self.artists = json.loads(f.read())

        with open("data/locationPopulations.json") as f:
            self.locationPopulations = json.loads(f.read())

        with open("data/locationOutliers.json") as f:
            self.locationOutliers = json.loads(f.read())

        self.df = pandas.DataFrame(self.artists)

    @staticmethod
    def flatten(l):
        return [item for sublist in l for item in sublist]

    @staticmethod
    def gender_lookup(gender_name):
        gender_dict = {
            "andy": "Androgynous",
            "female": "Female",
            "male": "Male",
            "mostly_female": "Mostly Female",
            "mostly_male": "Mostly Male",
            "unknown": "Unknown"
        }

        return gender_dict[gender_name]

    def gender_per_genre(self, genre):
        d = gender.Detector()
        artists = self.artists_by_genre(genre)
        names = [re.findall(r"[\w]+", a["members"]) for a in artists]
        names = self.flatten(names)

        genders = [d.get_gender(n) for n in names]
        df = pandas.DataFrame(data=genders, columns=["name"])
        group_by_gender = df.groupby("name").size()

        data = [["Gender", "Number"]]
        for name, size in group_by_gender.iteritems():
            data.append([self.gender_lookup(name), size])

        return data

    def per_capita(self, location, number):
        if location not in self.locationPopulations:
            return None

        return round(number / self.locationPopulations[location] * 100000)

    def by_location(self):
        group_by_location = pandas.DataFrame(self.artists).groupby("location").size()

        data = [["City", "Number of artists"]]
        for name, size in group_by_location.iteritems():
            if name not in self.locationOutliers:
                data.append([name, size])

        return data

    def per_capita_map(self):
        group_by_location = pandas.DataFrame(self.artists).groupby("location").size()

        data = [["Location", "Artists per 100000 people"]]
        for name, size in group_by_location.iteritems():
            location_per_capita = self.per_capita(name, size)

            if location_per_capita is not None:
                data.append([name, location_per_capita])

        return data

    def location_table(self):
        group_by_location = pandas.DataFrame(self.artists).groupby("location").size()
        data = []
        for name, size in group_by_location.iteritems():
            if name not in self.locationOutliers:
                data.append([name, size, self.per_capita(name, size)])

        return data

    def percentage_of_artists(self, genre=None, track_condition=lambda t: True):
        artists_played = [a for a in self.artists_by_genre(genre) if any(filter(track_condition, a["tracks"]))]

        percentage = len(artists_played) / len(self.artists) * 100
        return round(percentage, 2)

    def percentage_of_artists_played_per_genre(self, track_condition=lambda t: True):
        all_genres = self.all_genres()
        data = [["Genre", "Percentage"]]
        for g in all_genres:
            data.append([g, self.percentage_of_artists(g, track_condition)])

        return data

    def all_genres(self):
        return set([g for a in self.artists for g in a["genre"]])

    def genre_percentages(self):
        genres = [g for a in self.artists
                  for g in a["genre"]]

        number_of_genres = len(genres)

        data = [["Genre", "Percentage"]]
        for name, group in groupby(sorted(genres)):
            genre_percentage = len(list(group)) / number_of_genres * 100
            data.append([name, round(genre_percentage, 2)])

        return data

    def artists_by_genre(self, genre):
        return [a for a in self.artists if genre in a["genre"]] if genre is not None else self.artists

    def most_popular_influences(self, genre=None, top_number=50):
        influences = [{"Artist": i} for a in self.artists_by_genre(genre)
                      for i in [inf.strip().lower() for inf in filter(lambda s: s != "", a["influences"].split(","))]]

        grouping = pandas.DataFrame(influences).groupby("Artist").size().sort_values(ascending=False)[:top_number]

        data = [["Artist", "Number"]]
        for name, size in grouping.iteritems():
            data.append([name, size])

        return data

    def most_popular_likes(self, genre=None, top_number=50):
        influences = [{"Artist": l["name"]} for a in self.artists_by_genre(genre)
                      for l in a["likes"]]

        grouping = pandas.DataFrame(influences).groupby("Artist").size().sort_values(ascending=False)[:top_number]

        data = [["Artist", "Number"]]
        for name, size in grouping.iteritems():
            data.append([name, size])

        return data

    def most_popular_tags(self, genre=None, top_number=50):
        tags = [{"Tag": t} for a in self.artists_by_genre(genre)
                for t in a["tags"]]

        grouping = pandas.DataFrame(tags).groupby("Tag").size().sort_values(ascending=False)[:top_number]

        data = [["Tag", "Number"]]
        for name, size in grouping.iteritems():
            data.append([name, size])

        return data

    def group_by_artist_property_per_year(self,
                                          artist_property,
                                          track_condition=lambda t: True,
                                          include_current_year=False):

        genre_years = [{artist_property: g, "year": Date.parse(t["date"]).year}
                       for a in self.artists
                       for g in (a[artist_property] if isinstance(a[artist_property], list) else [a[artist_property]])
                       for t in filter(track_condition, a["tracks"])]

        grouping = pandas.DataFrame(genre_years).groupby(["year", artist_property]).size()
        years = list(grouping.keys().levels[0])
        genres = list(grouping.keys().levels[1])

        data = [["Year"] + genres]

        if include_current_year is False:
            years.pop()

        for year in years:
            year_counts = [str(year)]
            year_grouping = grouping[year]

            for genre in genres:
                if genre in year_grouping:
                    year_counts.append(year_grouping[genre])
                else:
                    year_counts.append(0)

            data.append(year_counts)
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

        # Add missing liked artist
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

        stats_container = {
            "TotalNumberOfArtists": len(self.artists),
            "TotalNumberOfTracks": len(tracks),
            "FromDate": tracks["date"].min(),
            "ToDate": tracks["date"].max(),
            "PercentageOfArtistsPlayedOnJJJ": self.percentage_of_artists(track_condition=lambda t: t["played_on_jjj"]),
            "PercentageOfArtistsPlayedOnUnearthed": self.percentage_of_artists(track_condition=lambda t: t["played_on_unearthed"]),
            "LastUpdated": Date.now()
        }

        return stats_container

