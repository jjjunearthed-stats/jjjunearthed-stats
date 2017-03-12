import scrapy


class Artist(scrapy.Item):
    name = scrapy.Field()
    location = scrapy.Field()
    genre = scrapy.Field()
    members = scrapy.Field()
    links = scrapy.Field()
    tags = scrapy.Field()
    influences = scrapy.Field()
    url = scrapy.Field()
    tracks = scrapy.Field()
    likes = scrapy.Field()


class ArtistRef(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()


class Track(scrapy.Item):
    name = scrapy.Field()
    plays = scrapy.Field()
    downloads = scrapy.Field()
    loves = scrapy.Field()
    shares = scrapy.Field()
    reviews = scrapy.Field()
    link = scrapy.Field()
    played_on_jjj = scrapy.Field()
    played_on_unearthed = scrapy.Field()
    mature = scrapy.Field()
    date = scrapy.Field()


class Review(scrapy.Item):
    reviewer = scrapy.Field()
    date = scrapy.Field()
    rating = scrapy.Field()
