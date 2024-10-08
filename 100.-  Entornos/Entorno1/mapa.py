import geopandas
import matplotlib.pyplot as plt

path = geopandas.datasets.get_path('naturalearth_lowres')

world = geopandas.read_file(path)
ax = world.plot()
world[world.continent == 'South America'].plot(ax=ax, cmap='Greens')
plt.show()

print(world)