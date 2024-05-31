import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
import git


class ButtonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Setting')
        self.setWindowIcon(QIcon('setting.png'))
        self.setFixedSize(400, 500)

        self.button1 = QPushButton('Change the theme')
        self.button1.clicked.connect(self.handle_Change_the_theme)
        self.button2 = QPushButton('Delete account')
        self.button2.clicked.connect(self.handle_Delete_account)
        self.button3 = QPushButton('editing information')
        self.button3.clicked.connect(self.handle_editing_information)
        self.button4 = QPushButton('excavating information')
        self.button4.clicked.connect(self.handle_excavating_information)
        self.button5 = QPushButton('Delete income')
        self.button5.clicked.connect(self.handle_Delete_income)
        self.button6 = QPushButton('Delete expense')
        self.button6.clicked.connect(self.handle_Delete_expense)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.button1)
        main_layout.addWidget(self.button2)
        main_layout.addWidget(self.button3)
        main_layout.addWidget(self.button4)
        main_layout.addWidget(self.button5)
        main_layout.addWidget(self.button6)
        main_layout.setSpacing(15)

        self.setLayout(main_layout)

        self.apply_stylesheet()

    def apply_stylesheet(self):
        self.setStyleSheet("""
            QWidget {
                background: #003C43;
                color: #E3FEF7;
                font-family: 'Arial';
                font-size: 14px;
            }
            QPushButton {
                background-color: #77B0AA;
                color: white;
                padding: 10px;
                border-radius: 15px;
                font-size: 24px;
                font-family: 'Times New Roman';
                box-shadow: 2px 2px 5px #000000;
                margin: 5px 20px;
            }
            QPushButton:hover {
                background-color: #E3FEF7;
                color: #003C43;
                border: 2px solid #77B0AA;
            }
        """)

    def handle_Change_the_theme(self):
        pass

    def handle_Delete_account(self):
        git.accounting_manager.delete_account("mehdi")
        QMessageBox.information(self, 'Success', 'goodbye')

    def handle_editing_information(self):
        pass

    def handle_excavating_information(self):
        pass

    def handle_Delete_income(self):
        git.accounting_manager.delete_records("mehdi", "income")
        QMessageBox.information(self, 'Success', 'Your revenue transactions have been deleted')

    def handle_Delete_expense(self):
        git.accounting_manager.delete_records("mehdi", "expense")
        QMessageBox.information(self, 'Success', 'Your paid transactions have been deleted')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    button_app = ButtonApp()
    button_app.show()
    sys.exit(app.exec_())
