from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QPushButton, QHBoxLayout, QGridLayout
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
import css_properties

app = QApplication(sys.argv)


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.theme_changer = css_properties.ThemeChanger()
        self.setFixedSize(400, 300)
        self.setWindowTitle("Start Window")
        self.setStyleSheet(self.theme_changer.generate_css_code())

        self.grid = QGridLayout(self)
        self.label = QLabel("Welcome to the app!", self)
        self.label.setStyleSheet("color: white; font-size: 40px;")
        self.grid.addWidget(self.label, 0, 0, 0, 2)


        self.login_btn = QPushButton("Login", self)
        self.setStyleSheet(self.theme_changer.generate_css_code())
        self.grid.addWidget(self.login_btn, 1, 0)

        self.sign_up_btn = QPushButton("Sign Up", self)
        self.sign_up_btn.setStyleSheet(self.theme_changer.generate_css_code())
        self.grid.addWidget(self.sign_up_btn, 1, 1)


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
        self.login.sign_up_btn.clicked.connect(self.go_to_sign_from_login)

        self.menu.record_income_btn.clicked.connect(self.go_to_income)
        self.menu.record_expense_btn.clicked.connect(self.go_to_expense)
        self.menu.search_btn.clicked.connect(self.go_to_search)
        self.menu.category_btn.clicked.connect(self.go_to_category)
        self.menu.account_inquiry_btn.clicked.connect(self.go_to_inquiry)
        self.menu.setting_btn.clicked.connect(self.go_to_setting)
        self.menu.exit_btn.clicked.connect(exit)

        self.income.Back_button.clicked.connect(self.back_from_income)
        self.expense.Back_button.clicked.connect(self.back_from_expense)
        self.search.back_button.clicked.connect(self.back_from_search)
        self.category.back_btn.clicked.connect(self.back_from_category)
        self.report.back_button.clicked.connect(self.back_from_inquiry)
        self.setting.Back_btn.clicked.connect(self.back_from_setting)

        self.setting.button2.clicked.connect(self.delete_account)
        self.setting.button1.clicked.connect(self.go_to_theme_changer)
        self.theme_changer.back_btn.clicked.connect(self.back_from_theme_changer)
        self.setting.button3.clicked.connect(self.apply_styles_to_edit)

        self.apply_styles()

    def delete_account(self):
        self.setting.handle_Delete_account()
        self.setting.close()
        self.show()

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
        response = self.login.login_check()
        if response['result']:
            self.current_user = response["user_info"]
            self.login.hide()
            self.menu.show()

    def go_to_theme_changer(self):
        self.setting.hide()
        self.theme_changer.show()
    
    def back_from_theme_changer(self):
        self.apply_styles()
        self.theme_changer.hide()
        self.setting.show()

    def go_to_income(self):
        self.menu.hide()
        self.income.set_current_user(self.current_user[3])
        self.income.add_categories()
        self.income.show()

    def go_to_expense(self):
        self.menu.hide()
        self.expense.set_current_user(self.current_user[3])
        self.expense.add_categories()
        self.expense.show()

    def go_to_search(self):
        self.menu.hide()
        self.search.set_current_user(self.current_user[3])
        self.search.show()

    def go_to_category(self):
        self.menu.hide()
        self.category.set_current_user(self.current_user[3])
        self.category.show()

    def go_to_inquiry(self):
        self.menu.hide()
        self.report.set_current_user(self.current_user[3])
        self.report.show()

    def go_to_setting(self):
        self.menu.hide()
        self.setting.set_current_user(self.current_user[3])
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

    def go_to_sign_from_login(self):
        self.login.hide()
        self.sign_up.show()

    def apply_styles(self):
        css = self.theme_changer.generate_css_code()
        self.setStyleSheet(css)
        self.sign_up.setStyleSheet(css)
        self.login.setStyleSheet(css)
        self.menu.setStyleSheet(css)
        self.income.setStyleSheet(css)
        self.expense.setStyleSheet(css)
        self.search.setStyleSheet(css)
        self.setting.setStyleSheet(css)
        self.category.setStyleSheet(css)
        self.report.setStyleSheet(css)
        self.edit.setStyleSheet(css)

    def apply_styles_to_edit(self):
        css = self.theme_changer.generate_css_code()
        self.setting.ui.setStyleSheet(css)



window = StartWindow()
window.show()
sys.exit(app.exec())
