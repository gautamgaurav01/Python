import pandas as pd

"""
Data cleanlng =
the process of fixing/removing:
incomplete, incorrect, or irrelevant data.
of work done with Pandas is data cleaning 
"""
df = pd.read_csv("data.csv")

# 1. Drop Irrelevant Columns
# df= df.drop(columns=["Legendary" , "No"])

# Handle Missing Data

print(df)
