import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")
print(titanic["Pclass"].value_counts())
print(titanic.groupby("Pclass")["Pclass"].count())

