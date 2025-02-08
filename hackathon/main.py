import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

plt.style.use('dark_background')
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', 1000)  # Adjust the width to prevent wrapping

df = pd.read_csv('data/CO2 Emissions_Canada.csv', encoding='latin-1')

df['Displacement per Cylinder'] = df['Engine Size(L)'] / df['Cylinders']
print(df)


df = df[['CO2 Emissions(g/km)', 'Fuel Consumption Comb (mpg)', 'Vehicle Class','Engine Size(L)','Cylinders','Transmission','Fuel Type','Displacement per Cylinder']]
print(df.head())
df.info()
df.describe()


# Columns to use
y_column = ['CO2 Emissions(g/km)', 'Fuel Consumption Comb (mpg)']
x_columns = ['Vehicle Class','Engine Size(L)','Cylinders','Transmission','Fuel Type', 'Displacement per Cylinder']

X = df[x_columns]
y1 = df['Fuel Consumption Comb (mpg)']
y2 = df['CO2 Emissions(g/km)']

# Preprocess categorical and numerical features
numerical_features = ['Engine Size(L)', 'Cylinders', 'Displacement per Cylinder']
categorical_features = ['Transmission', 'Fuel Type', 'Vehicle Class']

# Create column transformer to apply different transformations for categorical and numerical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)  # Handle unseen categories in categorical features
    ])

# Split data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y1, test_size=0.2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y2, test_size=0.2, random_state=42)

# Create a pipeline that first applies preprocessing, then fits a RandomForestRegressor model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train the model
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
df.loc[X_test.index, 'Predicted'] = y_pred
df['Emissions_Type'] = np.where(df['Predicted'].notna(), 'Predicted', 'Actual')

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

target_range = np.max(y_test) - np.min(y_pred)
p = (1.0 - (rmse / target_range)) * 100
print(f"Predicted Emissions: {y_pred}")
print(f"Root Mean Squared Error: {p:.2f}%")


print(df.head())
def test(data):
    return model.predict(pd.DataFrame([data], columns=x_columns))

print(test(["TWO-SEATER", 12.6, 12, "M7", "N", .5]))

pairplot = sns.pairplot(df, y_vars=["CO2 Emissions(g/km)"], x_vars=x_columns, hue='Emissions_Type', palette={'Actual': 'blue', 'Predicted': 'red'})

for ax in pairplot.axes.flatten():
    # Rotate x-axis labels
    for label in ax.get_xticklabels():
        label.set_rotation(75)
        label.set_fontsize(6)

plt.show()


