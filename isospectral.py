import gc

import numpy as np
import FE

import triangle
import triangle.plot as plot

import matplotlib.pyplot as plt
import matplotlib.tri as tri

domain1 = {
'vertices':np.array([
[0.,0.],
[1.,0.],
[1.5,0.5],
[2.,0.],
[2.,1.],
[1.5,1.5],
[1.,1.],
[0.5,0.5],
[0.,1.]
]), 
'triangles':np.array([
[0,1,7],
[1,6,7],
[1,2,6],
[2,3,4],
[2,4,6],
[4,5,6],
[0,7,8]
])
}


domain2 = {
'vertices':np.array([
[2.,0.],
[2.5,-0.5],
[3.,0.],
[2.5,0.5],
[3.,1.],
[3.,2.],
[2.5,1.5],
[2.,2.],
[2.,1.]
]),
'triangles':np.array([
[0,1,2],
[0,2,3],
[0,3,8],
[3,4,8],
[4,5,6],
[4,6,8],
[6,7,8]
])
}


mesh1 = triangle.triangulate(domain1, 'pqa0.02r')
mesh2 = triangle.triangulate(domain2, 'pqa0.02r')

ax1 = plt.subplot(121, aspect='equal')
ax2 = plt.subplot(122, aspect='equal')
plot.plot(ax1, **mesh1)
plot.plot(ax2, **mesh2)
plt.show()

X1 = mesh1['vertices'][:,0]
Y1 = mesh1['vertices'][:,1]

X2 = mesh2['vertices'][:,0]
Y2 = mesh2['vertices'][:,1]

evals1,evecs1 = FE.findEigs(mesh1,25)
evals2,evecs2 = FE.findEigs(mesh2,25)

for j in range(25):
	x1 = evals1[j]
	x2 = evals2[j]
	print x1, x2, np.abs(x2 - x1), np.abs(x2 - x1)/min(x2,x1)

k = 17
v1 = evecs1[:,k]
v2 = evecs2[:,k]

#ax1 = plt.subplot(121,aspect='equal')
#ax1.tricontourf(X1,Y1,v1,0,cmap='copper')
#ax2 = plt.subplot(122,aspect='equal')
#ax2.tricontourf(X2,Y2,v2,0,cmap='copper')
#ax.triplot(tri.Triangulation(t['vertices'][:,0],d['vertices'][:,1]))
#ax.tricontourf(X,Y,v,levels=[-1e9,0,1e9],cmap='gray')
#plt.show()

fn_list = [[X1,Y1,v1],[X2,Y2,v2]]

n = len(X1)

f = open('isospectral.dat', 'w+')
f.truncate()
for t in mesh1['triangles']:
	s = ''
	tdata = []
	for j in range(3):
		x,y = mesh1['vertices'][t[j]]
		z = v1[t[j]]
		tdata.append([np.array([x,y]),z])
	p1 = tdata[0][0]
	p2 = tdata[1][0]
	p3 = tdata[2][0]
	center = (p1 + p2 + p3)/3.
	zcent = (tdata[0][1] + tdata[1][1] + tdata[2][1])/3.0

	tdata.append*( [center, zcent] )

	f.write( s )
	f.write('\n\n')


f.close()
