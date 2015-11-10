import FE
import triangle
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

tri = {'vertices':np.array([[0.,0.],[1.,0.],[0.7,0.05]]),'triangles':np.array([[0,1,2]])}

tri_mesh = triangle.triangulate(tri,'qa0.000005')

print str(len(tri_mesh['vertices'])) + ' nodes'

L,M = FE.assembleMatrices(tri_mesh)
eig = FE.eigenvalues(L,M)
elist = eig[0]
efunc = eig[1]
for j in range(10):
	print elist[j]

fig = plt.figure()
vertices = np.asarray(tri_mesh['vertices'])
faces = np.asarray(tri_mesh['triangles'])
x = vertices[:,0]
y = vertices[:,1]
for j in range(5):
	z = efunc[:,j]
	plt.tricontourf(x,y,z,100,cmap='afmhot')
	axes().set_aspect('equal')
	plt.show()

