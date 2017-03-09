import scrapy
import Items
from scrapy import cmdline


def get_artists(response):
    name = response.css("h1#unearthed-profile-title ::text").extract_first()
    location = response.css("span.genres.location span.location ::text").extract_first()
    genre = response.css("span.genres.location span.genre ::text").extract()
    website = response.xpath("//h3[.='Website'][1]/following-sibling::p[1]/a/text()").extract()
    social_links = response.xpath("//ul[@class ='social']/li/a/@href").extract()
    tags = response.xpath("//h3[.='Tags'][1]/following-sibling::p/a/text()").extract()
    members = response.xpath("//h3[.='band members'][1]/following-sibling::p/text()").extract_first()
    influences = response.xpath("//h3[.='Influences'][1]/following-sibling::p/text()").extract_first()

    return Items.Artist(
        name=name,
        location=location,
        genre=genre,
        members="" if members is None else list(map(lambda s: s.strip(), members.split(","))),
        links=website+social_links,
        tags=tags,
        influences="" if influences is None else list(map(lambda s: s.strip(), influences.split(","))),
        url=response.url,
        tracks=get_tracks(response)
    )


def get_tracks(response):
    track_names = response.css("div.track_name ::text").extract()
    track_plays = response.xpath("//p[@class='plays'][1]/following-sibling::p/text()").extract()
    track_downloads = response.xpath("//p[@class='downloads'][1]/following-sibling::p/text()").extract()
    track_loves = response.xpath("//p[@class='loves'][1]/following-sibling::p/text()").extract()
    track_shares = response.xpath("//p[@class='shares'][1]/following-sibling::p/text()").extract()
    track_links = response.xpath("//a[@class='download'][1]/@href").extract()

    tracks = [Items.Track(
        name=name,
        plays=track_plays[i],
        downloads=track_downloads[i],
        loves=track_loves[i],
        link="https://www.triplejunearthed.com" + track_links[i],
        shares=track_shares[i]) for i, name in enumerate(track_names)]

    for track in tracks:
        track["reviews"] = list(get_reviews(response, track["name"]))

    return tracks


def get_reviews(response, track_name):
    review_tracks = response.css("h4.track ::text").extract()
    review_reviewers = response.css("a.reviewer_name ::text").extract()
    review_dates = response.css("p.review_date ::text").extract()
    review_ratings = response.css("div.stars ::text").extract()

    for i, review_track in enumerate(review_tracks):
        if review_track.strip() == track_name.strip():
            yield Items.Review(
                reviewer=review_reviewers[i].strip(),
                date=review_dates[i].strip(),
                rating=to_rating(review_ratings[i].strip()))


def to_rating(rating):
    return {
        "00": 0,
        "05": 0.5,
        "10": 1,
        "15": 1.5,
        "20": 2,
        "25": 2.5,
        "30": 3,
        "35": 3.5,
        "40": 4,
        "45": 4.5,
        "50": 5,
    }[rating]


class JJJUnearthedSpider(scrapy.Spider):
    name = "JJJUnearthedSpider"
    download_delay = 3
    start_urls = ["https://www.triplejunearthed.com/artist/lonelyspeck"]

    def parse(self, response):
        yield get_artists(response)
        nextpages = response.xpath("//p/a[contains(@href, '/artist/')]/@href").extract()

        for nextpage in nextpages:
            next_page = nextpage
            if next_page:
                yield scrapy.Request(response.urljoin(next_page), callback=self.parse)


cmdline.execute("scrapy runspider JJJUnearthedSpider.py -t json -o artists.json".split())
