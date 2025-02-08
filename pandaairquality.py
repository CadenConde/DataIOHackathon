import pandas as pd
import folium
import json
import branca.colormap as cm
from gtts import gTTS
import chardet

# ---- Detect File Encoding ----
file_path = "1. Cement_emissions.csv"  # Change this to your actual file path

with open(file_path, "rb") as f:
    raw_data = f.read(10000)  # Read a portion of the file
    detected_encoding = chardet.detect(raw_data)["encoding"]
    print(f"Detected file encoding: {detected_encoding}")

# ---- Load CO2 Emissions Data ----
try:
    df = pd.read_csv(file_path, encoding=detected_encoding)
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding="latin1")  # Fallback encoding

# Convert the dataset to long format
df_melted = df.melt(id_vars=["Year"], var_name="Country", value_name="CO2_Emissions")

# Fill NaN values with 0 for proper visualization
df_melted["CO2_Emissions"] = df_melted["CO2_Emissions"].fillna(0)

# ---- Load GeoJSON for World Map ----
geojson_path = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
  # Change to your actual GeoJSON file path
with open(geojson_path, "r") as f:
    world_geojson = json.load(f)

# Normalize CO2 emissions for color mapping
min_co2 = df_melted["CO2_Emissions"].min()
max_co2 = df_melted["CO2_Emissions"].max()

# Define a color scale (White → Orange → Purple)
color_scale = cm.LinearColormap(
    colors=["white", "orange", "purple"],
    vmin=min_co2,
    vmax=max_co2,
    caption="CO2 Emissions Over Time"
)

# ---- Create Interactive Map ----
m = folium.Map(location=[20, 0], zoom_start=2)

# Use the latest year available for visualization
latest_year = df["Year"].max()
latest_data = df_melted[df_melted["Year"] == latest_year]

# Create a dictionary mapping country names to CO2 emissions
country_emission_map = latest_data.set_index("Country")["CO2_Emissions"].to_dict()

# Function to style each country based on CO2 emissions
def style_function(feature):
    country_name = feature["properties"]["name"]
    emissions = country_emission_map.get(country_name, 0)
    return {
        "fillColor": color_scale(emissions) if emissions > 0 else "white",
        "color": "black",
        "weight": 0.5,
        "fillOpacity": 0.7,
    }

# Apply the style function to the GeoJSON layer
folium.GeoJson(
    world_geojson,
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["Country"], localize=True)
).add_to(m)

# Add the legend to the map
color_scale.add_to(m)

# ---- Save Map as an HTML File ----
map_path = "co2_emissions_map.html"
m.save(map_path)
print(f"Map saved: {map_path}")

# ---- Generate MP3 Audio Notification ----
audio_text = f"The CO2 emissions map for {latest_year} has been successfully created. Open the file co2_emissions_map.html to view it."
tts = gTTS(text=audio_text, lang="en")

# Save the audio file
mp3_path = "co2_emissions_map.mp3"
tts.save(mp3_path)

print(f"Audio notification saved: {mp3_path}")
