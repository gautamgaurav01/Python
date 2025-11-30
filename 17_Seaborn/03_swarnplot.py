import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# Create a swarmplot to visualize body mass distribution across species
# hue="island" separates points by island using different colors
# dodge=True keeps hue groups separated within each species category
# palette="Set1" applies a predefined color scheme


sns.swarmplot(
    data=penguins,
    x="species",
    y="body_mass_g",
    hue="island",
    palette="Set1",
    dodge=True,
)

plt.title("Body Mass by Species and Island (Penguins Dataset)")

plt.show()
