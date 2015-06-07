#Imports
import sys
from PyQt5.QtWidgets import *
#from PyQt5.QtWidgets import (QApplication, QDialog, QMenuBar, QMenu, QVBoxLayout, QWidget, QToolBar, QMainWindow, QAction, QTreeView, QHBoxLayout)
from PyQt5.QtGui import (QIcon, QStandardItemModel)

from PyQt5.QtCore import *

# TestWidget Class
class ScribeMainWindow(QMainWindow):
	def __init__(self):
		super(ScribeMainWindow, self).__init__()
		
		self.initUI()
		
	# Initialize UI
	def initUI(self):
	
		# Geometry
		self.setGeometry(448, 156, 1024, 768)
		
		#Text
		self.setWindowTitle('Scribe')
		self.setWindowIcon(QIcon('./icons/blue_scroll.ico'))
		
		self.setDockNestingEnabled(False)
		# ======== Create Menus ========
		# ==============================
		menuBar = self.menuBar()
		
		
		# File Menu
		fileMenu = menuBar.addMenu('&File')
		
		newAction = QAction(QIcon('./icons/paper_blank.ico'), "New", self)
		newAction.setShortcut('Ctrl+N')
		newAction.setStatusTip('Create a new contact...')
		newAction.triggered.connect(self.debugPrint)
		
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
		
		fileMenu.addAction(newAction)
		fileMenu.addAction(openAction)
		fileMenu.addAction(saveAction)
		fileMenu.addAction(saveAsAction)
		fileMenu.addAction(exitAction)
		fileMenu.insertSeparator(saveAction)
		fileMenu.insertSeparator(exitAction)
		
		
		# Edit Menu
		editMenu = menuBar.addMenu("&Edit")
		
		settingsAction = QAction(QIcon('./icons/blue_gear.ico'), "Settings", self)
		
		editMenu.addAction(settingsAction)
		
		# Tools Menu
		toolsMenu = menuBar.addMenu("Tools")
		
		
		
		# Help Menu
		helpMenu = menuBar.addMenu("&Help")
		
		aboutAction = QAction(QIcon('./icons/paper_folded.ico'), '&About', self)
		aboutAction.triggered.connect(self.helpDialog)
		
		helpMenu.addAction(aboutAction)
		
		# ======== Create Toolbar ======
		# ==============================
		toolBar = QToolBar(self)
		toolBar.setWindowTitle("Action Bar")
		toolBar.setMovable(False)
		toolBar.addAction(newAction)
		toolBar.addAction(openAction)
		toolBar.addAction(saveAction)
		toolBar.addSeparator()
		toolBar.addAction(settingsAction)
		self.addToolBar(toolBar)
		self.addToolBarBreak()
		
		
		self.navBar = QToolBar(self)
		self.navBar.setWindowTitle("Navigation Bar")
		self.navBar.setMovable(False)
		
		buttonGroup = QButtonGroup()
		
		addressBookButton = QPushButton(QIcon('./icons/blue_binder.ico'), "Address Book", self)
		addressBookButton.setFlat(True)
		addressBookButton.setCheckable(True)
		addressBookButton.setChecked(True)
		addressBookButton.setAutoExclusive(True)
		buttonGroup.addButton(addressBookButton)
		self.navBar.addWidget(addressBookButton)
		self.navBar.addSeparator()
		
		invoicesButton = QPushButton(QIcon('./icons/paper_folded_bullets.ico'), "Invoices", self)
		invoicesButton.setFlat(True)
		invoicesButton.setCheckable(True)
		invoicesButton.setAutoExclusive(True)
		buttonGroup.addButton(invoicesButton)
		self.navBar.addWidget(invoicesButton)
		self.navBar.addSeparator()
		
		paymentsButton = QPushButton(QIcon('./icons/green_dollar_sign.ico'), "Payments", self)
		paymentsButton.setFlat(True)
		paymentsButton.setCheckable(True)
		paymentsButton.setAutoExclusive(True)
		buttonGroup.addButton(paymentsButton)
		self.navBar.addWidget(paymentsButton)
		self.navBar.addSeparator()
		
		syncButton = QPushButton(QIcon('./icons/green_blue_sync.ico'), "Sync", self)
		syncButton.setFlat(True)
		syncButton.setCheckable(True)
		syncButton.setAutoExclusive(True)
		buttonGroup.addButton(syncButton)
		self.navBar.addWidget(syncButton)
		self.navBar.addSeparator()
		
		
		self.addToolBar(Qt.TopToolBarArea, self.navBar)
		
		
		
		# ======== Create Statusbar ======
		# ==============================
		self.statusBar()
		
		
		
		# == Main widget
		self.itemList = QTableView()
		self.itemList.setAlternatingRowColors(True)
		self.itemList.setContextMenuPolicy(Qt.CustomContextMenu)
		self.itemList.customContextMenuRequested.connect(self.addressContextDialog)
		
		itemModel = self.createModel()
		
		self.addItem(itemModel, "John Smith", "(517)-286-1273", "1234 Mainstreet Lane")
		self.addItem(itemModel, "Melissa King", "(517)-743-2217", "1312 Sunnybrook Road")
		#self.addItem(itemModel, "Kevin", "1/2/34", "1234 Mainstreet Lane")
		#self.addItem(itemModel, "Kevin", "1/2/34", "1234 Mainstreet Lane")
		
		self.itemList.setModel(itemModel)
		
		
		
		# Layout
		self.setCentralWidget(self.itemList)
		
		
		
		
		self.show()
		
	def addressContextDialog(self, point):
	
		
		# Create the context menu widget
		self.addressContextMenu = QMenu()
		self.addressContextMenu.resize(200, 100)
		
		# Create the actions for the menu
		newContactAction = QAction(QIcon('./icons/green_plus.ico'), "Create new contact", self.addressContextMenu)
		
		
		self.addressContextMenu.addAction(newContactAction)
		self.addressContextMenu.show()
		
		
		itemListOffset_x = self.itemList.pos().x()
		itemListOffset_y = self.itemList.pos().y()
		
		windowOffset_x = self.pos().x()
		windowOffset_y = self.pos().y()
		
		totalOffset_x = itemListOffset_x + windowOffset_x + 20
		totalOffset_y = itemListOffset_y + windowOffset_y + 50
		
		
		
		targetPoint = QPoint(point.x()+totalOffset_x, point.y()+totalOffset_y)
		print(targetPoint)
		
		
		self.addressContextMenu.move(targetPoint)
		
		
	def newContactDialog(self):
		debugPrint()
		
	def openDialog(self):
		pass
		
	def saveFile(self):
		pass
		
	def saveFileAs(self):
		pass
		
	def debugPrint(self):
		print(self.toolBarArea(self.navBar))
		
	def createModel(self):
		model = QStandardItemModel(0, 3)
		
		model.setHeaderData(0, Qt.Horizontal, "Name")
		model.setHeaderData(1, Qt.Horizontal, "Phone")
		model.setHeaderData(2, Qt.Horizontal, "Address")
		
		return model
		
		
	def addItem(self, model, name, phone, address):
		model.insertRow(0)
		model.setData(model.index(0, 0), name)
		model.setData(model.index(0, 1), phone)
		model.setData(model.index(0, 2), address)
		
		
		
		
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