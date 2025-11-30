import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

penguins = sns.load_dataset("penguins")

# Create a pivot table: average body mass for each species and sex
pivot = penguins.pivot_table(
    index="species",
    columns="sex",
    values="body_mass_g",
    aggfunc=np.mean
)

# Heatmap of average body mass
sns.heatmap(
    pivot,
    annot=True,      # show values on the heatmap
    cmap="YlGnBu",
    fmt=".1f"
)

plt.title("Average Body Mass by Species and Sex (Penguins Dataset)")
plt.xlabel("Sex")
plt.ylabel("Species")
plt.show()
