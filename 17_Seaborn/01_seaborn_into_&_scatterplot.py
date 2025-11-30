"""
Seaborn is a Python library built on top of Matplotlib that focuses on statistical data
visualization. It provides high-level functions, built-in themes, and automatic handling
of datasets, allowing users to create informative and visually appealing plots with
minimal code. Seaborn is widely used for exploring trends, relationships, and distributions
in data.
"""

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set the visual style before creating any plots
sns.set_style("dark")

# 1. Display the list of available built-in Seaborn datasets
datasets = sns.get_dataset_names()
print(datasets)

# 2. Load the Penguims dataset and preview the first few rows
penguins = sns.load_dataset("penguins")
print(penguins.head())

# 3. Display the count of each species in the dataset
print(penguins["species"].value_counts())

# 4. Create a scatter plot showing flipper length vs body mass, colored by island
sns.scatterplot(
    data=penguins,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="island",
    palette="Set1"
)


# sns.scatterplot(
#     data=penguins,
#     x="species",
#     y="body_mass_g",
#     hue="island",
#     style="sex" ,
#     palette="Set1"
# )

# Remove the top and right spines for a cleaner visual appearance
sns.despine()

# Adjust context for clearer text and labels in notebook environments
sns.set_context("notebook")

# 5. Display the plot with a title
plt.title("Flipper Length vs Body Mass (Penguins Dataset)")
plt.show()
