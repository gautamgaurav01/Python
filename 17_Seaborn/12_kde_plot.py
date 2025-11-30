import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# KDE plot of body mass by sex
# KDE (Kernel Density Estimate) plot shows a smooth estimate of the probability density 
# of a continuous variable. It helps visualize the distribution and compare groups.
sns.kdeplot(
    data=penguins,
    x="body_mass_g",
    hue="sex",
    fill=True,          # fills the area under the curve
    palette="Set2",
    common_norm=False   # normalize each distribution separately
)

plt.title("KDE of Body Mass by Sex (Penguins Dataset)")
plt.show()
