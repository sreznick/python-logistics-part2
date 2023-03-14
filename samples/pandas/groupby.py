import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")
print(titanic[["Sex", "Age"]].groupby("Sex").mean())
print(titanic.groupby("Sex").mean(numeric_only=True))
print(titanic.groupby("Sex")["Age"].mean())
print(titanic.groupby(["Sex", "Pclass"])["Fare"].mean())

