import pandas as pd
import matplotlib.pyplot as plt

air_quality_no2 = pd.read_csv("air_quality_no2_long.csv",
                              parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location",
                                   "parameter", "value"]]
air_quality_pm25 = pd.read_csv("air_quality_pm25_long.csv",
                               parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location",
                                     "parameter", "value"]]
stations_coord = pd.read_csv("air_quality_stations.csv")
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
print(air_quality.head())

