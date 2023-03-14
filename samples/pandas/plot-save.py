import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
fig.savefig("no2_concentrations.png")
plt.show()

