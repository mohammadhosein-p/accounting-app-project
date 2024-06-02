from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QLineEdit, QGridLayout, QPushButton, \
    QMessageBox, QRadioButton, QTextEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont, QPixmap
from git import *
import sys

app = QApplication(sys.argv)


class Category(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Category Form')
        self.setGeometry(700, 200, 550, 500)
        self.setFixedSize(500, 400)

        self.setStyleSheet("""
            QRadioButton {
                color: #E3FEF7;
                font-size: 20px;
                font-weight: bold;
                font-family: 'Times New Roman';
                spacing: 10px;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
            }
            QRadioButton::indicator:unchecked {
                border: 2px solid #E3FEF7;
                background-color: #003C43;
                border-radius: 10px;
            }
            QRadioButton::indicator:checked {
                border: 2px solid #77B0AA;
                background-color: #77B0AA;
                border-radius: 10px;
            }
            QWidget {
                background-color: #003C43;
            }
            QLabel {
                color: #E3FEF7;
            }
            QComboBox, QDateEdit {
                border: 3px solid #135D66;
                border-top-left-radius: 10px; border-bottom-left-radius: 10px;
                padding: 5px;
                background-color: #E3FEF7;
            }
            QLineEdit {
                border: 3px solid #135D66;
                border-radius: 10px;
                padding: 5px;
                background-color: #E3FEF7;
                font-size: 20px;
                font-weight: bold;
                font-family: 'Times New Roman';
            }
            QLineEdit:focus, QComboBox:focus, QDateEdit:focus {
                border: 3px solid red;
            }
            QTextEdit {
                border: 3px solid #135D66;
                border-radius: 10px;
                padding: 10px;
                background-color: #E3FEF7;
                font-size: 20px;
                font-weight: bold;
                font-family: 'Times New Roman';
            }
            QTextEdit:focus {
                border: 3px solid red;
            }
            QPushButton {
                background-color: #77B0AA;
                color: white;
                padding: 10px;
                text-align: center;
                margin: 4px 2px;
                border-radius: 10px;
                font-size: 20px;
                font-weight: bold;
                font-family: 'Times New Roman';
            }
            QPushButton:hover {
                background-color: #EEEEEE;
                color: #003C43;
            }
            QCalendarWidget QToolButton {
                background-color: #003C43;
                color: #003C43;
                border: none;
                border-radius: 5px;
                padding: 5px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #003C43;
                color: #003C43;
            }
            QCalendarWidget QWidget {
                background-color: #003C43;
            }
            QCalendarWidget QAbstractItemView:enabled {
                color: #003C43;
                background-color: #E3FEF7;
                selection-background-color: #77B0AA;
                selection-color: #FFFFFF;
            }
        """)

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
        # نام کاربری تغییر داده شود
        result = category_manager.add_category("username", self.title_line_edit.text(),
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
            QMessageBox.information(self, "success", "category found successfuly")
        else:
            QMessageBox.warning(self, "Error", "there was an error")


if __name__ == "__main__":
    window = Category()
    data_manager = DataManager()
    category_manager = CategoryManager(data_manager)
    window.show()
    sys.exit(app.exec())
