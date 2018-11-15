import numpy as np
import pathlib


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


index = 0
stages = [0]

while index < len(data_quasi)-1:
    index_new = index+int(np.ceil(data_quasi[index][-2]/cell_length))+1
    stages.append(index_new)
    index = index_new
stages = np.delete(stages, -1)
end_length = data_quasi[stages[-1]][-2]
print(end_length)
