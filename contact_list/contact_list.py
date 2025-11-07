"""The module defines the ContactList class."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Sukhpreet Kaur"

from PySide6.QtWidgets import  (QMainWindow, QLineEdit, QPushButton,
                                QTableWidget, QLabel, QVBoxLayout, 
                                QWidget, QTableWidgetItem)
from PySide6.QtCore import Slot

class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts."""

    def __init__(self):
        """Initializes a new instance of the ContactList class."""

        super().__init__()
        self.__initialize_widgets()  
        self.add_button.clicked.connect(self.__on_add_contact)      

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.
        
        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot()
    def __on_add_contact(self):

        """This will handle the add contact button click event"""

        name = self.contact_name_input.text().strip()
        phone = self.phone_input.text().strip()

        if len(name) > 0 and len(phone) > 0:
            row_position = self.contact_table.rowCount()
            self.contact_table.insertRow(row_position)
            name_item = QTableWidgetItem(name)
            self.contact_table.setItem(row_position, 0,
                                        QTableWidgetItem(name_item))
            phone_item = QTableWidgetItem(phone)
            self.contact_table.setItem(row_position, 1,
                                    QTableWidgetItem(phone_item))

            self.status_label.setText(f"Added contact: {name}")
            self.contact_name_input.clear()
            self.phone_input.clear()
        else:
            self.status_label.setText(f"Please enter a contact "
                                      f"name and phone number.")

