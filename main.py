import sys
from PlotGUI import *
import random

class GUIForm(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.PlotFunc)

	def PlotFunc(self):
		randomNumbers = random.sample(range(0,10), 10)
		self.ui.widget.canvas.ax.clear()
		self.ui.widget.canvas.ax.plot(randomNumbers)
		self.ui.widget.canvas.draw()

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = GUIForm()
	myapp.show()
	sys.exit(app.exec_())
