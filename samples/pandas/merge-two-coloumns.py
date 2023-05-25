
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
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
air_quality_parameters = pd.read_csv("air_quality_parameters.csv")
air_quality = pd.merge(air_quality, air_quality_parameters,
                       how="left", left_on='parameter', right_on='id')
print(air_quality.head())

