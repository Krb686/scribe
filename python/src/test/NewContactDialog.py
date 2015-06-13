from PyQt5.QtWidgets import (QDialog, QLineEdit, QLabel, QPushButton, QFormLayout, QGroupBox, QHBoxLayout, QGridLayout)
#import weakref

class NewContactDialog(QDialog):
	def __init__(self, parent):
		QDialog.__init__(self)
		self.parent = parent
		self.initComponent()
		
	def initComponent(self):
		
		# Components
		
		# == Name ==
		nameGroupBox = QGroupBox("Name")
		self.firstNameBox = QLineEdit()
		firstNameLabel = QLabel("First:")
		self.middleNameBox = QLineEdit()
		middleNameLabel = QLabel("Middle:")
		self.lastNameBox = QLineEdit()
		lastNameLabel = QLabel("Last:")
		
		nameLayout = QHBoxLayout()
		nameLayout.addWidget(firstNameLabel)
		nameLayout.addWidget(self.firstNameBox)
		
		nameLayout.addWidget(middleNameLabel)
		nameLayout.addWidget(self.middleNameBox)
		
		nameLayout.addWidget(lastNameLabel)
		nameLayout.addWidget(self.lastNameBox)
		
		nameGroupBox.setLayout(nameLayout)
		
		# ======== Phone ========
		# =======================
		phoneGroupBox = QGroupBox("Phone")
		
		self.phoneBox = QLineEdit()
		phoneLabel = QLabel("Phone:")
		
		phoneLayout = QHBoxLayout()
		phoneLayout.addWidget(phoneLabel)
		phoneLayout.addWidget(self.phoneBox)
		
		phoneGroupBox.setLayout(phoneLayout)
		
		# ======== Address ========
		# =========================
		addressGroupBox = QGroupBox("Address")
		
		self.addressBox = QLineEdit()
		addressLabel = QLabel("Address:")
		
		addressLayout = QHBoxLayout()
		addressLayout.addWidget(addressLabel)
		addressLayout.addWidget(self.addressBox)
		
		addressGroupBox.setLayout(addressLayout)
		
		# == Submit  Button ==
		
		submitButton = QPushButton("Submit")
		submitButton.clicked.connect(self.submitNewContact)
		
		
		dialogLayout = QGridLayout()
		
		dialogLayout.addWidget(nameGroupBox, 0, 0)
		dialogLayout.addWidget(phoneGroupBox, 1, 0)
		dialogLayout.addWidget(addressGroupBox, 2, 0)
		dialogLayout.addWidget(submitButton)
		
		self.setLayout(dialogLayout)
		self.resize(400, 100)
		
	def submitNewContact(self):
		first = self.firstNameBox.text()
		middle = self.middleNameBox.text()
		last = self.lastNameBox.text()
		
		name = first+middle+last
		phone = self.phoneBox.text()
		address = self.addressBox.text()
		
		self.parent.addItem(self.parent.itemModel, name, phone, address)
		self.close()