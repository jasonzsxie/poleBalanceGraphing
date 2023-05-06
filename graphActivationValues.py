import numpy as np
import matplotlib.pyplot as plt
import math
import os
from mpl_toolkits import mplot3d

currentdirectory = os.path.dirname(__file__)

path0delay = currentdirectory + '/ActivationValues/0stepdelay.txt'
path1delay = currentdirectory + '/ActivationValues/1stepdelay.txt'
path2delay = currentdirectory + '/ActivationValues/2stepdelay.txt'
ffpath0delay = currentdirectory + '/ActivationValues/ff0stepdelay.txt'
ffpath1delay = currentdirectory + '/ActivationValues/ff1stepdelay.txt'
ffpath2delay = currentdirectory + '/ActivationValues/ff2stepdelay2.txt'

# script_path = os.path.dirname(__file__)
# script_dir = os.path.split(script_path)[0]
# rel_path = 'internal//PoleBalance//rc_smt_20230413084814_tg00869f05000_d002//rc_smt_20230413084814_tg00869f05000_d002_xy_track.txt'
# abs_file_path = os.path.join(script_dir, rel_path)
lines = []
with open(path0delay) as f:
    lines = f.readlines()
xcoords = []
ycoords = []
zcoords = []
for line in lines:
    line = line.rstrip()
    splited = line.split("\t")
    xcoords.append(float(splited[0]))
    ycoords.append(float(splited[1]))
    zcoords.append(float(splited[2]))

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.scatter3D(xcoords, ycoords, zcoords)
plt.show()
