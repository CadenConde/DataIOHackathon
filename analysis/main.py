import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Load dataset
df = pd.read_csv('data.csv')

# Check basic info and summary
df.info()
df.describe()

# Data visualization
sns.histplot(df['Model'], kde=True)
plt.xticks(rotation=45, fontsize=5)
plt.show()

# Correlation heatmap
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# Grouping and aggregation
# grouped_data = df.groupby('category_column')['numeric_column'].mean()

# Statistical test
t_stat, p_val = stats.ttest_ind(df['group1'], df['group2'])
print(f"T-statistic: {t_stat}, P-value: {p_val}")
