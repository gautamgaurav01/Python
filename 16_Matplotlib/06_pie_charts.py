
import matplotlib.pyplot as plt
import numpy as np

#Bar chart= Circular chart divided into slices to show percentages of the total.
#           Good for visualizing distribution among categories.

categories = ["Grains", "Vegetables", "Fruits", "Sweets", "Proteins"]
values = [190, 250, 150, 140, 307]

colors = ["#ff9999","#66b3ff","#99ff99","#ffcc99","#c2c2f0"]  # Optional: different colors for slices

plt.pie(values, 
        labels=categories, 
        colors=colors, 
        autopct='%1.1f%%',   # limit percentage point
        explode=[0,0,0,0,0.2], # explode part
        shadow=True,  # give shadow
        startangle=44)  # rotate angle 
        
plt.title("Daily Consumption", 
          fontsize=20, 
          family="Arial", 
          fontweight="bold", 
          color="#2d4cfc")

plt.axis('equal')  # Equal aspect ratio ensures pie is circular
plt.show()