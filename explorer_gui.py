import numpy as np
from scipy.special import *
import scipy.linalg as lin
import FE
import Tkinter as Tk
import triangle
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import sys

class Explorer:
	
	def __init__(self,root,canvas_width,canvas_height):

		self.root = root
		self.canvas_width = canvas_width
		self.canvas_height = canvas_height

		# these methods set up the gui
		self.fig, self.ax = mpl.pyplot.subplots()
		self.ax.clear()
		self.ax.autoscale(enable=False)
		self.ax.axis('off')
		self.canvas = FigureCanvasTkAgg(self.fig,master=root)
		self.canvas.show()
		self.canvas.get_tk_widget().pack()

		# these flags govern the current state		
		self.currently_drawing = False		# flag if currently drawing a domain
		self.display_mesh = False			# flag if displaying mesh instead of func
		
		self.domain = {'vertices':np.array([[0.,0.],[1.,0.7],[0.5,0.5]])}
		self.mesh = triangle.triangulate(self.dom,'qa0.0001')

		self.mouse_clicks = []
		
	def newDomain(self,vertex_list):
		self.domain = triangle.convex_hull({'vertices':np.array(vertex_list)})


	def plotCurrentDomain(self):
		

	


	def _quit():
		root.quit()
		root.destroy()

if __name__ == '__main__':

