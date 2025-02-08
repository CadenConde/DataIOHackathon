import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

plt.style.use('dark_background')

# make the bullshit fit
plt.subplots_adjust(bottom=0.4, left=0.2)

df_cement = pd.read_csv('hackathon/data/1. Cement_emissions.csv', encoding='latin-1')
df_airpol = pd.read_csv('hackathon/data/global air pollution dataset.csv', encoding='latin-1')
df_canada = pd.read_csv('hackathon/data/CO2 Emissions_Canada.csv', encoding='latin-1')

df_airpol = df_airpol.drop(columns=['NO2 AQI Category'], errors='ignore')

cement_constant_columns = [
    'Andorra', 'Anguilla', 'Antigua and Barbuda', 'Aruba', 'Belize', 'Bermuda', 
    'Bonaire, Saint Eustatius and Saba', 'British Virgin Islands', 'Brunei Darussalam', 
    'Central African Republic', 'Comoros', 'Cook Islands', "Côte d'Ivoire", 'Curaçao', 
    'Dominica', 'Equatorial Guinea', 'Faeroe Islands', 'Micronesia (Federated States of)', 
    'French Polynesia', 'Gambia', 'Greenland', 'Grenada', 'Guinea', 'Guinea-Bissau', 
    'Kiribati', 'Lesotho', 'Liechtenstein', 'Maldives', 'Malta', 'Marshall Islands', 
    'Mauritania', 'Mauritius', 'Montenegro', 'Montserrat', 'Nauru', 'Niue', 
    'Occupied Palestinian Territory', 'Palau', 'Papua New Guinea', 'South Sudan', 
    'Saint Helena', 'Saint Lucia', 'Sint Maarten (Dutch part)', 'Samoa', 
    'Sao Tome and Principe', 'Seychelles', 'Sierra Leone', 'Singapore', 'Solomon Islands', 
    'Saint Kitts and Nevis', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 
    'Swaziland', 'Timor-Leste', 'Tonga', 'Turks and Caicos Islands', 'Tuvalu', 
    'Vanuatu', 'Wallis and Futuna Islands'
]

# Remove the erroneous columns from the cement dataframe
df_cement = df_cement.drop(columns=constant_columns)

dfs = [df_cement, df_airpol, df_canada]

# Loop through all columns and convert string columns to categorical integer codes
for df in dfs:
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = pd.Categorical(df[col]).codes

# Display the first few rows to confirm the change
# print(df_airpol.head())
# print(df_canada.head())
print(df_cement.head())

df_canada.info()
df_canada.describe()

# Data visualization
sns.pairplot(df)
# plt.show()

plt.title("global air pollution dataset")
sns.heatmap(df_canada.corr(), annot=True, cmap='coolwarm')
plt.show()

x = df_canada["Cylinders"]
y = df_canada["Engine volume"]
# plt.plot(x, y, 'x')
# slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
# def y(x): return slope * x + intercept
# plt.plot(x, y(x), color='red', label='Regression line')  # Plot regression line
#
# plt.show()
#
