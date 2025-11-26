import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([10, 18, 28, 35])

style = {
    "marker": "*",
    "markersize": 30,
    "markerfacecolor": "cyan",
    "markeredgecolor": "#1cd3fc",
    "linestyle": "dotted",
    "linewidth": 2,
    "color": "red"
}

plt.title("Class Size", fontsize=20,
          family="Arial",
          fontweight="bold",
          color="#2d4cfc")

plt.xlabel("Year", fontsize=14)
plt.ylabel("Student Count", fontsize=14)

plt.tick_params(axis="both",
                colors="#2d4cfc")

plt.plot(x, y1, **style)
plt.plot(x, y2, **style)
plt.xticks(x) # returns (locations, labels)
plt.show()
