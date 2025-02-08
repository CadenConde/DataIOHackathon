import plotly.express as px
import pandas as pd

# Load your dataset
df = pd.read_csv("datasets/co2_emissions_kt_by_country.csv")

# Check the first few rows to ensure it's loaded correctly
print(df.head())

# Get the min and max values of emissions for proper scaling
min_value = df["value"].min()
max_value = df["value"].max()

# Create choropleth map with custom color scale and thresholds
fig = px.choropleth(
    df,
    locations="country_code",  # Use the country_code (ISO-3 codes)
    color="value",  # The emissions value
    hover_name="country_name",  # Hover to show the full country name
    animation_frame="year",  # Animate over the years
    color_continuous_scale="Reds",  # Choose the color scale
    title="Yearly Carbon Emissions by Country",
    labels={"value": "CO2 Emissions (kt)", "year": "Year"},
    locationmode="ISO-3",  # Use ISO-3 country codes for locations
    range_color=[min_value, 3_000_000],  # Set the range for color mapping
)

# Show the plot
fig.show()