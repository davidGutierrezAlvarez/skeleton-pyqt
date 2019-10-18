import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow, QMessageBox,
							QPushButton, QLabel,QTableWidgetItem,
							QAbstractItemView)
from PyQt5.QtGui import QIcon, QColor
from PyQt5 import QtWidgets, QtCore #,QtGui
from PyQt5.uic import loadUi



class main(QMainWindow):
	color = QColor(228,30,94)
	def __init__(self):
		super().__init__()
		loadUi('skeleton.ui', self)

		#eliminar bordes
		#flags = QtCore.Qt.WindowFlags(QtCore.Qt.CustomizeWindowHint)
		#self.setWindowFlags(flags)#
		#pantalla completa
		#QtWidgets.QMainWindow.showFullScreen(self)
		self.mode_active = True
		with open("css/stylesheet.css") as f:
			self.setStyleSheet(f.read())

		self.btn_1.clicked.connect(self.accion)
		self.btn_2.clicked.connect(self.accion)
		self.btn_3.clicked.connect(self.accion)
		self.btn_4.clicked.connect(self.accion)
		self.btn_5.clicked.connect(self.accion)
		self.btn_6.clicked.connect(self.accion)
		self.btn_7.clicked.connect(self.accion)

		self.nocturno.clicked.connect(self.mode)

	def accion(self):
		btn = self.sender().objectName()
		#objtengo el nombre de los botones
		#recojo su valor numerico con btn[-1]
		#lo convierto de string a int
		#con esto selcciono el tab
		self.tabWidget.setCurrentIndex(int(btn[-1])-1)

		#dar color
		if self.mode_active:
			self.sender().setStyleSheet("background-color: #2271b3")
		else:
			self.sender().setStyleSheet("background-color: #d081d8")
		try:
			#quitar color al anterior, si hay un anterior
			self.ultimo.setStyleSheet("background-color: none")
		except Exception:
			pass
		self.ultimo = self.sender()

	def mode(self):
		if self.mode_active:
			with open("css/nocturno.css") as f:
				self.setStyleSheet(f.read())
			self.ultimo.setStyleSheet("background-color: #d081d8")
			self.mode_active = False
			
		else:
			with open("css/stylesheet.css") as f:
				self.setStyleSheet(f.read())
			self.ultimo.setStyleSheet("background-color: #2271b3")
			self.mode_active = True

if __name__ == "__main__":
	app = QApplication(sys.argv)
	GUI = main()
	#GUI.setStyleSheet("background-color:white;")
	GUI.show()
	sys.exit(app.exec_())
