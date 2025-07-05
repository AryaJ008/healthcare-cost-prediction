import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (make sure insurance.csv is in the same folder)
df = pd.read_csv("insurance.csv")

# Basic info
print("\nFirst 5 Rows:\n", df.head())
print("\nData Info:\n")
print(df.info())
print("\nStatistics:\n", df.describe())
print("\nMissing Values:\n", df.isnull().sum())
# Visualizations
sns.histplot(df['age'], kde=True)
plt.title("Age Distribution")
plt.show()

sns.boxplot(x='smoker', y='charges', data=df)
plt.title("Charges by Smoking Status")
plt.show()

sns.scatterplot(x='bmi', y='charges', hue='smoker', data=df)
plt.title("BMI vs Charges")
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
