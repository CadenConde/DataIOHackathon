import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

plt.style.use('dark_background')

# make the bullshit fit
plt.subplots_adjust(bottom=0.4, left=0.2)


# df = pd.read_csv('data/1. Cement_emissions.csv', encoding='latin-1')
df = pd.read_csv('data/global air pollution dataset.csv', encoding='latin-1')

# Loop through all columns and convert string columns to categorical integer codes
for col in df.select_dtypes(include=['object']).columns:
    df[col] = pd.Categorical(df[col]).codes

print(df.head())
df.info()
df.describe()

# Data visualization
sns.pairplot(df)
# plt.show()

plt.title("global air pollution dataset")
# sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# x = df["Cylinders"]
# y = df["Engine volume"]
# plt.plot(x, y, 'x')
# slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
# def y(x): return slope * x + intercept
# plt.plot(x, y(x), color='red', label='Regression line')  # Plot regression line
#
# plt.show()
#
