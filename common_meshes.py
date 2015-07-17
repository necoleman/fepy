import numpy as np

def square(dilation_factor):
	return {'vertices':dilation_factor*np.array([[0.,1.],[1.,1.],[0.,0.],[1.,0.]]),'triangles':np.array([[0,1,3],[0,2,3]])}

def rightTriangle(dilation_factor):
	return {'vertices':dilation_factor*np.array([[0.,0.],[1.,0.],[0.,1.]]),'triangles':np.array([[0,1,2]])}

def equilateralTriangle(dilation_factor):
	return {'vertices':dilation_factor*np.array([[0.,0.],[1.,0.],[0.5,np.sqrt(3.)/2.]]),'triangles':np.array([[0,1,2]])}


