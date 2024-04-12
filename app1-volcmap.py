import folium
import pandas as pd

# Read in volcano data
data = pd.read_csv("./volcanoes.csv")
# Variables for map markers
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
# Initialise map; the focus starts around the US MidWest
map = folium.Map(location=[41.59901965178514, -109.6281607566247],zoom_start=4.5)

# Function for map marker colour
def iconColour(elevation):
    if elevation > 3000: return "red"
    elif elevation > 1500: return "orange"
    elif elevation > 1000: return "green"
    else: return "lightgreen"

# Iterate through volcano list; create map marker then add to marker group
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

# Add contents of marker group to map
map.add_child(markerGroup)
# Save map HTML file
map.save("./VolcanoMap.html")
