# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
max_temp = max(weatherdata, key=lambda x: x['tmax'])
print(f"Dia mais quente: {max_temp['date']}")

# TODO: What was the coldest day in the data set?
min_temp = min(weatherdata, key=lambda x: x['tmin'])
print(f"Dia mais frio: {min_temp['date']}")

# TODO: How many days had snowfall?
nevou = [day for day in weatherdata if day['snow']>0]
print(f"Nevou {len(nevou)} dias")
