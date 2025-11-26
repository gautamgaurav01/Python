import pandas as pd

df = pd.read_csv("data.csv")

# Filtering = Keep the row that match the condition

# tall_pokemon= df[df["Height"] >= 2]
# print(tall_pokemon)

# heavy_pokemon= df[df["Weight"] >= 100]
# print(heavy_pokemon)

# legendary_pokemon= df[df["Legendary"]==True]
# print(legendary_pokemon)

water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
print(water_pokemon)
