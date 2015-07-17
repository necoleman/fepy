from Mesh import *
import FE
import triangle
import triangle.plot
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

def testFE():
	ptlist = {'vertices':np.array(((0,0),(1,0),(1,1),(0,1)))}
	triang = triangle.triangulate(ptlist)

	print triang
	print '\n\n'
	print triang['vertices']
	print triang['triangles']

	triangle.plot.compare(plt,ptlist,triang)
	plt.show()

	print '\n\nNow testing the FE assembly ...'

	L,M = FE.assembleMatrices(triang)

	elist = FE.eigenvalues(L,M)[0]
	elist.sort()

	print 'eigenvalues:'

	for j in elist:
		print j

	triangle.plot.compare(plt,ptlist,triang)
	plt.show()

	triang = triangle.triangulate(triang,'rqa0.1')

	L,M = FE.assembleMatrices(triang)

	elist = FE.eigenvalues(L,M)[0]
	elist.sort()

	print '\n\neigenvalues:'

	for j in elist:
		print j

	triangle.plot.compare(plt,ptlist,triang)
	plt.show()

	triang = triangle.triangulate(triang,'rqa0.01')

	L,M = FE.assembleMatrices(triang)

	elist = FE.eigenvalues(L,M)[0]
	elist.sort()

	print '\n\neigenvalues:'

	for j in elist:
		print j

	triangle.plot.compare(plt,ptlist,triang)
	plt.show()

def testSubdivide():

    g = Mesh()
    g.addVertex(0,0)
    g.addVertex(1,0)
    g.addVertex(0,1)
    g.addFace(0,1,2)

    L,M = FE.assembleMatrices(g)

    #print L
    #print M

    elist = FE.eigenvalues(L,M)

    print '\n\n\n'
    #print elist

    g.plot()

    g.subdivide(0)

    L,M = FE.assembleMatrices(g)

    #print '\n\n'
    #print L
    #print M

    #print '\n\n'

    elist = FE.eigenvalues(L,M)

    #print '\n\n\n'
    #print elist

    #g.plot()

    #g.subdivide(0)

    #g.plot()

    #g.subdivide(0)

    #g.plot()

    #for k in range(10):
    #    j = np.random.choice( range(len(g.face_list)) )
    #    g.subdivide(j)

    g.subdivide_all()

    g.plot()

    g.subdivide_all()
    g.subdivide_all()

    g.plot()

    L,M = FE.assembleMatrices(g)

    elist = FE.eigenvalues(L,M)[0]
    elist.sort()

    print elist

    #v = np.ones( len(g.vertex_list) )
    #print L.dot(v) - M.dot(v)

def testSquare():

    ptlist = {'vertices':np.array( ((0.,0.),(0.5,0.),(1.,0.),(0.,0.5),(0.5,0.5),(1.,0.5),(0.,1.),(0.5,1.),(1.,1.)) )}
    t = triangle.triangulate(ptlist)
    t1 = triangle.triangulate(ptlist,'qa0.001')
	
    triangle.plot.compare(plt,t,t1)
#    plt.show()

    L,M = FE.assembleMatrices(t)
#    print L
#    print '\n\n'
#    print M

    np.savetxt('textL',L)
    np.savetxt('textM',M)

    eig = FE.eigenvalues(L,M)
    elist = eig[0]
    efunc = eig[1]
    print elist[0]
    print elist[1]
    print elist[2]

#    vertices = np.asarray(t['vertices'])
#    faces = np.asarray(t['triangles'])
#    x = vertices[:,0]
#    y = vertices[:,1]

#    z = efunc[1]

#    plt.figure()
#    plt.tricontourf(x,y,faces,z,cmap='afmhot')
#    plt.show()
    print '****************************'

    L,M = FE.assembleMatrices(t1)
    eig = FE.eigenvalues(L,M)
    elist = eig[0]
    efunc = eig[1]
    for j in range(10):
        print elist[j]

    vertices = np.asarray(t1['vertices'])
    faces = np.asarray(t1['triangles'])
    x = vertices[:,0]
    y = vertices[:,1]
    z = efunc[:,5]

    plt.figure()
    plt.tricontourf(x,y,z,100,cmap='afmhot')
    plt.show()

    print '***************************\n\n\n\n\n'


if __name__ == '__main__':
    testSquare()
