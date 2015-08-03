import numpy as np
from scipy.special import *
import FE
from Tkinter import *
import triangle
import common_meshes

import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import matplotlib.tri as tri

# simple gui plan:
# 	
class FEGui:
	
	def __init__(self,root,canvas_width,canvas_height):
		self.root=root
		self.canvas_width = canvas_width
		self.canvas_height = canvas_height

		self.nodes = False
		self.eiglevel = 1
		self.current_refine = 1

		# set up the domain
		self.dom = {'vertices':np.array([[0.,0.],[1.,0.7],[0.5,0.5]])}
		self.mesh = triangle.triangulate(self.dom,'qa0.001')
		x = self.mesh['vertices'][:,0]
		y = self.mesh['vertices'][:,1]
		
		self.eigvals,self.eigvecs = FE.findEigs(self.mesh,10)
		z = self.eigvecs[:,self.eiglevel]

		# set up the matplotlib nonsense
		self.fig, self.ax = mpl.pyplot.subplots()

		self.ax.clear()
		self.ax.autoscale(enable=False)
		self.ax.axis('off')
		
		triang = tri.Triangulation(x,y)
		self.ax.tricontourf(triang,z,100,cmap=plt.get_cmap('copper'))

		self.canvas = FigureCanvasTkAgg(self.fig,master=root)
		self.canvas.show()
		self.canvas.get_tk_widget().pack()

		#self.canvas.mpl_connect("button_press_event", self.setVertex)
		self.canvas.mpl_connect("key_press_event", self.keyEvent)

		print 'connected key press'

		self.ax.set_xlim([0,1])
		self.ax.set_ylim([0,1])
		self.ax.autoscale(enable=False)

		self.fig.tight_layout()

		self.redraw()

		# build and pack other controls
		self.control_frame = Frame(master=root,width=canvas_width/4,height=canvas_height)
		
		self.control_frame.pack(side=TOP)

		self.b = Button(self.control_frame, text="QUIT", command = self.quit)
		self.b.pack(side=LEFT)

		self.c = Button(self.control_frame, text="Toggle Nodal", command=self.toggle)
		self.c.pack(side=LEFT)
		
		self.s = Button(self.control_frame, text="Energy Up", command=self.energy_up)
		self.s.pack(side=LEFT)

		self.t = Button(self.control_frame, text="Energy Down", command=self.energy_down)
		self.t.pack(side=LEFT)

	def keyEvent(self,event):
		print event.key
		if event.key == 'r':
			self.refine()
		if event.key == 'c':
			self.coarsen()
		if event.key == 'up':
			self.energy_up()
			print 'up'
		if event.key == 'down':
			self.energy_down()
		if event.key == ' ':
			self.redraw()


	def quit(self):
		sys.exit()

	def toggle(self):
		self.nodes = not self.nodes
		self.redraw()

	# domain manipulation methods
	def refine(self,event):
		if self.current_refine < 100:
			self.current_refine += 5
		self.redraw()

	def coarsen(self,event):
		if self.current_refine > 5:
			self.current_refine -= 5
		self.redraw()


	def energy_up(self):
		self.eiglevel += 1
		self.redraw()
	
	def energy_down(self):
		if self.eiglevel > 1:
			self.eiglevel -= 1
		self.redraw()

		
	def redraw(self):
		self.ax.clear()
		self.ax.autoscale(enable=False)

		x = self.mesh['vertices'][:,0]
		y = self.mesh['vertices'][:,1]
		
		z = self.eigvecs[:,self.eiglevel]


		X = self.dom['vertices'][:,0]
		Y = self.dom['vertices'][:,1]
		outline = tri.Triangulation(X,Y)
		self.ax.triplot(outline)

		if self.nodes:
			self.ax.tricontour(x,y,z,0)
		else:
			self.ax.tricontourf(x,y,z,100,cmap=plt.get_cmap('copper'))

		self.canvas.draw()

if __name__ == '__main__':
	root = Tk()

	FEGui(root,600,600)

	root.mainloop()
