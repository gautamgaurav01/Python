import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# Create a stripplot to visualize body mass distribution across species
# hue="island" separates points by island using different colors
# jitter=True spreads overlapping points for better visibility
# dodge=True keeps hue groups separated within each species category
# palette="Set1" applies a predefined color scheme
sns.stripplot(
    data=penguins,
    x="species",
    y="body_mass_g",
    hue="island",
    palette="Set1",
    jitter=True,
    dodge=True
)

plt.title("Body Mass by Species and Island (Penguins Dataset)")

plt.show()
