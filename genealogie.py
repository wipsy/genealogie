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

fig     = plt.figure()
ax      = fig.add_subplot(111)

map = Basemap( resolution='i', projection='tmerc', lat_0 = 46.227638, lon_0 = 2.213749000000007, width = 1000000, height = 1000000)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='lightgrey',lake_color='aqua')
map.drawcoastlines()

map.readshapefile('departements-20170102', 'france')
print(map.france_info)

patches   = []
for info, shape in zip(map.france_info, map.france):
    if info['nom'] == 'Haute-Loire':
        patches.append( Polygon(np.array(shape), True) )
        
ax.add_collection(PatchCollection(patches, facecolor= 'm', edgecolor='w', linewidths=1., zorder=2))

x, y = map(0, 0)
map.plot(x, y, marker='D',color='m')

plt.show()
