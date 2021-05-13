# -*- coding: utf-8 -*-
"""
Created on Thu May 13 12:08:09 2021

@author: sebusiaczek
"""

#%%
import geopandas as gpd
import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os


gdf=gpd.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf=gdf.to_crs("EPSG:4326")
#gdf.plot("TOT",legend=True)



gdf['centroid']=gdf.centroid
gdw=gpd.read_file('Województwa.shp')
gdw=gdw.to_crs("EPSG:4326")
#gdw.plot(legend=True)
cell = gpd.GeoDataFrame(gdw, columns=['geometry'])


ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_FEM_0_14', cmap='jet')

plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")


merged = gpd.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, 'TOT_FEM_0_14'] = dissolve.TOT_FEM_0_14.values

ax = cell.plot(column='TOT_FEM_0_14', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('liczba ludności w województwach w wieku 0-14 kobiet')
#%%
import geopandas as gpd
import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os


gdf=gpd.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf=gdf.to_crs("EPSG:4326")
#gdf.plot("TOT",legend=True)



gdf['centroid']=gdf.centroid
gdw=gpd.read_file('Województwa.shp')
gdw=gdw.to_crs("EPSG:4326")
#gdw.plot(legend=True)
cell = gpd.GeoDataFrame(gdw, columns=['geometry'])


ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_FEM_15_64', cmap='jet')

plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")


merged = gpd.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, 'TOT_FEM_15_64'] = dissolve.TOT_FEM_15_64.values

ax = cell.plot(column='TOT_FEM_15_64', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('liczba ludności w województwach w wieku 15-64 kobiet')
#%%
import geopandas as gpd
import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os


gdf=gpd.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf=gdf.to_crs("EPSG:4326")
#gdf.plot("TOT",legend=True)



gdf['centroid']=gdf.centroid
gdw=gpd.read_file('Województwa.shp')
gdw=gdw.to_crs("EPSG:4326")
#gdw.plot(legend=True)
cell = gpd.GeoDataFrame(gdw, columns=['geometry'])


ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_FEM_65__', cmap='jet')

plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")


merged = gpd.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, 'TOT_FEM_65__'] = dissolve.TOT_FEM_65__.values

ax = cell.plot(column='TOT_FEM_65__', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('liczba ludności w województwach w wieku 65+ kobiet')
#%%
import geopandas as gpd
import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os


gdf=gpd.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf=gdf.to_crs("EPSG:4326")
#gdf.plot("TOT",legend=True)



gdf['centroid']=gdf.centroid
gdw=gpd.read_file('Województwa.shp')
gdw=gdw.to_crs("EPSG:4326")
#gdw.plot(legend=True)
cell = gpd.GeoDataFrame(gdw, columns=['geometry'])
ratio=gdf['TOT']/gdf['SHAPE_Area']

ax=gdf.plot(markersize=.1, figsize=(12, 8), column=ratio, cmap='jet')

plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")


merged = gpd.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, ratio] = ratio.values

ax = cell.plot(column=ratio, figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('gęstoć zaludnienia w poszczególnych województwach')