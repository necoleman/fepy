import numpy as np
import FE
import triangle
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from pylab import *

import triangle.plot as plot

dom = {'vertices':np.array([[0.,0.],[1.,0.],[1.,1.01],[0.,1.01]]),'triangles':np.array([[0,1,2],[0,2,3]])}

mesh = triangle.triangulate(dom,'qa0.0005')

ax1 = plt.subplot(111,aspect='equal')
plot.plot(ax1, **mesh)
plt.show()

L,M = FE.assembleMatrices(mesh)
evals,efunc = FE.sparseEigs(L,M)

fig = plt.figure()
vertices = np.asarray(mesh['vertices'])
faces = np.asarray(mesh['triangles'])
x = vertices[:,0]
y = vertices[:,1]
#for j in range(1,5):
#	z = efunc[:,j]
#	plt.tricontourf(x,y,z,0,cmap='afmhot')
#	axes().set_aspect('equal')
#	plt.show()

z = efunc[:,11]
plt.tricontourf(x,y,z,0,cmap='afmhot')
axes().set_aspect('equal')
plt.show()
