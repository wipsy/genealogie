'''
Documentation, License etc.

@package genealogie
'''

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.patches import PathPatch
import numpy as np
import geojson
import geopandas as gpd
import mplleaflet

ancestors = gpd.GeoDataFrame.from_file('data/Genealogie.geojson')
#france_map = gpd.GeoDataFrame.from_file('map-geojson/Metropolitan_France_AL6.GeoJson')

print(ancestors)    
ancestors['count'] = ancestors.groupby('birth place')['birth place'].transform('count')
print(ancestors)

ancestors[1:10].plot(s=ancestors['count'][1:10]*100, column='birth', colormap='plasma')

#plt.scatter(ancestors['longitude'][1:10], ancestors['latitude'][1:10], s=ancestors['count'][1:10]*100, c=ancestors['birth'][1:10], cmap='plasma') # Draw blue line

#fig, ax = plt.subplots()
#ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

#print(weight['Bourbourg(59)'])

#ax = genealogie.geometry.plot()
#mplleaflet.display(fig=ax.figure) # To display it right at the notebook.
mplleaflet.show() # To output _map.html file and display it in your browser.

#fig     = plt.figure()
#ax      = fig.add_subplot(111)

#map = Basemap( resolution='i', projection='tmerc', lat_0 = 46.227638, lon_0 = 2.213749000000007, width = 1000000, height = 1000000)

#map.drawmapboundary(fill_color='aqua')
#map.fillcontinents(color='lightgrey',lake_color='aqua')
#map.drawcoastlines()

#map.readshapefile('shapefiles/departements-20170102', 'france')
#print(map.france_info)


#patches   = []
#for info, shape in zip(map.france_info, map.france):
    #poly = Polygon(np.array(shape), True)
     #contains_point(point, transform=None, radius=0.0)¶
    #if poly.contains((0, 0)):
        #patches.append( poly )
        
#ax.add_collection(PatchCollection(patches, facecolor= 'm', edgecolor='w', linewidths=1., zorder=2))

#x, y = map(0, 0)
#map.plot(x, y, marker='D',color='m')
