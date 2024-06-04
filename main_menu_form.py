import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main_Menu')
        self.setWindowIcon(QIcon('menu.png'))
        self.setFixedSize(400, 500)

        self.record_income_btn = QPushButton('Record income')
        self.record_expense_btn = QPushButton('Record Expense')
        self.search_btn = QPushButton('Search')
        self.category_btn = QPushButton('Category')
        self.account_inquiry_btn = QPushButton('Account Inquiry')
        self.setting_btn = QPushButton('Setting')
        self.exit_btn = QPushButton('Exit')

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.record_income_btn)
        main_layout.addWidget(self.record_expense_btn)
        main_layout.addWidget(self.search_btn)
        main_layout.addWidget(self.category_btn)
        main_layout.addWidget(self.account_inquiry_btn)
        main_layout.addWidget(self.setting_btn)
        main_layout.addWidget(self.exit_btn)
        main_layout.setSpacing(15)

        self.setLayout(main_layout)
        self.apply_stylesheet()

    def apply_stylesheet(self):
        self.setStyleSheet("""
            QWidget {
                background: #003C43;
                color: #E3FEF7;
                font-family: 'Times New Roman';
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    button_app = Menu()
    button_app.show()
    sys.exit(app.exec_())
