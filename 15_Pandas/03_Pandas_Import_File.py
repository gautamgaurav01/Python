"""
A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

In our examples we will be using a CSV file called 'data.csv'.
"""

import pandas as pd

df = pd.read_csv("data.csv")
# print(df)
print(df.to_string())


"""
Big data sets are often stored, or extracted as JSON.

JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

In our examples we will be using a JSON file called 'data.json'.
"""
#
import pandas as pd

df = pd.read_json("data.json")

print(df.to_string())
