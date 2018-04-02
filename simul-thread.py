import time, sys
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QHBoxLayout, QSpinBox

class SimulRunner(QObject):

	stepIncreased = pyqtSignal(int, name='stepIncreased')
	def __init__(self):
		super().__init__()
		self._step = 0
		self._isRunning = True
		self._maxSteps = 20

	def longRunning(self):
		while self._step < self._maxSteps and self._isRunning == True:
			self._step += 1
			self.stepIncreased.emit(self._step)
			print('in longRunning: ', int(QThread.currentThreadId()))
			time.sleep(1)
			QApplication.processEvents()

	def stop(self):
		self._isRunning = False
		print('in stop method: ', int(QThread.currentThreadId()))

class MyThread(QThread):
	def run(self):
		self.exec_()


class SimulationUi(QDialog):
	def __init__(self):
		super().__init__()

		self.goButton = QPushButton('Go')
		self.stopButton = QPushButton('Stop')
		self.currentStep = QSpinBox()

		self.layout = QHBoxLayout()
		self.layout.addWidget(self.goButton)
		self.layout.addWidget(self.stopButton)
		self.layout.addWidget(self.currentStep)
		self.setLayout(self.layout)

		self.simulRunner = SimulRunner()
		self.simulThread = MyThread()
		self.simulRunner.moveToThread(self.simulThread)
		
		#self.stopButton.clicked.connect(self.simulThread.quit)
		self.stopButton.clicked.connect(self.simulRunner.stop)
		self.goButton.clicked.connect(self.simulThread.start)
		self.simulThread.started.connect(self.simulRunner.longRunning)
		self.simulRunner.stepIncreased.connect(self.currentStep.setValue)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	simul = SimulationUi()
	print('in main: ',  print(int(QThread.currentThreadId())))
	simul.show()
	sys.exit(app.exec_())
