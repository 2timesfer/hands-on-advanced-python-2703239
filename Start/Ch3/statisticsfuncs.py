# Example file for Advanced Python: Hands On by Joe Marini
# Using the statistics package

import json
import statistics

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# select the days from the summer months from all the years
summers = ["-06-","-07-","-08-"]
summer_months = [d for d in weatherdata if any([month in d['date'] for month in summers])]
print(f"Data for {len(summer_months)} summer days")

# TODO: calculate the mean for both min and max temperatures
maxt = [d['tmax'] for d in summer_months]
mint = [d['tmin'] for d in summer_months]
print(max_mean := statistics.mean(maxt))
print(min_mean := statistics.mean(mint))


# TODO: calculate the median values for min and max temperatures
print(statistics.median(maxt))
print(statistics.median(mint))

# TODO: use the standard deviation function to find outlier temperatures
upper_outlier = max_mean + (statistics.stdev(maxt)*2)
lower_outlier = min_mean - (statistics.stdev(mint)*2)
print(upper_outlier)
print(lower_outlier)

max_outliers = [t for t in maxt if t>=upper_outlier]
min_outliers = [t for t in mint if t<=lower_outlier]
print(max_outliers)
print(min_outliers)
