"""
A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

In our examples we will be using a CSV file called 'data.csv'.
"""

import pandas as pd
df = pd.read_csv("data.csv")
print(df.to_string()) 
print(df)

import pandas as pd
print(pd.options.display.max_rows)  


#

import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df) 