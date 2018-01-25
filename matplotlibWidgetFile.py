from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
	def __init__(self):
		self.fig = Figure(figsize=(5,3))
		self.ax = self.fig.add_subplot(111)

		super().__init__(self.fig)
		#self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		self.updateGeometry()

class PlotWidget(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.canvas = MplCanvas()
		self.vbl = QVBoxLayout()
		self.vbl.addWidget(self.canvas)
		self.setLayout(self.vbl)

#class serverCanvas(FigureCanvas):