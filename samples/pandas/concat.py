import pandas as pd

df = pd.DataFrame(
        {
            "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
            ],
            "Age": [22, 35, 58],
            "Sex": ["male", "male", "female"],
        }
)

df2 = pd.concat([df, pd.DataFrame({'Name':['Jane'], 'Age':[25], 'Location':['Madrid']})])
df3 = pd.concat([df, df, df2])


print(df)
print(df2)
print(df3)

