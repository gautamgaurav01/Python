import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")


sns.set_style("whitegrid")
sns.lineplot(
    data=penguins,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="island",
    style="sex"
)

plt.title("Body Mass vs Flipper Length (Penguins Dataset)")
plt.show()
