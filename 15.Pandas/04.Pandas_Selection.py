#
import pandas as pd


# Selection by Coloumn

# df = pd.read_csv("data.csv")
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df[["Name" , "Height" , "Weight"]].to_string())


# Selection by Row

# df = pd.read_csv("data.csv", index_col="Name")
# print(df)
# print(df.loc["Pikachu"])
# print(df.loc["Pikachu",["Height" , "Weight"]])
# print(df.loc["Pikachu":"Nidorina" , ["Height" , "Weight"]])
# print(df.iloc[0:11:2 , 0:3])


# Searching

df = pd.read_csv("data.csv", index_col="Name")
pokemon = input("Enter a Pokemon Name: ")

try:
    print(df.loc[pokemon])

except KeyError:
    print(pokemon, "not found")
