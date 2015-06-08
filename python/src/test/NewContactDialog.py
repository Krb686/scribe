from PyQt5.QtWidgets import (QDialog, QLineEdit, QLabel, QPushButton, QFormLayout, QGroupBox, QHBoxLayout, QGridLayout)
#from PyQt5.QtGui import ()

class NewContactDialog(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.initComponent()
	def initComponent(self):
		
		
		# Components
		
		# == Name ==
		nameGroupBox = QGroupBox("Name")
		firstNameBox = QLineEdit()
		firstNameLabel = QLabel("First:")
		middleNameBox = QLineEdit()
		middleNameLabel = QLabel("Middle:")
		lastNameBox = QLineEdit()
		lastNameLabel = QLabel("Last:")
		
		nameLayout = QHBoxLayout()
		nameLayout.addWidget(firstNameLabel)
		nameLayout.addWidget(firstNameBox)
		
		nameLayout.addWidget(middleNameLabel)
		nameLayout.addWidget(middleNameBox)
		
		nameLayout.addWidget(lastNameLabel)
		nameLayout.addWidget(lastNameBox)
		
		nameGroupBox.setLayout(nameLayout)
		
		# == Phone ==
		phoneGroupBox = QGroupBox("Phone")
		
		phoneBox = QLineEdit()
		phoneLabel = QLabel("Phone:")
		
		phoneLayout = QHBoxLayout()
		phoneLayout.addWidget(phoneLabel)
		phoneLayout.addWidget(phoneBox)
		
		phoneGroupBox.setLayout(phoneLayout)
		
		# == Address ==
		addressBox = QLineEdit()
		addressLabel = QLabel("Address:")
		
		submitButton = QPushButton("Submit")
		
		
		dialogLayout = QGridLayout()
		
		dialogLayout.addWidget(nameGroupBox, 0, 0)
		dialogLayout.addWidget(phoneGroupBox, 1, 0)
		dialogLayout.addWidget(submitButton)
		#layout.addRow(phoneLabel, phoneBox)
		#layout.addRow(addressLabel, addressBox)
		
		
		
		self.setLayout(dialogLayout)
		self.resize(400, 100)
		