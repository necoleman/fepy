import numpy as np
import FE
import triangle
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from pylab import *

import triangle.plot as plot

dom = {'vertices':np.array([[0.,0.],[1.,0.],[1.,.49],[.9,.49],[.9,.1],[.1,.1],[.1,.9],[.9,.9],[.9,.51],[1.,.51],[1.,1.],[0.,1.]]),'triangles':np.array([[0,1,5],[0,5,6],[1,4,5],[1,4,2],[2,3,4],[0,6,11],[6,10,11],[6,7,10],[7,8,9],[7,9,10]])}#,'segments':np.array([[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11]])}

print len(dom['vertices'])
print dom['triangles']

mesh = triangle.triangulate(dom,'pqa0.05')

print mesh

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

#z = efunc[:,11]
#plt.tricontourf(x,y,z,0,cmap='afmhot')
#axes().set_aspect('equal')
#plt.show()

for k in range(15):
	l = evals[k]
	t = 4.*np.pi*k/.28
	print str(l) + '  ...  ' + str(t) + ' ... ' + str(l < t)
