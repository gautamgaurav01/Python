import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# Violin plot of body mass by species and sex
sns.violinplot(
    data=penguins,
    x="species",
    y="body_mass_g",
    hue="sex",
    palette="Set2",
    split=True  # optional: splits violin by hue for comparison
)
#width of violen = density of data
#middle line = median
#thick bar = interquartile range(if inner='box')
plt.title("Body Mass Distribution by Species and Sex (Penguins Dataset)")
plt.show()
