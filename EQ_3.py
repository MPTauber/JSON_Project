############ if P:\Advanced not recognized, go into vscode --> settings.json --> delete the beginning of "" 
############ and leave "JSON_project\\Scripts\\python.exe"

#################### if pyplot doesnt work (line under the "from"s) then go into the terminal and do: pip3 install pyplot
import json

in_file = open("eq_data_30_day_m1.json","r")
out_file = open("readable_eq_data.json", "w")

eq_data = json.load(in_file) #loads it as a dictionary (cause thatrs what json is in)


json.dump(eq_data, out_file, indent=4) # makes the dictionary more eeasily readable. The indent just indents the stuff 4 levels deep.

list_of_eqs = eq_data["features"]  # Check the file to see what to use.
#################################### "features" is the key (so everything that follows is a list.) Each dictionary is one earthquake.


print(len(list_of_eqs)) # ow many earthquakes are in the list

mags, lons, lats = [],[],[] #three lists for magnitudes, latitudes, longitudes

for eq in list_of_eqs:
    mag = eq["properties"]["mag" ]# look at file to find position of earthquakes and their magnitude. 
    ###############################So the key is properties, and the key of that is mag
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    hover_texts = eq["properties"]["title"] # grabs the "title" 
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10]) #shows just the first 1o values

######## Now also find longitude and latitude. Check file and find "geometry" then "coordinates" 

from plotly.graph_objs import Scattergeo, Layout ## plotly is a large lib, so we only import a few things
from plotly import offline 
print(type(mags))

'''
data = [{ ### created dictionary to customize size of dots on map
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],## magnifies size of each dot 5 times
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar' : {'title':'Magnitude'} ## gives the little color thing on the side 
        },
}]

my_layout = Layout(title = "Global Earthquakles")

fig = {"data": data, "layout":my_layout}

offline.plot(fig,filename="global_earthquakes.html")'''