from ArtistsStats import ArtistStats
import File

stats = ArtistStats()

# File.write_file("docs/data/artistsByLocation.json", stats.by_location())
# File.write_file("docs/data/artistsPerCapita.json", stats.per_capita_map())
# File.write_file("docs/data/artistsLocationTable.json", stats.location_table())
# File.write_file("docs/_data/stats.json", stats.stats())
# File.write_file("docs/data/mostPopularInfluences.json", stats.most_popular_influences())
# File.write_file("docs/data/mostPopularLikes.json", stats.most_popular_likes())
# File.write_file("docs/data/mostPopularTags.json", stats.most_popular_tags())


all_genres = stats.all_genres()

File.write_file("docs/data/gendersStacked.json", stats.genders_stacked(all_genres))

# for g in all_genres:
#     genre_filename = g.replace(" ", "")
#     File.write_file("docs/data/mostPopularInfluences" + genre_filename + ".json", stats.most_popular_influences(g))
#     File.write_file("docs/data/mostPopularLikes" + genre_filename + ".json", stats.most_popular_likes(g))
#     File.write_file("docs/data/mostPopularTags" + genre_filename + ".json", stats.most_popular_tags(g))

# File.write_file("docs/data/genrePercentages.json", stats.genre_percentages())
#
# File.write_file("docs/data/genresPlayedOnJJJ.json",
#                 stats.percentage_of_artists_played_per_genre(lambda t: t["played_on_jjj"]))
# File.write_file("docs/data/genresPlayedOnUnearthed.json",
#                 stats.percentage_of_artists_played_per_genre(lambda t: t["played_on_unearthed"]))
#
# File.write_file("docs/data/genresPerYear.json", stats.group_by_artist_property_per_year("genre"))
# File.write_file("docs/data/genresPlayedOnJJJPerYear.json",
#                 stats.group_by_artist_property_per_year("genre", lambda t: t["played_on_jjj"]))
# File.write_file("docs/data/locationsPlayedOnJJJPerYear.json",
#                 stats.group_by_artist_property_per_year("location", lambda t: t["played_on_jjj"]))
# File.write_file("docs/data/genresPlayedOnUnearthedPerYear.json",
#                 stats.group_by_artist_property_per_year("genre", lambda t: t["played_on_unearthed"]))
# File.write_file("docs/data/locationsPlayedOnUnearthedPerYear.json",
#                 stats.group_by_artist_property_per_year("location", lambda t: t["played_on_unearthed"]))
