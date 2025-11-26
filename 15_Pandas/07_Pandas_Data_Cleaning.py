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

# df= df.dropna(sunset= ["Type2"])
# df= df.fillna({"Type2" : "None"})


# Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Fire": "FIRE"})


# 4. Standardize text
# df["Name"]= df["Name"].str.lower()


# 5. Fix data types
# df["Legendary"] = df["Legendary"].astype(bool)


# 6. Remove duplicate values
df = df.drop_duplicates()
print(df.to_sting())
