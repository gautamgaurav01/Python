"""A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional
array, or a table with rows and columns."""

import pandas as pd

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
# load data into a DataFrame object:
df = pd.DataFrame(data)
print(df, "\n")
# use a list of indexes:
print(df.loc[[0, 1]], "\n")


""" #Named Indexes """
import pandas as pd

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df, "\n")


# Locate Named Indexes
# refer to the named index:
print(df.loc["day2"], "\n")

print(df.head(2), "\n")

print(df.describe())


#
import pandas as pd

data = {"calories": [420, 380, 390], "duration": [30, 40, 45]}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df[(df["calories"] > 380) & (df["duration"] > 40)])
df.loc["day2", "calories"] = 30
print(df)


import pandas as pd

data = {"Name": ["Gaurav", "Sandesh"], "Age": [20, 21]}
df = pd.DataFrame(data, index=["Student-1", "Student-2"])
df["Work"] = ["Python", "Js"]
df.loc["Student-3"] = ["Puskar", 19, "HTML"]
print(df)
print(df.info())
