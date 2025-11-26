
import matplotlib.pyplot as plt
import numpy as np

# Bar chart = compare categories of data by representing each category with a bar

categories=np.array(["Grains" , "Vegetables", "Fruits" , "Sweets" , "Proteins"])
values= [4,3,5,6,7]

plt.bar(categories,values , color="green") #create bar chart vertically
#plt.barh(categories,values , color="green") #create bar chart horizontally

plt.title("Daily Consumption", fontsize=20,
          family="Arial",
          fontweight="bold",
          color="#2d4cfc")

plt.xlabel("Categories", fontsize=14)
plt.ylabel("Values", fontsize=14)

plt.tick_params(axis="both",
                colors="#2d4cfc")


plt.show() # show bar chart