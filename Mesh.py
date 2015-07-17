import numpy as np
import matplotlib.tri as tri
import matplotlib.pyplot as plt
import triangle

class Mesh:

    # vertices are stored as tuples of points
    # faces are stored as tuples of vertices
    def __init__(self):
        self.vertex_list = []
        self.face_list = []

	# import vertices from a triangulation
    def importTriangulation(self,tri):
        self.vertex_list = list(tri['vertices'])
		

    # add a face with the given indices
    def addFace(self,i,j,k):
        self.face_list.append( (i,j,k) )

    # add a vertex with the given indices
    def addVertex(self,x,y):
        self.vertex_list.append( np.array( [x,y] ) )

    def plot(self):
        points = np.asarray( self.vertex_list )
        x = points[:,0]
        y = points[:,1]
        triangles = np.asarray( self.face_list )

        plt.figure()
        plt.gca().set_aspect('equal')
        plt.triplot(x, y, triangles, 'go-')
        plt.show()

    def mplTriangObj(self):
        points = np.asarray( self.vertex_list )
        x = points[:,0]
        y = points[:,1]
        triangles = np.asarray( self.face_list )
        return x,y,triangles

	# note: need to rewrite the methods below
    
    # subdivide the given face
    def subdivide(self,i):
        face = self.face_list.pop(i)
        vertex0 = self.vertex_list[face[0]]
        vertex1 = self.vertex_list[face[1]]
        vertex2 = self.vertex_list[face[2]]

        # new vertices
        vertex01 = (vertex0 + vertex1)/2.0
        vertex02 = (vertex0 + vertex2)/2.0
        vertex12 = (vertex1 + vertex2)/2.0

        n = len(self.vertex_list)
        # add new vertices
        self.vertex_list.append(vertex01)
        self.vertex_list.append(vertex02)
        self.vertex_list.append(vertex12)

        # note that the indices are:
        # 01 --> n
        # 02 --> n+1
        # 12 --> n+2

        # new faces
        face0 = (face[0], n, n+1)
        face1 = (face[1], n+2, n)
        face2 = (face[2], n+1, n+2)
        face3 = (n, n+2, n+1)

        # add to face_list!
        self.face_list.append(face0)
        self.face_list.append(face1)
        self.face_list.append(face2)
        self.face_list.append(face3)

    def subdivide_all(self):
        old_face_list = self.face_list
        self.face_list = []
        for face in old_face_list:
            vertex0 = self.vertex_list[face[0]]
            vertex1 = self.vertex_list[face[1]]
            vertex2 = self.vertex_list[face[2]]

            # new vertices
            vertex01 = (vertex0 + vertex1)/2.0
            vertex02 = (vertex0 + vertex2)/2.0
            vertex12 = (vertex1 + vertex2)/2.0

            n = len(self.vertex_list)
            # add new vertices
            self.vertex_list.append(vertex01)
            self.vertex_list.append(vertex02)
            self.vertex_list.append(vertex12)

            # note that the indices are:
            # 01 --> n
            # 02 --> n+1
            # 12 --> n+2

            # new faces
            face0 = (face[0], n, n+1)
            face1 = (face[1], n+2, n)
            face2 = (face[2], n+1, n+2)
            face3 = (n, n+2, n+1)

            # add to face_list!
            self.face_list.append(face0)
            self.face_list.append(face1)
            self.face_list.append(face2)
            self.face_list.append(face3)            


