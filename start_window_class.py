from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont
import sys
import login_window_class
import sign_up_form
import main_menu_form
import search_form
import submit_income_form
import submit_expenses_form
import setting_form
import category_form_class
import reporting_form
import editt
from css_properties import css_code

app = QApplication(sys.argv)


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 300)
        self.setWindowTitle("Start Window")
        self.setStyleSheet(css_code)

        self.label = QLabel("Welcome to the app!", self)
        self.label.setGeometry(80, 50, 280, 50)
        self.label.setFont(QFont("Times New Roman", 18))
        self.label.setStyleSheet("color: #EEEEEE;")
        self.hbox = QHBoxLayout(self)

        self.login_btn = QPushButton("Login", self)
        self.login_btn.setFixedSize(100, 35)
        self.login_btn.setFont(QFont("Times New Roman", 14))

        self.sign_up_btn = QPushButton("Sign Up", self)
        self.sign_up_btn.setFixedSize(100, 35)
        self.sign_up_btn.setFont(QFont("Times New Roman", 14))

        self.hbox.addWidget(self.login_btn)
        self.hbox.addWidget(self.sign_up_btn)

        # -----------------------------------------------MANAGING------------------------------------- #

        self.sign_up = sign_up_form.SignUpForm()
        self.login = login_window_class.LoginPage()
        self.menu = main_menu_form.Menu()
        self.income = submit_income_form.RecordIncome()
        self.expense = submit_expenses_form.RecordExpenses()
        self.search = search_form.SearchFilterApp()
        self.setting = setting_form.Setting()
        self.category = category_form_class.Category()
        self.report = reporting_form.Reporting()
        self.edit = editt.SignUpForm()

        self.sign_up_btn.clicked.connect(self.create_sign_up_page)
        self.login_btn.clicked.connect(self.create_login_page)

        self.sign_up.back_button.clicked.connect(self.back_from_sing_up)

        self.login.back_btn.clicked.connect(self.back_from_login)
        self.login.submit_btn.clicked.connect(self.go_to_menu_from_login)

        self.menu.record_income_btn.clicked.connect(self.go_to_income)
        self.menu.record_expense_btn.clicked.connect(self.go_to_expense)
        self.menu.search_btn.clicked.connect(self.go_to_search)
        self.menu.category_btn.clicked.connect(self.go_to_category)
        self.menu.account_inquiry_btn.clicked.connect(self.go_to_inquiry)
        self.menu.setting_btn.clicked.connect(self.go_to_setting)

        self.income.Back_button.clicked.connect(self.back_from_income)
        self.expense.Back_button.clicked.connect(self.back_from_expense)
        self.search.back_button.clicked.connect(self.back_from_search)
        self.category.back_btn.clicked.connect(self.back_from_category)
        self.report.back_button.clicked.connect(self.back_from_inquiry)
        self.setting.Back_btn.clicked.connect(self.back_from_setting)


    def create_sign_up_page(self):
        self.hide()
        self.sign_up.show()

    def create_login_page(self):
        self.hide()
        self.login.show()

    def back_from_sing_up(self):
        self.sign_up.hide()
        self.show()

    def back_from_login(self):
        self.login.hide()
        self.show()

    def go_to_menu_from_login(self):
        self.login.hide()
        self.menu.show()

    def go_to_income(self):
        self.menu.hide()
        self.income.show()

    def go_to_expense(self):
        self.menu.hide()
        self.expense.show()

    def go_to_search(self):
        self.menu.hide()
        self.search.show()

    def go_to_category(self):
        self.menu.hide()
        self.category.show()

    def go_to_inquiry(self):
        self.menu.hide()
        self.report.show()

    def go_to_setting(self):
        self.menu.hide()
        self.setting.show()

    def back_from_income(self):
        self.income.hide()
        self.menu.show()

    def back_from_expense(self):
        self.expense.hide()
        self.menu.show()

    def back_from_search(self):
        self.search.hide()
        self.menu.show()

    def back_from_setting(self):
        self.setting.hide()
        self.menu.show()

    def back_from_category(self):
        self.category.hide()
        self.menu.show()

    def back_from_inquiry(self):
        self.report.hide()
        self.menu.show()



window = StartWindow()
window.show()
sys.exit(app.exec())
