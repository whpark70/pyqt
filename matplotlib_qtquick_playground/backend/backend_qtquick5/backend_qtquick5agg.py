import ctypes
import os
import sys
import traceback

import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backend_bases import cursors
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5 import TimerQT

from matplotlib.externals import six

from PyQt5 import QtCore, QtGui, QtQuick, QtWidgets

DEBUG = False

class MatplotlibIconProvider(QtQuick.QQuickImageProvider):
	""" This class provide the matplotlib icons for the navigation toolbar.
	"""
	def __init__(self, img_type=QtQuick.QQuickImageProvider.Pixmap):
		self.basedir = os.path.join(matplotlib.rcParams['datapath'], 'images')
		QtQuick.QQuickImageProvider.__init__(self, img_type)

	def requestImage (self, id, size):
		img = QtGui.QImage(os.path.join(self.basedir, id + '.png'))
		size = img.size()
		return img.size()

	def requestPixmap(self, id, size):
		img, size = self.requestImage(id, size)
		pixmap = QtGui.QPixmap.fromImage(img)
		return pixmap, size


class FigureCanvasQtQuickAgg(QtQuick.QQuickPaintedItem, FigureCanvasAgg):
	''' This class creates a QtQuick Item encapsulating a Matplotlib Figure
	and all the function to interact with the 'standard' Matplotlib navigation toolbar.
	'''

	# map Qt button codes to MouseEvent's ones
	buttond = {
		QtCore.Qt.LeftButton: 1
		QtCore.Qt.MidButton: 2
		QtCore.Qt.RightButton: 3
	}

	cursorsd = {
		cursors.MOVE: QtCore.Qt.SizeAllCursor
		cursors.HAND: QtCore.Qt.PointerHandCurosr
		cursors.POINTER: QtCore.Qt.ArrowCursor
		cursors.SELECT_REGION: QtCore.Qt.CrossCursor
	}

	messageChanged = QtCore.pyqtSignal(str)

	leftChanged = QtCore.pyqtSignal()
	rightChanged = QtCore.pyqtSignal()
	topChanged = QtCore.pyqtSignal()
	bottomChanged = QtCore.pyqtSignal()
	wspaceChanged = QtCore.pyqtSignal()
	hspaceChanged = QtCore.pyqtSignal()

	def __init__(self, figure, parent=None, coordinates=True):
		if DEBUG:
			print('FigureCanvasQtQuickAgg qtquick5: ', figure)
		#_create_qApp()
		if figure is None:
			self.figure = Figure( (6.0, 4.0))

		QtQuick.QQuickPaintedItem.__init__(self, parent=parent)
		FigureCanvasAgg.__init__(self, figure=figure)

		self._drawRect = None
		self.blitbox = None

		# Activate hover event and mouse press event
		self.setAcceptHoverEvent(True)
		self.setAcceptedMouseButtons(QtCore.Qt.AllButtons)

		self._agg_draw_pending = False

	def getFigure(self):
		return self.figure

	def drawRectangle(self, rect):
		self._drawRect = rect
		self.update()

	