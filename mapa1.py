# Mapa
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
map = Basemap(projection='merc', lat_0 = -34, lon_0 = -58,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-58.8, llcrnrlat=-34.7,
    urcrnrlon=-57.1, urcrnrlat=-34.1)
 
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'grey')
map.drawmapboundary()
 
plt.show()
