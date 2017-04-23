import json


class LocationPopulations:
    def __init__(self):
        self.locationPopulationsJson = json.loads(open("data/locationPopulations.json").read())

    def per_capita(self, location, number):
        population = self.population(location)

        if population is None:
            return None

        return round(number / population * 100000)

    def population(self, location):
        for l in self.locationPopulationsJson:
            if l.get("location") == location:
                return l.get("population")

        return None
