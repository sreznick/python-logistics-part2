import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality_no2_long.csv", parse_dates=["date.utc"])
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
no_2 = air_quality.pivot(index="datetime", columns="location", values="value")
print(no_2.index.year)
print(no_2.index.weekday)
