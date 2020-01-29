import json

in_file = open("eq_data_1_day_m1.json","r")
out_file = open("readable_eq_data.json", "w")

eq_data = json.load(in_file) #loads it as a dictionary (cause thatrs what json is in)

print(type(eq_data))


json.dump(eq_data, out_file, indent=4) # makes the dictionary more eeasily readable. The indent just indents the stuff 4 levels deep.

list_of_eqs = eq_data["features"]  # Check the file to see what to use.
#################################### "features" is the key (so everything that follows is a list.) Each dictionary is one earthquake.

print(type(list_of_eqs))

print(len(list_of_eqs)) # ow many earthquakes are in the list

mags, lons, lats = [],[],[] #three lists for magnitudes, latitudes, longitudes

for eq in list_of_eqs:
    mag = eq["properties"]["mag" ]# look at file to find position of earthquakes and their magnitude. 
    ###############################So the key is properties, and the key of that is mag
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10]) #shows just the first 1o values

######## Now also find longitude and latitude. Check file and find "geometry" then "coordinates" 

from plotly.graph_objs import Scattergeo, Layout ## plotly is a large lib, so we only import a few things
from plotly import offline 

data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title = "Global Earthquakles")

fig = {"data": data, "layout":my_layout}

offline.plot(fig,filename="global_earthquakes.html")