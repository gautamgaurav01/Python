
import matplotlib.pyplot as plt
import numpy as np

#Histogram = A visual representation of the distribution of quantitative data.
#            They group values into bins (intervals) 
#            and counts how many fall in each range.

scores=np.random.normal(loc=80 , scale=10 , size=100)
scores= np.clip(scores, 0 , 100)

plt.hist(scores,
         bins=10, # how many bins 
         color="green",
         edgecolor="black") # make histrogram

plt.title("Exam Scores", fontsize=20,
          family="Arial",
          fontweight="bold",
          color="#2d4cfc")

plt.xlabel("Scores", fontsize=14)
plt.ylabel("No of Students", fontsize=14)

plt.show() # show 