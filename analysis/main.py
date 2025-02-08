import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

plt.style.use('dark_background')
# Load dataset
df = pd.read_csv('car_price_prediction.csv').head(1000)

# Loop through all columns and convert string columns to categorical integer codes
for col in df.select_dtypes(include=['object']).columns:
    df[col] = pd.Categorical(df[col]).codes

# Check basic info and summary
print(df.head())
df.info()
df.describe()

# Data visualization
# sns.pairplot(df)
# plt.show()
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

x = df["Cylinders"]
y = df["Engine volume"]
plt.plot(x, y, 'x')
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
def y(x): return slope * x + intercept
plt.plot(x, y(x), color='red', label='Regression line')  # Plot regression line

plt.subplots_adjust(bottom=0.2)
plt.show()
