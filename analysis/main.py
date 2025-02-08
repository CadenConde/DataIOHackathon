import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

plt.style.use('dark_background')
# Load dataset
df = pd.read_csv('car_price_prediction.csv').head(1000)

# Check basic info and summary
print(df.head())
df.info()
df.describe()

# Data visualization
sns.pairplot(df)

plt.subplots_adjust(bottom=0.1)
plt.show()
