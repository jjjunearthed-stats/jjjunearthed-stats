import scrapy
import Items
import XPath


class JJJUnearthedSpider(scrapy.Spider):
    name = "JJJUnearthedSpider"
    download_delay = 5
    start_urls = ["https://www.triplejunearthed.com/artist/rainbow-chan"]

    @staticmethod
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

    @staticmethod
    def get_artist_likes(response):
        like_urls = response.xpath(
            "//div[@class='content_module module_artistinfo'][1]/div/p/a[contains(@href, '/artist/')]/@href").extract()
        like_names = response.xpath(
            "//div[@class='content_module module_artistinfo'][1]/div/p/a[contains(@href, '/artist/')]/text()").extract()

        for i, like_url in enumerate(like_urls):
            yield Items.ArtistRef(
                url="https://www.triplejunearthed.com" + like_url,
                name=like_names[i].strip()
            )

    def get_artists(self, response):
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
            members="" if members is None else members.strip(),
            links=website + social_links,
            tags=tags,
            influences="" if influences is None else influences.strip(),
            url=response.url,
            tracks=self.get_tracks(response),
            likes=list(self.get_artist_likes(response))
        )

    @staticmethod
    def played_on_jjj(response, name):
        played = response.xpath(
            "//div[@class='track_name' and .=" + XPath.to_literal(name) +
            "][1]/following-sibling::div/div[@class='icons playedontriplej'][1]").extract_first()

        return played is not None

    @staticmethod
    def played_on_unearthed(response, name):
        played = response.xpath(
            "//div[@class='track_name' and .=" + XPath.to_literal(name) +
            "][1]/following-sibling::div/div[@class='icons unearthed'][1]").extract_first()

        return played is not None

    @staticmethod
    def mature(response, name):
        played = response.xpath(
            "//div[@class='track_name' and .=" + XPath.to_literal(name) +
            "][1]/following-sibling::div/div[@class='icons mature'][1]").extract_first()

        return played is not None

    def get_tracks(self, response):
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
            played_on_jjj=self.played_on_jjj(response, name),
            played_on_unearthed=self.played_on_unearthed(response, name),
            mature=self.mature(response, name),
            shares=track_shares[i]) for i, name in enumerate(track_names)]

        for track in tracks:
            track["reviews"] = list(self.get_reviews(response, track["name"]))

        return tracks

    def get_reviews(self, response, track_name):
        review_tracks = response.css("h4.track ::text").extract()
        review_reviewers = response.css("a.reviewer_name ::text").extract()
        review_dates = response.css("p.review_date ::text").extract()
        review_ratings = response.css("div.stars ::text").extract()

        for i, review_track in enumerate(review_tracks):
            if review_track.strip() == track_name.strip():
                yield Items.Review(
                    reviewer=review_reviewers[i].strip(),
                    date=review_dates[i].strip(),
                    rating=self.to_rating(review_ratings[i].strip()))

    def parse(self, response):
        yield self.get_artists(response)
        nextpages = response.xpath("//p/a[contains(@href, '/artist/')]/@href").extract()

        for nextpage in nextpages:
            next_page = nextpage
            if next_page:
                yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
