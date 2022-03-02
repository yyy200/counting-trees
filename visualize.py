import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as cx

aoi_boundary_HARV = gpd.read_file("tree-wgs84/TOPO_TREE_WGS84.shp")
ax = aoi_boundary_HARV.plot(markersize=1)
cx.add_basemap(ax, crs=aoi_boundary_HARV.crs.to_string())

plt.show()
