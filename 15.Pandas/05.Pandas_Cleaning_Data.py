"""
Data Cleaning
Data cleaning means fixing bad data in your data set.

Bad data could be:

Empty cells
Data in wrong format
Wrong data
Duplicates
"""

import pandas as pd

df = pd.read_csv("data.csv")
new_df = df.dropna()
print(new_df.to_string(),"\n")
#

df.dropna(inplace = True)
print(df.to_string(),"\n")