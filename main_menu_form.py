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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    button_app = Menu()
    button_app.show()
    sys.exit(app.exec_())
