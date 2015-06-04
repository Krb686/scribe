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

		
		#Menu
		self.menuBar = QMenuBar()
		self.fileMenu = QMenu("&File", self)
		self.exitAction = self.fileMenu.addAction("E&xit")
		self.exitAction.triggered.connect(self.exitApp)
		self.menuBar.addMenu(self.fileMenu)
		
		
		#Layout
		layout = QVBoxLayout()
		layout.setMenuBar(self.menuBar)

		self.setLayout(layout)
		self.show()
		
	# Exit
	def exitApp(self):
		sys.exit(0)
		
		
if __name__ == '__main__':

	app = QApplication(sys.argv)
	testWidget = TestWidget()
	sys.exit(app.exec_())