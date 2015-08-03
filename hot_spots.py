import numpy as np
import triangle
import FE

import matplotlib.pyplot as plt
import matplotlib.tri as tri


def assembleTriangle(x,y):
	domain = {'vertices':np.array([[0.,0.],[1.,0.],[x,y]]),'triangles':np.array([0,1,2])}
	mesh = triangle.triangulate(domain,'qa0.00005')
	return mesh

# return principle eigenvalue of triangle
def findTriangleEig(x,y):
	mesh = assembleTriangle(x,y)
	evals,evecs = FE.findEigs(mesh,n=2)
	return evals[1], evecs[:,1], mesh

# plot principle eigenvalue's eigenfunction
def plotTriangleEig(x,y):
	d = {'vertices':np.array([[0.,0.],[1.,0.],[x,y]]),'triangles':np.array([0,1,2])}
	l,v,m = findTriangleEig(x,y)
	X = m['vertices'][:,0]
	Y = m['vertices'][:,1]
	plt.tricontour(X,Y,v,250,cmap='coolwarm')
	plt.triplot(tri.Triangulation(d['vertices'][:,0],d['vertices'][:,1]))
	plt.tricontourf(X,Y,v,0,cmap='gray')
	print 'eigenvalue: ' + str(l)
	plt.show()

def maxValue(x,y):
	d = {'vertices':np.array([[0.,0.],[1.,0.],[x,y]]),'triangles':np.array([0,1,2])}
	l,v,m = findTriangleEig(x,y)
	indx, maxval = findMax(v)
	maxpt = m['vertices'][indx]
	return maxpt

# return the extremal value and index of that value of a 1d array	
def findMax(a):
	maxval = 0
	indx = 0
	for j in range(len(a)):
		if np.abs(a[j]) > maxval:
			maxval = a[j]
			indx = j
	return indx, maxval

def maxValSurvey():
	stepsize = 0.1
	for x in np.arange(0.5,1.0,stepsize):
		for y in np.arange(stepsize,np.sqrt(1. - x**2),stepsize):
			print x,y,maxValue(x,y)

if __name__ == '__main__':
	plotTriangleEig(0.6,0.6)
