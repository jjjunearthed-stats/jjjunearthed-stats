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


class Track(scrapy.Item):
    name = scrapy.Field()
    plays = scrapy.Field()
    downloads = scrapy.Field()
    loves = scrapy.Field()
    shares = scrapy.Field()
    reviews = scrapy.Field()
    link = scrapy.Field()


class Review(scrapy.Item):
    reviewer = scrapy.Field()
    date = scrapy.Field()
    rating = scrapy.Field()
