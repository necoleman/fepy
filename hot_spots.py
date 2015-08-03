import gc

import numpy as np
import triangle
import FE

import matplotlib.pyplot as plt
import matplotlib.tri as tri


def assembleTriangle(x,y,h):
	domain = {'vertices':np.array([[0.,0.],[1.,0.],[x,y]]),'triangles':np.array([0,1,2])}
	mesh = triangle.triangulate(domain,'qa'+str(h))
	return mesh

# return principle eigenvalue of triangle
def findTriangleEig(x,y,h):
	mesh = assembleTriangle(x,y,h)
	evals,evecs = FE.findEigs(mesh,n=2)
	return evals[1], evecs[:,1], mesh

def findTriangleEigs(x,y,h,n):
	mesh = assembleTriangle(x,y,h)
	evals,evecs = FE.findEigs(mesh,n=2*n)
	return evals[n], evecs[:,n], mesh

# plot principle eigenvalue's eigenfunction
def plotTriangleEig(x,y,h,contour=True):
	d = {'vertices':np.array([[0.,0.],[1.,0.],[x,y]]),'triangles':np.array([0,1,2])}
	l,v,m = findTriangleEig(x,y,h)
	X = m['vertices'][:,0]
	Y = m['vertices'][:,1]
	fig = plt.figure()
	ax = fig.add_subplot(111,aspect='equal')
	ax.axis('off')
	if contour:
		ax.tricontour(X,Y,v,250,cmap='coolwarm')
	ax.triplot(tri.Triangulation(d['vertices'][:,0],d['vertices'][:,1]))
	ax.tricontourf(X,Y,v,levels=[-1e9,0,1e9],cmap='gray')
	print 'eigenvalue: ' + str(l)
	plt.show()

# plot eigenvalue's eigenfunction
def plotTriangleEigs(x,y,h,k,contour=True):
	d = {'vertices':np.array([[0.,0.],[1.,0.],[x,y]]),'triangles':np.array([0,1,2])}
	l,v,m = findTriangleEigs(x,y,h,2*k)
	X = m['vertices'][:,0]
	Y = m['vertices'][:,1]
	fig = plt.figure()
	ax = fig.add_subplot(111,aspect='equal')
	ax.axis('off')
	if contour:
		ax.tricontour(X,Y,v,250,cmap='coolwarm')
	ax.triplot(tri.Triangulation(d['vertices'][:,0],d['vertices'][:,1]))
	ax.tricontourf(X,Y,v,levels=[-1e9,0,1e9],cmap='gray')
	print 'eigenvalue: ' + str(l)
	plt.show()


# d = domain; v = function; m = mesh
def plotTriangleFunc(d,v,m):
	X = m['vertices'][:,0]
	Y = m['vertices'][:,1]
	fig = plt.figure()
	ax = fig.add_subplot(111,aspect='equal')
	ax.tricontour(X,Y,v,250,cmap='coolwarm')
	ax.triplot(tri.Triangulation(d['vertices'][:,0],d['vertices'][:,1]))
	ax.tricontourf(X,Y,v,levels=[-1e9,0,1e9],cmap='gray')
	#print 'eigenvalue: ' + str(l)
	plt.show()

def maxValue(x,y,h):
	d = {'vertices':np.array([[0.,0.],[1.,0.],[x,y]]),'triangles':np.array([0,1,2])}
	l,v,m = findTriangleEig(x,y,h)
	indx, maxval = findMax(v)
	maxpt = m['vertices'][indx]
	return maxpt, l, v, m

# return the extremal value and index of that value of a 1d array	
def findMax(a):
	maxval = 0
	indx = 0
	for j in range(len(a)):
		if np.abs(a[j]) > maxval:
			maxval = a[j]
			indx = j
			#print maxval
	return indx, maxval

def maxValSurvey():
	stepsize = 0.01
	flaglist = []
	for x in np.arange(0.5,1.0,stepsize):
		for y in np.arange(stepsize,np.sqrt(1. - x**2),stepsize):
			maxpt, l, v, m = maxValue(x,y,0.001)
			d = {'vertices':m['vertices'][:3],'triangles':np.array([0,1,2])}
			print x,y,maxpt
			if np.linalg.norm(maxpt) > 0.05 and np.linalg.norm(maxpt - np.array([1.,0.])) > 0.05 and np.linalg.norm(maxpt - np.array([x,y])) > 0.005:
				print '     FLAG!!!'
				flaglist.append([x,y,maxpt])
				#plotTriangleFunc(d,v,m)
			gc.collect()

	print '\n\n***\n\nreiterating flags ...'
	new_flaglist = []
	for k in flaglist:
		x, y, p = k
		maxpt, l, v, m = maxValue(x,y,0.00001)
		print x,y,maxpt
		if np.linalg.norm(maxpt) > 0.05 and np.linalg.norm(maxpt - np.array([1.,0.])) > 0.05 and np.linalg.norm(maxpt - np.array([x,y])) > 0.005:
			print '******** FLAG!!!'
			new_flaglist.append([x,y,maxpt])

	print '\n\n***\n\nrereiterating flags ...'

	new_new_flaglist = []
	for k in new_flaglist:
		x, y, p = k
		maxpt, l, v, m = maxValue(x,y,0.00000001)
		print x,y,maxpt
		if np.linalg.norm(maxpt) > 0.05 and np.linalg.norm(maxpt - np.array([1.,0.])) > 0.05 and np.linalg.norm(maxpt - np.array([x,y])) > 0.005:
			print '******** FLAG!!!'
			new_new_flaglist.append([x,y,maxpt])


	print len(flaglist)
	print len(new_flaglist)
	print len(new_new_flaglist)

if __name__ == '__main__':
	maxValSurvey()
#	maxpt, l, v, m = maxValue(0.7,0.5)
#	d = {'vertices':m['vertices'][:3],'triangles':np.array([0,1,2])}
#	print maxpt
#	plotTriangleFunc(d,v,m)

