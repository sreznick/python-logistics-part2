import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality_long.csv", index_col="date.utc", parse_dates=True)
no2 = air_quality[air_quality["parameter"] == "no2"]
no2_subset = no2.sort_index().groupby(["location"]).head(2)
print(no2_subset.pivot(columns="location", values="value"))

