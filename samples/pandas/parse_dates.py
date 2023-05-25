
import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality_no2_long.csv", parse_dates=["date.utc"])
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
print(air_quality["datetime"])

