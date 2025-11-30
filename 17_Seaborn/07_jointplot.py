import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# Create a joint plot of body mass vs flipper length
jp = sns.jointplot(
    data=penguins,
    x="flipper_length_mm",
    y="body_mass_g",
    kind="scatter",   # default is scatter; you can also use 'reg' for regression
    hue="sex",
    palette="Set2"
)

plt.show()
