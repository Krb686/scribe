#Imports
import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QMenuBar, QMenu, QVBoxLayout, QWidget)
from PyQt5.QtGui import (QIcon)

# TestWidget Class
class TestWidget(QWidget):
	def __init__(self):
		super(TestWidget, self).__init__()
		
		self.initUI()
		
	# Initialize UI
	def initUI(self):
		
		#Geometry
		self.setGeometry(640, 300, 640, 480)
		
		#Text
		self.setWindowTitle('Scribe')
		self.setWindowIcon(QIcon('sparrow.ico'))

		
		# ==== Create Menus ====
		# ======================
		
		self.menuBar = QMenuBar()
		
		# File Menu
		self.fileMenu = QMenu("&File", self)
		self.exitAction = self.fileMenu.addAction("E&xit")
		self.exitAction.triggered.connect(self.exitApp)
		self.menuBar.addMenu(self.fileMenu)
		
		# Edit Menu
		self.editMenu = QMenu("&Edit", self)
		self.menuBar.addMenu(self.editMenu)
		
		# Help Menu
		self.helpMenu = QMenu("&Help", self)
		self.aboutAction = self.helpMenu.addAction("&About")
		self.aboutAction.triggered.connect(self.openHelp)
		self.menuBar.addMenu(self.helpMenu)
		
		
		#Layout
		layout = QVBoxLayout()
		layout.setMenuBar(self.menuBar)

		self.setLayout(layout)
		self.show()
		
	def openHelp(self):
		helpDialog = QDialog()
		helpDialog.resize(300, 300)
		helpDialog.setWindowTitle("About")
		helpDialog.exec_()
		
	# Exit
	def exitApp(self):
		sys.exit(0)
		
		
if __name__ == '__main__':

	app = QApplication(sys.argv)
	testWidget = TestWidget()
	sys.exit(app.exec_())