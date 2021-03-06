import FE
import triangle
import common_meshes
import time

def compareSparseDense():
	print '\n\n\n************'

	domain = common_meshes.square(1)

	eigenlist = []

	start_mesh = time.time()
	mesh = triangle.triangulate(domain,'qa0.00001')
	finish_mesh = time.time()

	print 'n:'
	print len(mesh['vertices'])

	print '\nmesh building time:'
	print finish_mesh - start_mesh

	start_assemble = time.time()
	L,M = FE.assembleMatrices(mesh)
	finish_assemble = time.time()

	print '\nassembly time:'
	print finish_assemble - start_assemble

	start_sparse = time.time()
	e_sparse = FE.sparseEigs(L,M)
	finish_sparse = time.time()

	print '\n\nsparse compute time:'
	print finish_sparse - start_sparse

#	start_dense = time.time()
#	e_dense = FE.eigenvalues(L,M)
#	finish_dense = time.time()

#	print '\ndense compute time:'
#	print finish_dense - start_dense

	print '\n\n********\nsparsely computed eigenvalues:'

	evals = e_sparse[0]
	evals.sort()
	for j in evals:
		print j

	print '********\n\n'

def sparseTime():
	meshAreas = []
	for k in range(1):
		meshAreas.append(0.0001 + 0.00001*k)

		meshAreas.append(0.001 + 0.0001*k)

	domain = common_meshes.square(1)
	mesh_count = []
	assemble_time = []
	eig_time = []
	lambda1 = []

	eig = []

	for h in meshAreas:
		mesh = triangle.triangulate(domain,'qa'+str(h))
		mesh_count.append(len(mesh['vertices']))

		start_assemble = time.time()
		L,M = FE.assembleMatrices(mesh)
		finish_assemble = time.time()
		assemble_time.append(finish_assemble - start_assemble)

		start_sparse = time.time()
		eig = FE.findEigs(mesh,15)
		finish_sparse = time.time()
		eig_time.append(finish_sparse - start_sparse)

		lambda1.append(eig[0][1])

	for k in range(len(meshAreas)):
		print mesh_count[k], assemble_time[k], eig_time[k], lambda1[k]

	print eig

if __name__ == '__main__':
	sparseTime()
