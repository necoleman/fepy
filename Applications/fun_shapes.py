import gc

import numpy as np
import FE

import triangle
import triangle.plot as plot

import matplotlib.pyplot as plt
import matplotlib.tri as tri

point_list = {'vertices':np.array(
[[0,0],
[0,-11],
[0.5,-11],
[0.5,-6.4],
[6.4,-6.4],
[6.4,-11],
[30,-11],
[30,0]]), 
'segments':np.array([[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,0]])}#,
#'segment_markers': np.array([[1],[1],[1],[1],[1],[1],[1],[1]]),
#'vertex_markers':np.array([[1],[1],[1],[1],[1],[1],[1],[1]])}

mesh = triangle.triangulate(point_list,'pqa0.02')

ax1 = plt.subplot(111, aspect='equal')
plot.plot(ax1, **mesh)
plt.show()

print len(mesh['vertices'])

evals, evecs = FE.findEigs(mesh,50)

X = mesh['vertices'][:,0]
Y = mesh['vertices'][:,1]

v = evecs[:,45]

fig = plt.figure()
ax = fig.add_subplot(111,aspect='equal')
ax.tricontourf(X,Y,v,0,cmap='copper')
#ax.triplot(tri.Triangulation(t['vertices'][:,0],d['vertices'][:,1]))
#ax.tricontourf(X,Y,v,levels=[-1e9,0,1e9],cmap='gray')
plt.show()


