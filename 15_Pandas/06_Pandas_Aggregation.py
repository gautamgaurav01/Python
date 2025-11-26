import pandas as pd

""" 
-------------aggregate functions-------------
Reduces a set of values into a single summary value
Used to summarize and analyze data
Often used with the groupby() function
"""

df = pd.read_csv("data.csv")


# Whole Data Frame

# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())


# Single Column

# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())


# with the groupby()

# group=df.groupby("Type1")
# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())
# print(group["Height"].count())
