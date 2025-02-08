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


df = df[['CO2 Emissions(g/km)', 'Fuel Consumption Comb (mpg)', 'Vehicle Class','Engine Size(L)','Cylinders','Transmission','Fuel Type','Displacement per Cylinder']]

x = list(set(df["Transmission"].values.tolist()))
for i in x:
    print(i)

