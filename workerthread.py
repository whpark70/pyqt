import sys, time
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel



class Worker(QObject):

	sig_numbers = pyqtSignal(int, name='sig_numbers')
	finished = pyqtSignal()
		
	def __init__(self, parent=None):
		super().__init__(parent)
		self.Running = True
		self.sum = 0

	@pyqtSlot()
	def stop(self):
		self.Running = False

	def isRunning(self):
		return self.Running
		
	@pyqtSlot()
	def process(self):

		while self.isRunning():
			self.sum += 1
			print(self.sum)
			self.sig_numbers.emit(self.sum)
			time.sleep(1)
		self.finished.emit()
		'''
		_cnt = 0
		while _cnt < 10:
			_cnt += 1
			print(_cnt)
			self.sig_numbers.emit(_cnt)
			time.sleep(1)
		'''

class MyWindow(QWidget):

	def __init__(self):
		super().__init__()
		
		self.startBtn = QPushButton("Start",self)
		self.cancelBtn = QPushButton("Cancel", self)
		self.label = QLabel('status', self)
		layout = QVBoxLayout(self)
		layout.addWidget(self.startBtn)
		layout.addWidget(self.cancelBtn)
		layout.addWidget(self.label)

		self.setFixedSize(400, 200)

	@pyqtSlot(int)
	def updateStatus(self, status):
		self.label.setText('{}'.format(status))



class Example(QObject):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.gui = MyWindow()

		self.worker = Worker()
		self.thread = QThread()
		self.worker.moveToThread(self.thread)
		self.thread.start()

		self._connectSignal()

		self.gui.show()


	def _connectSignal(self):
		self.gui.startBtn.clicked.connect(self.worker.process)
		self.worker.sig_numbers.connect(self.gui.updateStatus)
		self.gui.cancelBtn.clicked.connect(self.forceWorkerReset)
		''''
		#self.gui.cancelBtn.clicked.connect(self.worker.stop)			# fail
		self.gui.cancelBtn.clicked.connect(self.workerStop)				# 직접적인 stop.
		
		self.worker.finished.connect(self.thread.quit)
		self.worker.finished.connect(self.worker.deleteLater)
		self.worker.finished.connect(self.thread.deleteLater)
		self.worker.finished.connect(self.finished)
		'''

	def forceWorkerReset(self):
		if self.thread.isRunning():
			self.thread.terminate()
			self.thread.wait()
			self.thread.start()

	def workerStop(self):
		self.worker.stop()
		
	def finished(self):
		print('thread finished')



if __name__ == '__main__':
	app = QApplication(sys.argv)
	example= Example(app)

	sys.exit(app.exec_())
			
