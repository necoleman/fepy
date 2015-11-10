import numpy as np

# these methods just return common meshes, useful for testing
# the idea is to 

# a dilation_factor x dilation_factor square
def square(dilation_factor):
	return {'vertices':dilation_factor*np.array([[0.,1.],[1.,1.],[0.,0.],[1.,0.]]),'triangles':np.array([[0,1,3],[0,2,3]])}

# a right triangle
def rightTriangle(dilation_factor):
	return {'vertices':dilation_factor*np.array([[0.,0.],[1.,0.],[0.,1.]]),'triangles':np.array([[0,1,2]])}

# an equilateral triangle
def equilateralTriangle(dilation_factor):
	return {'vertices':dilation_factor*np.array([[0.,0.],[1.,0.],[0.5,np.sqrt(3.)/2.]]),'triangles':np.array([[0,1,2]])}

# classic example of isospectral domains from the '90s
# (is the '90s classic now?)
def isospectralDomains():
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

	return domain1, domain2
