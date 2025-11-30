import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# Box plot of body mass by species and sex
sns.boxplot(
    data=penguins,
    x="species",
    y="body_mass_g",
    hue="sex",
    palette="Set2"
)

plt.title("Body Mass Distribution by Species and Sex (Penguins Dataset)")
plt.show()
