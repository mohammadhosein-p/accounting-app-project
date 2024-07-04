from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QLineEdit, QGridLayout, QPushButton, \
    QMessageBox, QRadioButton, QTextEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont, QIcon
from modules.data_manager_class import *
import sys

app = QApplication(sys.argv)


class Category(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Category Form')
        self.setWindowIcon(QIcon('../source/growth.png'))
        self.setGeometry(700, 200, 550, 500)
        self.setFixedSize(500, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.grid = QGridLayout(central_widget)

        self.grid.setContentsMargins(20, 20, 20, 20)
        self.grid.setSpacing(10)

        self.insert_radiobtn = QRadioButton("Insert", self)
        self.grid.addWidget(self.insert_radiobtn, 0, 1)

        self.find_radiobtn = QRadioButton("Find", self)
        self.grid.addWidget(self.find_radiobtn, 0, 2)

        self.edit_radiobtn = QRadioButton("Edit", self)
        self.grid.addWidget(self.edit_radiobtn, 0, 3)

        self.title_line_edit = QLineEdit(self)
        self.grid.addWidget(self.title_line_edit, 1, 1, 1, 3)
        self.title_label = QLabel("category title: ", self)
        self.title_label.setFont(QFont('Times New Roman', 12))
        self.grid.addWidget(self.title_label, 1, 0)

        self.describtion_text_edit = QTextEdit(self)
        self.grid.addWidget(self.describtion_text_edit, 2, 1, 2, 3)
        self.discribtion_label = QLabel("discribtion: ", self)
        self.discribtion_label.setFont(QFont('Times New Roman', 12))
        self.grid.addWidget(self.discribtion_label, 2, 0)

        self.find_btn = QPushButton("Find", self)
        self.find_btn.setVisible(False)
        self.grid.addWidget(self.find_btn, 4, 2)

        self.insert_btn = QPushButton("Insert", self)
        self.insert_btn.setVisible(False)
        self.grid.addWidget(self.insert_btn, 4, 1)

        self.edit_btn = QPushButton("Edit", self)
        self.edit_btn.setVisible(False)
        self.grid.addWidget(self.edit_btn, 4, 3)

        self.back_btn = QPushButton("Back", self)
        self.grid.addWidget(self.back_btn, 5, 0, 1, 4)

        self.grid.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding), 5, 0, 1, 3)

        self.insert_btn.clicked.connect(self.insert_data)
        self.find_btn.clicked.connect(self.find_data)
        self.edit_btn.clicked.connect(self.edit_data)

        self.insert_radiobtn.toggled.connect(self.insert_mode)
        self.find_radiobtn.toggled.connect(self.find_mode)
        self.edit_radiobtn.toggled.connect(self.edit_mode)

    def insert_mode(self):
        self.find_btn.setVisible(False)
        self.insert_btn.setVisible(True)
        self.edit_btn.setVisible(False)
        self.describtion_text_edit.setReadOnly(False)

    def find_mode(self):
        self.insert_btn.setVisible(False)
        self.find_btn.setVisible(True)
        self.edit_btn.setVisible(False)
        self.describtion_text_edit.setReadOnly(True)

    def edit_mode(self):
        self.find_btn.setVisible(False)
        self.insert_btn.setVisible(False)
        self.edit_btn.setVisible(True)
        self.describtion_text_edit.setReadOnly(False)

    def insert_data(self):
        result = category_manager.add_category(self.current_user, self.title_line_edit.text(),
                                               self.describtion_text_edit.toPlainText())
        if result['result']:
            QMessageBox.information(self, "success", "category added successfuly")
        else:
            QMessageBox.warning(self, "Error", "there was an error")

    def find_data(self):
        result = category_manager.find_category(self.title_line_edit.text())
        if result['result']:
            self.describtion_text_edit.setText(result["data"][2])
            QMessageBox.information(self, "success", "category found successfuly")
        else:
            QMessageBox.warning(self, "Error", "there was an error")

    def edit_data(self):
        result = category_manager.edit_category(self.title_line_edit.text(), self.describtion_text_edit.toPlainText())
        if result['result']:
            QMessageBox.information(self, "success", "category edited successfuly")
        else:
            QMessageBox.warning(self, "Error", "there was an error")
 
    def set_current_user(self, user):
        self.current_user = user

if __name__ == "__main__":
    window = Category()
    data_manager = DataManager()
    category_manager = CategoryManager(data_manager)
    window.show()
    sys.exit(app.exec())
