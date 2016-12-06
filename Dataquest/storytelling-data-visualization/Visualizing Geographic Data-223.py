## 1. Geographic Data ##

import pandas as pd

airlines = pd.read_csv("airlines.csv")
airports = pd.read_csv("airports.csv")
routes = pd.read_csv("routes.csv")

print(airlines.iloc[1])
print(airports.iloc[1])
print(routes.iloc[1])

## 4. Workflow With Basemap ##

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m = Basemap(projection="merc",llcrnrlat=-80,llcrnrlon=-180,urcrnrlat=80,urcrnrlon=180)

## 5. Converting From Spherical to Cartesian Coordinates ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
lat = airports["latitude"].tolist()
long = airports["longitude"].tolist()

x,y = m(long,lat)

## 6. Generating A Scatter Plot ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
x, y = m(longitudes, latitudes)

m.scatter(x,y,s=1)
plt.show()

## 7. Customizing The Plot Using Basemap ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()

## 8. Customizing The Plot Using Matplotlib ##

# Add code here, before creating the Basemap instance.
fig = plt.Figure(figsize=(15,20))
ax = fig.add_subplot(111)
ax.set_title("Scaled Up Earth With Coastlines")
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1, ax= ax)
m.drawcoastlines()
plt.show()

## 9. Introduction to Great Circles ##

geo_routes = pd.read_csv("geo_routes.csv")
print(geo_routes.info())
print(geo_routes.head())

## 10. Displaying Great Circles ##

fig, ax = plt.subplots(figsize=(15,20))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()

def create_great_circles(df):
    for i,r in df.iterrows():
        start_lon = r["start_lon"]
        start_lat = r["start_lat"]
        end_lon = r["end_lon"]
        end_lat = r["end_lat"] 
        if abs(start_lat-end_lat ) < 180 and abs(start_lon-end_lon) <180:
            m.drawgreatcircle(start_lon,start_lat,end_lon,end_lat) 

    
dfw = geo_routes[geo_routes['source'] == "DFW"]
create_great_circles(dfw)
plt.show()