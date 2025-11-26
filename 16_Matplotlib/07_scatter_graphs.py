
import matplotlib.pyplot as plt
import numpy as np

#scatter graph -Shows the relationship between two variables 
#              Helps to identify a correlation (+,-,None) 
#              Example: Study hours vs. Test scores

x1=np.array([0,1,2,3,4,5,6,7,7,8]) #Hours studies
y1=np.array([55,60,65,62,68,70,75,78,82,85])  # Grades

x2=np.array([0,2,2,8,9,4,3]) #Hours studies
y2=np.array([55,40,35,22,18,67,70])  # Grades

plt.scatter(x1,y1, color="skyblue",
                alpha=0.5, # dot opacity
                s=200,  # dot size 
                label="Class A")   

plt.scatter(x2,y2, color="red",
                alpha=0.5,  # dot opacity
                s=200,  # dot size 
                label="Class B")    

plt.title("Hours Studies & Grades", fontsize=20,
          family="Arial",
          fontweight="bold",
          color="#2d4cfc")

plt.xlabel("Hours Studies", fontsize=14)
plt.ylabel("Grades", fontsize=14)
plt.legend() # show label of data
plt.show()  # show graph