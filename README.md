# Triple J Unearthed Stats

A statistical analysis of every artist on Triple J Unearthed.

## Statistic Cruncher
- [CrunchStats.py](CrunchStats.py)

Parses all the artists in [artists.json](data/artists.json) and spits out the stats as json files into the [docs/data](docs/data) (to generate the charts) and [docs/_data](docs/_data) (to be read server side from [Jekyll](https://jekyllrb.com/docs/datafiles/)).

## Charts
- [Google Charts](https://developers.google.com/chart/) are generated using [Unobtrusive Google Charts](https://github.com/craigles/unobtrusive-google-charts)

## Schema
```
{
  "influences": "Red Hot Chili Peppers, Infectious Grooves, Fishbone, Mr Bungle, Rage Against the Machine, Faith No More, Helmet, Brown Hornet, Primus, Incubus",
  "_type": "Artist",
  "name": "Twitch",
  "links": [
    "https://www.facebook.com/twitchbandadelaide",
    "https://twitter.com/twitchband"
  ],
  "tags": [
    "# Alternative #Groove #jams #funk"
  ],
  "url": "https://www.triplejunearthed.com/artist/twitch-0",
  "tracks": [
    {
      "played_on_unearthed": false,
      "plays": 192,
      "loves": 3,
      "avg_rating": 4,
      "played_on_jjj": false,
      "shares": 8,
      "reviews": [
        {
          "date": "2017-04-01",
          "rating": 3.5,
          "reviewer": "Valley FM 89.5"
        },
        {
          "date": "2015-07-25",
          "rating": 5,
          "reviewer": "Rusty Freer"
        },
        {
          "date": "2015-07-22",
          "rating": 5,
          "reviewer": "ian millsy"
        }
      ],
      "number_of_reviews": 4,
      "link": "https://www.triplejunearthed.com/download/track/4280771",
      "mature": true,
      "date": "2015-07-16",
      "downloads": 46,
      "name": "Boomstick"
    }
  ],
  "likes": [
    {
      "url": "https://www.triplejunearthed.com/artist/pimpin-horus",
      "name": "Pimpin' Horus"
    },
    {
      "url": "https://www.triplejunearthed.com/artist/silent-duck",
      "name": "Silent Duck"
    },
    {
      "url": "https://www.triplejunearthed.com/artist/tony-font-show",
      "name": "Tony Font Show"
    }
  ],
  "members": "Andy - vocals\r\nTom - drums\r\nMat - bass\r\nSi - guitar",
  "genre": [
    "Rock"
  ],
  "location": "Adelaide, SA"
}
```
