import numpy as np
import pathlib
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection


quasi = pathlib.Path("input/quasi.txt")
if quasi.exists():
    print("file quasi exists")
else:
    print("Error: file quasi does not exist")

events = pathlib.Path("input/new_events.txt")
if events.exists():
    print("file events exists")
else:
    print("Error: file events does not exist")

data_quasi = np.loadtxt(quasi)
data_events = np.loadtxt(events, skiprows=1)

cell_length = data_quasi[0][-1]
end_length = np.amax(data_quasi, axis=0)[-2]
index_max = np.argmax(data_quasi, axis=0)[-2]
height_max = max(data_quasi[index_max + 1][-2], abs(data_quasi[index_max + 1][-1]), np.amax(data_events, axis=0)[3],
                 -np.amin(data_events, axis=0)[3])
length_max = max(end_length, np.amax(data_events, axis=0)[3])
opening_max = data_quasi[index_max+1][1]
opening_min = np.amin(data_quasi, axis=0)[1]

index = 0
quasi_stages = [0]
while index < index_max:
    index = index + int(np.ceil(data_quasi[index][-2] / data_quasi[index][-1])) + 1
    quasi_stages.append(index)

for plot_index in quasi_stages:
    fig, ax = plt.subplots()
    patches = []
    number_of_full_cells = int(data_quasi[plot_index][-2]/cell_length)
    for cell_index in range(number_of_full_cells):
        x_min = cell_index*cell_length
        x_max = x_min+cell_length
        y_min = data_quasi[plot_index+1+cell_index][-1]
        y_max = data_quasi[plot_index+1+cell_index][-2]
        coord = np.array([[x_min, y_min],
                          [x_min, y_max],
                          [x_max, y_max],
                          [x_max, y_min]])
        patches.append(Polygon(coord, True))
    x_min = number_of_full_cells*cell_length
    x_max = data_quasi[plot_index][-2]
    y_min = data_quasi[plot_index+number_of_full_cells+1][-1]
    y_max = data_quasi[plot_index + number_of_full_cells + 1][-2]
    coord = np.array([[x_min, y_min],
                      [x_min, y_max],
                      [x_max, y_max],
                      [x_max, y_min]])
    patches.append(Polygon(coord, True))
    p = PatchCollection(patches)
    ax.add_collection(p)
    ax.set_xlim((0, length_max))
    ax.set_ylim((-height_max, height_max))
    fig.savefig('output/time'+str(int(data_quasi[plot_index][1]))+'.png')
    plt.close()



