import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality_long.csv", index_col="date.utc", parse_dates=True)
print(air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
))
print(air_quality.pivot_table(
    values="value",
    index="location",
    columns="parameter",
    aggfunc="mean",
    margins=True,
))

