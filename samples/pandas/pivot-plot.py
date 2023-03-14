import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality_long.csv", index_col="date.utc", parse_dates=True)
no2 = air_quality[air_quality["parameter"] == "no2"]
no2.pivot(columns="location", values="value").plot()
plt.show()

