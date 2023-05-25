import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality_no2_long.csv", parse_dates=["date.utc"])
air_quality = air_quality.rename(columns={"date.utc": "datetime"})

fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(
    kind='bar', rot=0, ax=axs
)
plt.xlabel("Hour of the day");  # custom x label using Matplotlib
plt.ylabel("$NO_2 (mg/m^3)$");
plt.show()

