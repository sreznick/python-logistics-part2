import pandas as pd

titanic = pd.read_csv("titanic.csv")
print(titanic["Name"].str.lower())
print(titanic["Name"].str.split(","))
print(titanic["Name"].str.contains("Countess"))

