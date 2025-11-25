import pandas as pd

df = pd.read_csv("titanic.csv")

# cleaning-dataset
df = df.drop_duplicates()
df = df.fillna("None")

# print(df.to_string())

# Overall survival rate
survival = df["Survived"].mean()
print("Overall survival rate:", survival)

# Survival rate by sex
survival_by_sex = df.groupby("Sex")["Survived"].mean()
print("\nSurvival rate by sex:")
print(survival_by_sex)
