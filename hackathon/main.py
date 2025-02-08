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

# plt.style.use('dark_background')
# pd.set_option('display.max_columns', None)  # Show all columns
# pd.set_option('display.width', 1000)  # Adjust the width to prevent wrapping
#
# df = pd.read_csv('data/CO2 Emissions_Canada.csv', encoding='latin-1')
#
# df['Displacement per Cylinder'] = df['Engine Size(L)'] / df['Cylinders']
# print(df)
#
#
# df = df[['CO2 Emissions(g/km)', 'Fuel Consumption Comb (mpg)', 'Vehicle Class','Engine Size(L)','Cylinders','Transmission','Fuel Type','Displacement per Cylinder']]
# print(df.head())
# df.info()
# df.describe()
#
#
# # Columns to use
# y_column = ['CO2 Emissions(g/km)', 'Fuel Consumption Comb (mpg)']
# x_columns = ['Vehicle Class','Engine Size(L)','Cylinders','Transmission','Fuel Type', 'Displacement per Cylinder']
#
# X = df[x_columns]
# y1 = df['Fuel Consumption Comb (mpg)']
# y2 = df['CO2 Emissions(g/km)']
#
# # Preprocess categorical and numerical features
# numerical_features = ['Engine Size(L)', 'Cylinders', 'Displacement per Cylinder']
# categorical_features = ['Transmission', 'Fuel Type', 'Vehicle Class']
#
# # Create column transformer to apply different transformations for categorical and numerical data
# preprocessor = ColumnTransformer(
#     transformers=[
#         ('num', StandardScaler(), numerical_features),
#         ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)  # Handle unseen categories in categorical features
#     ])
#
# # Split data into training and test sets
# X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y1, test_size=0.2, random_state=42)
# X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y2, test_size=0.2, random_state=42)
#
# # Create a pipeline that first applies preprocessing, then fits a RandomForestRegressor model
# model1 = Pipeline(steps=[
#     ('preprocessor', preprocessor),
#     ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
# ])
# model2 = Pipeline(steps=[
#     ('preprocessor', preprocessor),
#     ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
# ])
#
# # Train the model
# model1.fit(X_train1, y_train1)
#
# y_pred1 = model1.predict(X_test1)
# df.loc[X_test1.index, 'Predicted'] = y_pred1
# df['Emissions_Type'] = np.where(df['Predicted'].notna(), 'Predicted', 'Actual')
#
# model2.fit(X_train2, y_train2)
#
# y_pred2 = model2.predict(X_test2)
# df.loc[X_test2.index, 'Predicted'] = y_pred2
# df['Emissions_Type'] = np.where(df['Predicted'].notna(), 'Predicted', 'Actual')
#
# # Calculate the mean squared error
# mse1 = mean_squared_error(y_test1, y_pred1)
# rmse1 = mse1 ** 0.5
#
# target_range1 = np.max(y_test1) - np.min(y_pred1)
# p1 = (1.0 - (rmse1 / target_range1)) * 100
#
# mse2 = mean_squared_error(y_test1, y_pred1)
# rmse2 = mse2 ** 0.5
#
# target_range2 = np.max(y_test1) - np.min(y_pred1)
# p2 = (1.0 - (rmse2 / target_range2)) * 100
#
# print(f"Predicted Emissions: {y_pred1}")
# print(f"Root Mean Squared Error for Emissions: {p1:.2f}%")
#
# print(f"Predicted MPG: {y_pred2}")
# print(f"Root Mean Squared Error for MPG: {p2:.2f}%")
#
#
# print(df.head())
# def test1(data):
#     return model1.predict(pd.DataFrame([data], columns=x_columns))
#
# def test2(data):
#     return model2.predict(pd.DataFrame([data], columns=x_columns))
#
# testData=["TWO-SEATER", 6.6, 6, "M7", "N", .5]
# print(test1(testData))
# print(test2(testData))
#
# aa = 4
# plt.figure(figsize=(22*aa, 5*aa))
# pairplot = sns.pairplot(df, y_vars=y_column, x_vars=x_columns, hue='Emissions_Type', palette={'Actual': 'blue', 'Predicted': 'red'})
# plt.subplots_adjust(bottom=0.3)
#
# for ax in pairplot.axes.flatten():
#     # Rotate x-axis labels
#     for label in ax.get_xticklabels():
#         label.set_rotation(75)
#         label.set_fontsize(6)
#
# plt.savefig('pairplot.png', format='png', dpi=300)
# plt.show()
#
#



def setup():
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
    X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y1, test_size=0.2, random_state=42)
    X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y2, test_size=0.2, random_state=42)

# Create a pipeline that first applies preprocessing, then fits a RandomForestRegressor model
    model1 = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    model2 = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

# Train the model
    model1.fit(X_train1, y_train1)

    y_pred1 = model1.predict(X_test1)
    df.loc[X_test1.index, 'Predicted'] = y_pred1
    df['Emissions_Type'] = np.where(df['Predicted'].notna(), 'Predicted', 'Actual')

    model2.fit(X_train2, y_train2)

    y_pred2 = model2.predict(X_test2)
    df.loc[X_test2.index, 'Predicted'] = y_pred2
    df['Emissions_Type'] = np.where(df['Predicted'].notna(), 'Predicted', 'Actual')

# Calculate the mean squared error
    mse1 = mean_squared_error(y_test1, y_pred1)
    rmse1 = mse1 ** 0.5

    target_range1 = np.max(y_test1) - np.min(y_pred1)
    p1 = (1.0 - (rmse1 / target_range1)) * 100

    mse2 = mean_squared_error(y_test2, y_pred2)
    rmse2 = mse2 ** 0.5

    target_range2 = np.max(y_test2) - np.min(y_pred2)
    p2 = (1.0 - (rmse2 / target_range2)) * 100

    print(f"Predicted Emissions: {y_pred1}")
    print(f"Root Mean Squared Error for Emissions: {p1:.2f}%")

    print(f"Predicted MPG: {y_pred2}")
    print(f"Root Mean Squared Error for MPG: {p2:.2f}%")


    print(df.head())
    def test1(data):
        return model1.predict(pd.DataFrame([data+[data[1]/data[2]]], columns=x_columns))

    def test2(data):
        return model1.predict(pd.DataFrame([data+[data[1]/data[2]]], columns=x_columns))

    return (test1, test2)
