import numpy as np
import matplotlib.pyplot as plt
import math
import os
from mpl_toolkits import mplot3d

currentdirectory = os.path.dirname(__file__)

path0delay = currentdirectory + '/DataToGraph/0stepDelay.txt'
path1delay = currentdirectory + '/DataToGraph/1stepDelay.txt'
path2delay = currentdirectory + '/DataToGraph/2stepDelay.txt'
ffpath0delay = currentdirectory + '/DataToGraph/ff0stepDelay.txt'
ffpath1delay = currentdirectory + '/DataToGraph/ff1stepDelay.txt'
ffpath2delay = currentdirectory + '/DataToGraph/ff2stepDelay100step.txt'
script_path = os.path.dirname(__file__)
script_dir = os.path.split(script_path)[0]
rel_path = 'internal//PoleBalance//rc_smt_20230413084814_tg00869f05000_d002//rc_smt_20230413084814_tg00869f05000_d002_xy_track.txt'
abs_file_path = os.path.join(script_dir, rel_path)
lines = []
with open(ffpath2delay) as f:
    lines = f.readlines()
xcoords = []
ycoords = []
xang = []
yang = []
for line in lines:
    line = line.rstrip()
    splited = line.split("\t")
    xcoords.append(float(splited[0]))
    ycoords.append(float(splited[1]))
    xang.append(float(splited[2]))
    yang.append(float(splited[3]))
zcoord = [] #pole has height of 1
xcoordpole = []
ycoordpole = []
for i in range(0, len(xcoords)):
    xcoordpole.append(math.sin(xang[i]) + xcoords[i])
    zcoord.append(math.cos(xang[i]))
for i in range(0, len(ycoords)):
    ycoordpole.append(math.sin(yang[i]) + ycoords[i])

#print(zcoord)
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.scatter3D(xcoordpole, ycoordpole, zcoord)

ax.scatter(xcoords, ycoords)
plt.show()
