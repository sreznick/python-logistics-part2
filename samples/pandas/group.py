import pandas as pd

air_quality = pd.read_csv("air_quality_no2_long.csv", parse_dates=["date.utc"])
air_quality = air_quality.rename(columns={"date.utc": "datetime"})

result = air_quality.groupby(
    [air_quality["datetime"].dt.weekday, "location"])["value"].mean()
print(result)
