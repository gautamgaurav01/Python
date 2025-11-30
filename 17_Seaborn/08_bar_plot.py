import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# Bar plot of total body mass by species and sex
sns.barplot(
    data=penguins,
    x="species",
    y="body_mass_g",
    hue="sex",
    estimator=np.median,
    palette="Set2"
)

plt.title("Total Body Mass by Species and Sex (Penguins Dataset)")
plt.show()
