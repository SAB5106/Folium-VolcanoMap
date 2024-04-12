import folium
import pandas as pd

# Initialise volcano data
data = pd.read_csv("./volcanoes.csv")
# Initialise pandas variables
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
# Initialise map
map = folium.Map(location=[41.59901965178514, -109.6281607566247],zoom_start=4.5)

# Function for icon colour
def iconColour(elevation):
    if elevation > 3000: return "red"
    elif elevation > 1500: return "orange"
    elif elevation > 1000: return "green"
    else: return "lightgreen"

# Add map markers
markerGroup = folium.FeatureGroup(name="Volcano Map")
for lt,ln,el,nm in zip(lat,lon,elev,name):
    markerGroup.add_child(folium.CircleMarker(
        location=[lt,ln],
        radius=8,
        popup=nm,
        fill=True,
        fill_color=iconColour(el),
        fill_opacity=0.8,
        color=iconColour(el)
    ))

# Output to HTML file
map.add_child(markerGroup)
map.save("./VolcanoMap.html")