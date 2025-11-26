
import matplotlib.pyplot as plt
import numpy as np

# Figure = The entire canvas
# Ax = Individual subplots (axes)

x= np.array([1,2,3,4,5])

figures, axes = plt.subplots(2, 2)  # 2 rows, 2 columns of subplots

# Example: plot something on each subplot
axes[0, 0].plot(x,x*2 , color="red")
axes[0, 0].set_title("x*2")

axes[0, 1].plot(x,x**2 , color="green")
axes[0, 1].set_title("x**2")

axes[1, 0].plot(x,x**3 , color="yellow")
axes[1, 0].set_title("x**3")

axes[1, 1].plot(x,x**4 , color="blue")
axes[1, 1].set_title("x**4")

plt.tight_layout()  # adjusts spacing so titles/labels don't overlap
plt.show()
