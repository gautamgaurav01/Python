import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# count plot 
sns.countplot(
    data=penguins,
    x="species",
    hue="sex"
)

plt.show()
