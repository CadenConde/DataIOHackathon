import pandas as pd
import folium
from geopy.geocoders import Nominatim
import random

# Load dataset
file_path = "hackathon/data/global air pollution dataset.csv"
df = pd.read_csv(file_path)

# Randomly select 50 cities
df_sample = df.sample(n=750, random_state=42).copy()

# Initialize geocoder
geolocator = Nominatim(user_agent="geoapi")

# Function to get latitude and longitude
n = 1
print("finding lat/long...")

def get_lat_lon(city, country, n=n):
    print(random.random())
    try:
        location = geolocator.geocode(f"{city}, {country}")
        if location:
            return location.latitude, location.longitude
    except:
        return None, None

# Add latitude and longitude columns
df_sample[['Latitude', 'Longitude']] = df_sample.apply(
    lambda row: pd.Series(get_lat_lon(row['City'], row['Country'])), axis=1
)

# Drop rows with missing coordinates
df_sample = df_sample.dropna(subset=['Latitude', 'Longitude'])

# Create folium map
map = folium.Map(location=[20, 0], zoom_start=2)

# Define AQI category colors
aqi_colors = {
    "Good": "green",
    "Moderate": "yellow",
    "Unhealthy for Sensitive Groups": "orange",
    "Unhealthy": "red",
    "Very Unhealthy": "purple",
    "Hazardous": "maroon"
}

# Add markers to the map
print("adding to map...")
for _, row in df_sample.iterrows():
    folium.CircleMarker(
        location=(row['Latitude'], row['Longitude']),
        radius=5,
        color=aqi_colors.get(row['AQI Category'], "gray"),
        fill=True,
        fill_color=aqi_colors.get(row['AQI Category'], "gray"),
        fill_opacity=0.7,
        popup=f"{row['City']}, {row['Country']}: {row['AQI Value']} ({row['AQI Category']})"
    ).add_to(map)

# Save and display the map
map.save("air_quality_map.html")