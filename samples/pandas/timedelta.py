import pandas as pd

air_quality = pd.read_csv("air_quality_no2_long.csv", parse_dates=["date.utc"])
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
print(air_quality["datetime"].min())
print(air_quality["datetime"].max())
print(air_quality["datetime"].max() - air_quality["datetime"].min())

