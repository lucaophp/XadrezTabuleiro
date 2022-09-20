import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

tab = np.tile([1,0], [8,4])
for i in range(tab.shape[0]):
  tab[i] = np.roll(tab[i], i % 2)
map_color = ListedColormap(['#779556','#ebecd0'])
plt.matshow(tab, cmap=map_color)
plt.xtricks([])
plt.ytricks([])
plt.show()
