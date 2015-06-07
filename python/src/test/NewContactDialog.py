from PyQt5.QtWidgets import (QDialog)

class NewContactDialog(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.initComponent()
	def initComponent(self):
		self.resize(500, 400)
	