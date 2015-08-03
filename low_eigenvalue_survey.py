from scipy import linalg as lin
import numpy as np
from Mesh import *
import itertools
import FE
import triangle

from tqdm import *

def triangleMesh(x,y,refinement):
	

	domain = {'vertices':np.array([[0.,0.],[1.,0.],[x,y]]),'triangles':np.array([[0,1,2]])}
	mesh = triangle.triangulate(domain, 'qa'+str(refinement))

	return mesh



# a,b,c = ANGLES
def buildTriangle(a,b,c):
	angles = [a,b,c]
	angles.sort()
	
	# law of sines says what the next side is
	r = np.sin(angles[1])/np.sin(angles[2])
	x = r*np.cos(angles[0])
	y = r*np.sin(angles[0])
	
	return triangleMesh(x,y,0.0001)

def eigenvalueSurvey(n):

	fn_list = []

	ds = 0.0005

	domain_list = []

	for x in np.arange(0.45,0.55,ds):
		max_height = min( 1.0 - x**2, 1.0 - (x-1.0)**2 )
		for y in np.arange(np.sqrt(3.)/2. - 0.05, np.sqrt(3.)/2. + 0.05, ds):
			domain_list.append( [x,y] )

	for p in tqdm(domain_list):
		x = p[0]
		y = p[1]
		area = y/2.0

		# define triangle
		T = triangleMesh(x,y,0.001)

		# get eigenvalues
		L,M = FE.assembleMatrices(T)
		eigvals = FE.sparseEigs(L,M,n)[0]
		for j in range(len(eigvals)):
			eigvals[j] = eigvals[j]*area		
		
		current_tuple = [x,y]+list(eigvals)

		fn_list.append(current_tuple)


	f = open('eig.dat', 'w+')
	f.truncate()
	for j in range(len(fn_list)):
		s = ''
		for k in range(n+2):
			s = s + str(fn_list[j][k]) + ' ' 
		s = s + '\n'
		f.write( s )
	f.close()

if __name__ == '__main__':
	eigenvalueSurvey(7)
