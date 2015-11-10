import numpy as np
from scipy.special import *
import scipy.linalg as lin
import FE
from Tkinter import *
import triangle
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import sys

# GUI for a triangle explorer

class TriGUI:

	def __init__(self,root,canvas_width,canvas_height):
		self.root=root
		self.canvas_width = canvas_width
		self.canvas_height = canvas_height

		self.moduli_space = {'vertices':np.array([[0.,0.],[1.,0.],[0.5,np.sqrt(3.)/2.]]),'triangles':[0,1,2]}

		self.fig, self.ax = mpl.pyplot.subplots()
		self.ax.clear()
		self.ax.autoscale(enable=False)
		self.ax.axis('off')
		self.canvas = FigureCanvasTkAgg(self.fig,master=root)
		self.canvas.show()
		self.canvas.get_tk_widget().pack()

		X = self.moduli_space['vertices'][:,0]
		Y = self.moduli_space['vertices'][:,1]
		outline = tri.Triangulation(X,Y)
		self.ax.triplot(outline)

		#self.canvas.mpl_connect("button_press_event", self.setVertex)

	def quite(self):
		self.root.destroy()

class EigenfunctionGUI:

	def __init__(self,root,canvas_width,canvas_height,a,b,c):
		self.root=root
		self.canvas_width = canvas_width
		

if __name__ == '__main__':
	root = Tk()

	T = TriGUI(root,600,600)

	root.mainloop()

	T.quit()
