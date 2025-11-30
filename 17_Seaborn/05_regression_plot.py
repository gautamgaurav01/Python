import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# Create a regression plot of body mass vs flipper length
sns.regplot(
    data=penguins,
    x="flipper_length_mm",
    y="body_mass_g"
)

plt.title("Body Mass vs Flipper Length (Penguins Dataset)")
plt.show()
