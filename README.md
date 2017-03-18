# Triple J Unearthed Stats

A statistical analysis of the artists on the Triple J Unearthed site.

## Web Scraper
- [JJJUnearthedSpider.py](JJJUnearthed/spiders/JJJUnearthedSpider.py)
- [RunSpider.py](RunSpider.py) (to run the above spider locally)

A web scraper which pulls artist, track and track review data from JJJ's Unearthed site. Uses the [Scrapy](https://scrapy.org) Python web scraping framework. Currently using [Scraping Hub](https://scrapinghub.com/) to run the spider and collect the artist data.

## Statistic Cruncher
- [CrunchStats.py](CrunchStats.py)

Crunches the artists in [artists.json](artists.json) and spits out the stats as json files into the [docs/data](docs/data) and [docs/_data](docs/_data) directories.

## Charts
- [charts.js](docs/scripts/charts.js)

Generates graphs using [Google Charts](https://developers.google.com/chart/).
