from datetime import datetime

date_format = "%Y-%m-%d"


def parse(date):
    return datetime.strptime(date, date_format)


def now():
    return datetime.strftime(datetime.now(), date_format)
