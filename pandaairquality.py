import pandas as pd
import folium
import json
import branca.colormap as cm
import numpy as np
from pathlib import Path
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

# ---- Load GeoJSON for World Map ----
geojson_path = Path("./hackathon/data/Externaldata/countries.geo.json").resolve()  # Adjust path as needed
with open(geojson_path, "r") as f:
    world_geojson = json.load(f)

# ---- Convert the dataset to long format ----
df_melted = df.melt(id_vars=["Year"], var_name="Country", value_name="CO2_Emissions")
# fix usa name so that the mapper can read its values
df_melted["Country"] = df_melted["Country"].replace("USA", "United States of America")
df_melted["CO2_Emissions"] = df_melted["CO2_Emissions"].fillna(0)

# usaxx = df_melted[df_melted['Country'] == "Russia"]
# print(usaxx)
# print(usaxx['CO2_Emissions'].mean())
# raise
# ---- Compute Average CO2 Emissions Per Country ----
df_avg = df_melted.groupby("Country", as_index=False)["CO2_Emissions"].mean()

# ---- Apply Log Transformation for Better Low-End Detail ----
# Using np.log1p ensures that zero values are handled (log1p(0)==0)
df_avg["Log_CO2_Emissions"] = np.log1p(df_avg["CO2_Emissions"])

# Get min and max of the log-transformed values for the color scale
min_log, max_log = df_avg["Log_CO2_Emissions"].min(), df_avg["Log_CO2_Emissions"].max()

# ---- Create a Color Scale based on Log-Transformed Emissions ----
color_scale = cm.LinearColormap(
    colors=["white", "lightyellow", "orange", "red", "purple", "#210042"],
    vmin=min_log,
    vmax=max_log,
    caption="Log-scaled CO₂ Emissions (log₁ₚ)"
)

# ---- Create a Mapping from Country to its Log-Transformed Emissions ----
country_emission_map = df_avg.set_index("Country")["Log_CO2_Emissions"].to_dict()

# ---- Define a Style Function that Uses the Log-Scaled Emissions ----
def style_function(feature):
    country_name = feature["properties"]["name"]
    # Get the log-scaled emission; default to 0 if not found
    emission_log = country_emission_map.get(country_name, 0)
    return {
        "fillColor": color_scale(emission_log),
        "color": "black",
        "weight": 0.5,
        "fillOpacity": 0.7,
    }

# ---- Create the Folium Map ----
m = folium.Map(location=[20, 0], zoom_start=2)

# ---- Add the GeoJSON Layer with the Custom Style and Tooltip ----
folium.GeoJson(
    world_geojson,
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["Country"], localize=True)
).add_to(m)

# ---- Add the Legend to the Map ----
color_scale.add_to(m)

# ---- Save the Map as an HTML File ----
map_path = "co2_emissions_map.html"
m.save(map_path)
print(f"Map saved: {map_path}")
