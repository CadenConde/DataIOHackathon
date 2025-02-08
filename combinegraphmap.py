import pandas as pd
import folium
import json
import branca.colormap as cm
import numpy as np
import random
from geopy.geocoders import Nominatim
import chardet
from pathlib import Path

### ---- Load & Process Air Quality Data ---- ###
print("Loading air quality data...")

# Load dataset
aq_file_path = "hackathon/data/global air pollution dataset.csv"
df_aq = pd.read_csv(aq_file_path)

# Randomly select 750 cities
df_sample = df_aq.sample(n=750, random_state=42).copy()

# Initialize geocoder
geolocator = Nominatim(user_agent="geoapi")

# Function to get latitude and longitude
def get_lat_lon(city, country):
    print(random.random())
    try:
        location = geolocator.geocode(f"{city}, {country}")
        if location:
            return location.latitude, location.longitude
    except:
        return None, None

# Add latitude & longitude columns
df_sample[['Latitude', 'Longitude']] = df_sample.apply(
    lambda row: pd.Series(get_lat_lon(row['City'], row['Country'])), axis=1
)

# Drop rows with missing coordinates
df_sample = df_sample.dropna(subset=['Latitude', 'Longitude'])

# Define AQI category colors
aqi_colors = {
    "Good": "green",
    "Moderate": "yellow",
    "Unhealthy for Sensitive Groups": "orange",
    "Unhealthy": "red",
    "Very Unhealthy": "purple",
    "Hazardous": "maroon"
}

### ---- Load & Process CO₂ Emissions Data ---- ###
print("Loading CO₂ emissions data...")

# Detect File Encoding
co2_file_path = "1. Cement_emissions.csv"
with open(co2_file_path, "rb") as f:
    raw_data = f.read(10000)
    detected_encoding = chardet.detect(raw_data)["encoding"]

# Load CO2 dataset
try:
    df_co2 = pd.read_csv(co2_file_path, encoding=detected_encoding)
except UnicodeDecodeError:
    df_co2 = pd.read_csv(co2_file_path, encoding="latin1")  # Fallback encoding

# Load GeoJSON for World Map
geojson_path = Path("./hackathon/data/Externaldata/countries.geo.json").resolve()
with open(geojson_path, "r") as f:
    world_geojson = json.load(f)

# Convert dataset to long format
df_melted = df_co2.melt(id_vars=["Year"], var_name="Country", value_name="CO2_Emissions")
df_melted["Country"] = df_melted["Country"].replace("USA", "United States of America")
df_melted["CO2_Emissions"] = df_melted["CO2_Emissions"].fillna(0)

# Compute Average CO2 Emissions Per Country
df_avg = df_melted.groupby("Country", as_index=False)["CO2_Emissions"].mean()

# Apply Log Transformation for Better Low-End Detail
df_avg["Log_CO2_Emissions"] = np.log1p(df_avg["CO2_Emissions"])

# Define Color Scale for CO2 Emissions
min_log, max_log = df_avg["Log_CO2_Emissions"].min(), df_avg["Log_CO2_Emissions"].max()
co2_color_scale = cm.LinearColormap(
    colors=["white", "lightyellow", "orange", "red", "purple", "#210042"],
    vmin=min_log,
    vmax=max_log,
    caption="Log-scaled CO₂ Emissions (log₁ₚ)"
)

# Create a Country-CO2 Mapping
country_emission_map = df_avg.set_index("Country")["Log_CO2_Emissions"].to_dict()

# Define Style Function for CO2 Emissions Choropleth
def style_function(feature):
    country_name = feature["properties"]["name"]
    emission_log = country_emission_map.get(country_name, 0)
    return {
        "fillColor": co2_color_scale(emission_log),
        "color": "black",
        "weight": 0.5,
        "fillOpacity": 0.7,
    }

### ---- Create Interactive Folium Map ---- ###
print("Creating combined map...")
m = folium.Map(location=[20, 0], zoom_start=2)

# Add CO2 Emissions Choropleth
folium.GeoJson(
    world_geojson,
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["Country"], localize=True)
).add_to(m)

# Add AQI Markers
for _, row in df_sample.iterrows():
    folium.CircleMarker(
        location=(row['Latitude'], row['Longitude']),
        radius=5,
        color=aqi_colors.get(row['AQI Category'], "gray"),
        fill=True,
        fill_color=aqi_colors.get(row['AQI Category'], "gray"),
        fill_opacity=0.7,
        popup=f"{row['City']}, {row['Country']}: {row['AQI Value']} ({row['AQI Category']})"
    ).add_to(m)

# Add Legends
co2_color_scale.add_to(m)

### ---- Save the Final Map ---- ###
map_path = "combined_air_quality_co2_map.html"
m.save(map_path)
print(f"Combined map saved: {map_path}")
