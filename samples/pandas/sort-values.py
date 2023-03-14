import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")
print(titanic.sort_values(by="Age").head())
print(titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head())

