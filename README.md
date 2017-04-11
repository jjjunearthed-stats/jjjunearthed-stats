# Triple J Unearthed Stats

A statistical analysis of every artist on Triple J Unearthed.

## Statistic Cruncher
- [CrunchStats.py](CrunchStats.py)

Parses all the artists in [artists.json](artists.json) and spits out the stats as json files into the [docs/data](docs/data) (to generate the charts) and [docs/_data](docs/_data) (to be read server side from [Jekyll](https://jekyllrb.com/docs/datafiles/)).

## Charts
- [charts.js](docs/scripts/charts.js)

Generates graphs using [Google Charts](https://developers.google.com/chart/).
