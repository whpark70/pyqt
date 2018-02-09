import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine



def main():
	app = QApplication(sys.argv)
	engine = QQmlApplicationEngine()
	engine.load("test.qml")
	engine.quit.connect(app.quit)
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
