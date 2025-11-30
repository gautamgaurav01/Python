import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# Create a histogram to visualize body mass distribution across sex
sns.histplot(
    data=penguins,
    x="body_mass_g",
    hue="sex",
    multiple="stack",  # stack bars for different sexes
    palette="Set2"
)

plt.title("Body Mass Distribution by Sex (Penguins Dataset)")
plt.show()
