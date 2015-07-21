from scipy import linalg as lin
from scipy.sparse.linalg import eigsh
import numpy as np
from Mesh import *
import itertools

# assemble the FE matrices from a mesh
# v = list of vertices
# f = list of triangles
def assembleMatrices( tri ):

    v = tri['vertices']
    f = tri['triangles']

    n = len(v)

    L = np.zeros( (n,n) )
    M = np.zeros( (n,n) )

    for t in f:
        d = {t[0]:0,t[1]:1,t[2]:2}
        v0 = np.array(v[t[0]])
        v1 = np.array(v[t[1]])
        v2 = np.array(v[t[2]])

        area = np.abs( np.cross(v2-v0, v1-v0) )/2.0

        A = np.array( [[v0[0], v1[0], v2[0]], [v0[1], v1[1], v2[1]], [1., 1., 1.]] )

        B = lin.inv(A)

        g = B[:,:2]

        for i,j in itertools.product(t,t):

            L[i,j] += area*B[d[i],:2].dot(B[d[j],:2])

            if i == j:
                M[i,j] += 2.*area / (12.)
                
            else:
                M[i,j] += 2.*area / (24.)

    return L, M

def eigenvalues(L,M):

    ev,ef = lin.eigh(L,M)
    return ev,ef

# change to test git

# use sparse arnoldi solver to find first n eigenvalues of Lx = nMx
def sparseEigs(L,M,n=15):

    evals,evecs = eigsh(L,n,M,sigma=0.01,which='LM')
    return evals,evecs

def findEigs(mesh,n):
    L,M = assembleMatrices(mesh)
    evals,evecs = sparseEigs(L,M,n)

    return evals,evecs
