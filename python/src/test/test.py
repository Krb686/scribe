#Imports
import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QMenuBar, QMenu, QVBoxLayout, QWidget, QToolBar, QMainWindow, QAction)
from PyQt5.QtGui import (QIcon)

# TestWidget Class
class ScribeMainWindow(QMainWindow):
	def __init__(self):
		super(ScribeMainWindow, self).__init__()
		
		self.initUI()
		
	# Initialize UI
	def initUI(self):
	
		# Geometry
		self.setGeometry(640, 300, 1280, 960)
		
		#Text
		self.setWindowTitle('Scribe')
		self.setWindowIcon(QIcon('./icons/blue_scroll.ico'))
		
		
		# ==== Create Menus ====
		# ======================
		menuBar = self.menuBar()
		
		
		# File Menu
		fileMenu = menuBar.addMenu('&File')
		
		openAction = QAction(QIcon('./icons/tan_folder.ico'), "&Open", self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip('Open file...')
		openAction.triggered.connect(self.openDialog)
		
		saveAction = QAction(QIcon('./icons/blue_floppy.ico'), "&Save", self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setStatusTip('Save current file.')
		saveAction.triggered.connect(self.saveFile)
		
		saveAsAction = QAction("Save As", self)
		saveAsAction.setStatusTip("Save as...")
		saveAction.triggered.connect(self.saveFileAs)
	
		exitAction = QAction(QIcon('./icons/red_x.ico'), '&Exit', self)        
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(QApplication.quit)
		
		fileMenu.addAction(openAction)
		fileMenu.addAction(saveAction)
		fileMenu.addAction(saveAsAction)
		fileMenu.addAction(exitAction)
		fileMenu.insertSeparator(saveAction)
		fileMenu.insertSeparator(exitAction)
		
		
		# Edit Menu
		editMenu = menuBar.addMenu("&Edit")
		
		
		# Help Menu
		helpMenu = menuBar.addMenu("&Help")
		
		aboutAction = QAction(QIcon('./icons/paper_folded.ico'), '&About', self)
		aboutAction.triggered.connect(self.helpDialog)
		
		helpMenu.addAction(aboutAction)
		
		self.statusBar()
		self.show()
		
	def openDialog(self):
		pass
		
	def saveFile(self):
		pass
		
	def saveFileAs(self):
		pass
	def helpDialog(self):
		helpDialog = QDialog()
		helpDialog.resize(300, 300)
		helpDialog.setWindowTitle("About")
		helpDialog.exec_()
		
	# Exit
	def exitApp(self):
		sys.exit(0)
		
		
if __name__ == '__main__':

	app = QApplication(sys.argv)
	SMW = ScribeMainWindow()
	sys.exit(app.exec_())