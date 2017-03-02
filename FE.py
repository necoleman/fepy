from scipy import linalg as lin
from scipy.sparse.linalg import eigsh
import numpy as np
import itertools
import time

# assemble the finite element matrices from a mesh
# v = list of vertices
# f = list of triangles
# 
# mesh format: 
#       {'vertices': np.array([[v0, v1], [v2, v3],...]),
#        'triangles': np.array([[0, 1, 2], [3, 4, 5], ...]),
#        'segments': np.array([[0, 1], [2, 3]])}
#
# returns the two matrices in the finite-element eigenvalue equation
#
# Lx = uMx
#
# L is the matrix of the weak Laplacian, whose elements are inner products of
# gradients of the finite elements
# M is the matrix of the L^2 inner product, whose elements are the L^2 inner
# products of the finite elements
#
# NB this is defined with *piecewise-linear* elements over *triangular* meshes.
# For something more sophisticated, you're going to have to go to the
# professionals at Deal.II, FEnics, or PyDec.
def assembleMatrices( tri ):

    # list the vertices
    v = tri['vertices']
    # list the triangles
    f = tri['triangles']

    # number of vertices
    n = len(v)

    # initialize the matrices for the Laplacian and the inner product 
    # dimensions are (no. vertices)x(no. vertices)
    # Laplacian
    L = np.zeros( (n,n) )

    # L^2 inner product
    M = np.zeros( (n,n) )

    # now loop over each triangle in the mesh and add the submatrix
    # corresponding to the face
    for t in f:
        # set up a dict that remembers which vertex is zeroth, first, second
        d = {t[0]:0,t[1]:1,t[2]:2}

        # vertices of the triangle
        v0 = np.array(v[t[0]])
        v1 = np.array(v[t[1]])
        v2 = np.array(v[t[2]])

        # area of t
        area = np.abs( np.cross(v2-v0, v1-v0) )/2.0

        # barycentric embedding matrix for the triangle
        A = np.array([[v0[0], v1[0], v2[0]],
                     [v0[1], v1[1], v2[1]], [1., 1., 1.]])

        # invert to find the coordinates of the gradients of the
        # elements
        B = lin.inv(A)
        #g = B[:,:2]

        # now iterate through the 9 entries of 
        for i,j in itertools.product(t,t):

            # first, the matrix for the Laplacian
            # (it ends up being the area times the inner product
            # of the two gradients)
            L[i,j] += area*B[d[i],:2].dot(B[d[j],:2])

            # now, the matrix for the L^2 inner product

            # treat the diagonal differently ...
            if i == j:
                M[i,j] += 2.*area / (12.)
            # ... than the off-diagonal
            else:
                M[i,j] += 2.*area / (24.)

    # return the finished product
    return L, M

# method for assembling L,M for Dirichlet boundary conditions
# (still doesn't work. needs double-checking)
#
# hand in a mesh which *also* 
def assembleDirichlet( tri ):
    L, M = assembleMatrices(tri)
    n = len( tri['vertices'] )

    # set the appropriate rows  of the Laplacian and the 
    # L^2 inner product matrices to zero
    for x in tri['segments']:
        i = x[0]
        L[i,:] = np.zeros(n)
        M[i,:] = np.zeros(n)
        L[i,i] = 1.0

    return L,M

# this finds *all* possible eigenvalues using a *dense* solver
# avoid --- it is very expensive for large meshes 
def eigenvalues(L,M):
    ev,ef = lin.eigh(L,M)
    return ev,ef

# use sparse arnoldi solver to find first n eigenvalues of Lx = nMx
def sparseEigs(L,M,n=15):

    # hand it to the black box!
    evals,evecs = eigsh(L,n,M,sigma=0.01,which='LM')

    # return the product
    return evals,evecs

# wrap it all up
# this method takes in a mesh and a number n
# and returns the first n eigenvalues/vectors of that mesh
# as a bonus, it also prints how long it took to stdout
def findEigs(mesh, n, bc='Neumann', verbose=False):
    # start the timer
    start = time.time()

    # build the matrices
    if bc is 'Neumann':
        L,M = assembleMatrices(mesh)
    elif bc is 'Dirichlet':
        L,M = assembleDirichlet(mesh)
    else:
        print("Sorry! Not valid boundary conditions!")

    # find the eigenvalues and eigenvectors
    evals,evecs = sparseEigs(L,M,n)

    # stop the timer
    finish = time.time()

    # print the results
    if verbose:
        print('             time: ' + str(finish - start))

    # return the finished product
    return evals,evecs
