import time, sys
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot, QTimer, Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QHBoxLayout, QSpinBox, QWidget

class Worker(QObject):
	stepIncreased = pyqtSignal(int, name='stepIncreased')
	def __init__(self):
		super().__init__()
		# QTimer 생성시, self 넣어야 동작함.
		self.timer = QTimer(self)
		self.timer.setInterval(1000)
		self.timer.timeout.connect(self.porcess)
		self._isRunning = True
		self._step = 0

	@pyqtSlot()
	def start(self):
		self.timer.start()

	@pyqtSlot()
	def stop(self):
		self.timer.stop()


	@pyqtSlot()
	def porcess(self):
		self._step += 1
		self.stepIncreased.emit(self._step)
		print(self._step)

class MyThread(QThread):
	def run(self):
		self.exec()


class MyWindow(QWidget):
	def __init__(self):
		super().__init__()

		self.timer = QTimer()
		self.goButton = QPushButton('Go')
		self.stopButton = QPushButton('Stop')
		self.currentStep = QSpinBox()

		self.layout = QHBoxLayout()
		self.layout.addWidget(self.goButton)
		self.layout.addWidget(self.stopButton)
		self.layout.addWidget(self.currentStep)
		self.setLayout(self.layout)

		self.worker = Worker()
		self.worker_thread = MyThread()
		self.worker.moveToThread(self.worker_thread)
		
		self.goButton.clicked.connect(self.worker.start, Qt.QueuedConnection)
		#self.timer.timeout.connect(self.worker.porcess)
		self.stopButton.clicked.connect(self.worker.stop)

		self.worker.stepIncreased.connect(self.currentStep.setValue)

		self.worker_thread.start()

	def timerStart(self):
		print('timer started!')
		self.timer.start(1000)

	def timerStop(self):
		self.timer.stop()
		print('timer stopped!')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	mywin = MyWindow()
	
	mywin.show()
	sys.exit(app.exec_())
