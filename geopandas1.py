# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:45:18 2021

@author: sebusiaczek
"""

import geopandas as gpd
import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
os.chdir('D:\lab\inf\cw2')

gdf=gpd.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf=gdf.to_crs("EPSG:4326")
gdf.plot("TOT",legend=True)



gdf['centroid']=gdf.centroid

#%%
import shapely as shap
xmin,ymin,xmax,ymax=[13,48,25,56]
n_cells=30
cell_size=(xmax-xmin)/n_cells
grid_cells=[]
for x0 in np.arange(xmin,xmax+cell_size,cell_size):
    for y0 in np.arange(ymin,ymax+cell_size,cell_size):
        x1=x0+cell_size
        y1=y0+cell_size
        grid_cells.append(shap.geometry.box(x0, y0, x1, y1)  )
cell = gpd.GeoDataFrame(grid_cells, columns=['geometry'])


ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT', cmap='jet')

plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")


merged = gpd.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, 'TOT'] = dissolve.TOT.values

ax = cell.plot(column='TOT', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('liczba ludności w siatce')
#%%
os.chdir('D:\lab\inf\cw2')

gdf=gpd.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf=gdf.to_crs("EPSG:4326")
#gdf.plot("TOT",legend=True)



gdf['centroid']=gdf.centroid
gdw=gpd.read_file('Województwa.shp')
gdw=gdw.to_crs("EPSG:4326")
#gdw.plot(legend=True)
cell = gpd.GeoDataFrame(gdw, columns=['geometry'])


ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT', cmap='jet')

plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")


merged = gpd.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, 'TOT'] = dissolve.TOT.values

ax = cell.plot(column='TOT', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('liczba ludności w województwach')

#%%
import geopandas as gpd
import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
os.chdir('D:\lab\inf\cw2')

gdf=gpd.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf=gdf.to_crs("EPSG:4326")
#gdf.plot("TOT",legend=True)



gdf['centroid']=gdf.centroid
gdw=gpd.read_file('Województwa.shp')
gdw=gdw.to_crs("EPSG:4326")
#gdw.plot(legend=True)
cell = gpd.GeoDataFrame(gdw, columns=['geometry'])


ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_0_14', cmap='jet')

plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")


merged = gpd.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, 'TOT_0_14'] = dissolve.TOT_0_14.values

ax = cell.plot(column='TOT_0_14', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('liczba ludności w województwach w wieku 0-14')
#%%
import geopandas as gpd
import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
os.chdir('D:\lab\inf\cw2')

gdf=gpd.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf=gdf.to_crs("EPSG:4326")
#gdf.plot("TOT",legend=True)



gdf['centroid']=gdf.centroid
gdw=gpd.read_file('Województwa.shp')
gdw=gdw.to_crs("EPSG:4326")
#gdw.plot(legend=True)
cell = gpd.GeoDataFrame(gdw, columns=['geometry'])


ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_15_64', cmap='jet')

plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")


merged = gpd.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, 'TOT_15_64'] = dissolve.TOT_15_64.values

ax = cell.plot(column='TOT_15_64', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('liczba ludności w województwach w wieku 15-65')
#%%
import geopandas as gpd
import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
os.chdir('D:\lab\inf\cw2')

gdf=gpd.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf=gdf.to_crs("EPSG:4326")
#gdf.plot("TOT",legend=True)



gdf['centroid']=gdf.centroid
gdw=gpd.read_file('Województwa.shp')
gdw=gdw.to_crs("EPSG:4326")
#gdw.plot(legend=True)
cell = gpd.GeoDataFrame(gdw, columns=['geometry'])


ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_65__', cmap='jet')

plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")


merged = gpd.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, 'TOT_65__'] = dissolve.TOT_65__.values

ax = cell.plot(column='TOT_65__', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('liczba ludności w województwach w wieku 65+')
#%%
import geopandas as gpd
import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
os.chdir('D:\lab\inf\cw2')

gdf=gpd.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf=gdf.to_crs("EPSG:4326")
#gdf.plot("TOT",legend=True)



gdf['centroid']=gdf.centroid
gdw=gpd.read_file('Województwa.shp')
gdw=gdw.to_crs("EPSG:4326")
#gdw.plot(legend=True)
cell = gpd.GeoDataFrame(gdw, columns=['geometry'])


ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_MALE_0_14', cmap='jet')

plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")


merged = gpd.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, 'TOT_MALE_0_14'] = dissolve.TOT_MALE_0_14.values

ax = cell.plot(column='TOT_MALE_0_14', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('liczba ludności w województwach w wieku 0-14 mężczyzn')
#%%
import geopandas as gpd
import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
os.chdir('D:\lab\inf\cw2')

gdf=gpd.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf=gdf.to_crs("EPSG:4326")
#gdf.plot("TOT",legend=True)



gdf['centroid']=gdf.centroid
gdw=gpd.read_file('Województwa.shp')
gdw=gdw.to_crs("EPSG:4326")
#gdw.plot(legend=True)
cell = gpd.GeoDataFrame(gdw, columns=['geometry'])


ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_MALE_15_64', cmap='jet')

plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")


merged = gpd.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, 'TOT_MALE_15_64'] = dissolve.TOT_MALE_15_64.values

ax = cell.plot(column='TOT_MALE_15_64', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('liczba ludności w województwach w wieku 15-64 mężczyzn')
#%%
import geopandas as gpd
import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
os.chdir('D:\lab\inf\cw2')

gdf=gpd.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf=gdf.to_crs("EPSG:4326")
#gdf.plot("TOT",legend=True)



gdf['centroid']=gdf.centroid
gdw=gpd.read_file('Województwa.shp')
gdw=gdw.to_crs("EPSG:4326")
#gdw.plot(legend=True)
cell = gpd.GeoDataFrame(gdw, columns=['geometry'])


ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_MALE_65__', cmap='jet')

plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")


merged = gpd.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, 'TOT_MALE_65__'] = dissolve.TOT_MALE_65__.values

ax = cell.plot(column='TOT_MALE_65__', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('liczba ludności w województwach w wieku 65+ mężczyzn')
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 12:08:09 2021

@author: weron
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
