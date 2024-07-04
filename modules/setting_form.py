import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
import modules.data_manager_class as data_manager_class
import modules.edit_info as edit_info
from datetime import datetime


class Setting(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Setting')
        self.setWindowIcon(QIcon('../source/setting.png'))
        self.setFixedSize(400, 500)

        self.button1 = QPushButton('Change the theme')
        self.button2 = QPushButton('Change font setting')
        self.button3 = QPushButton('Delete account')
        self.button4 = QPushButton('Edit information')
        self.button4.clicked.connect(self.handle_editing_information)
        self.button5 = QPushButton('Export information')
        self.button5.clicked.connect(self.handle_excavating_information)
        self.button6 = QPushButton('Delete income')
        self.button6.clicked.connect(self.handle_Delete_income)
        self.button7 = QPushButton('Delete expense')
        self.button7.clicked.connect(self.handle_Delete_expense)
        self.Back_btn = QPushButton('Back')

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.button1)
        main_layout.addWidget(self.button2)
        main_layout.addWidget(self.button3)
        main_layout.addWidget(self.button4)
        main_layout.addWidget(self.button5)
        main_layout.addWidget(self.button6)
        main_layout.addWidget(self.button7)
        main_layout.addWidget(self.Back_btn)
        main_layout.setSpacing(15)

        self.setLayout(main_layout)

    def handle_Delete_account(self):
        data_manager_class.accounting_manager.delete_account(self.current_user)
        QMessageBox.information(self, 'Success', 'goodbye')

    def handle_editing_information(self):
        editor = data_manager_class.accounting_manager.edit_information(self.current_user)
        self.ui = edit_info.SignUpForm()

        self.ui.first_name_input.setText(f"{editor[0][0]}")
        self.ui.last_name_input.setText(f"{editor[0][1]}")
        self.ui.mobile_input.setText(f"{editor[0][2]}")
        self.ui.email_input.setText(f"{editor[0][4]}")
        self.ui.username_input.setText(f"{editor[0][3]}")
        self.ui.username_input.setEnabled(False)
        initial_date = datetime.strptime(editor[0][7], "%Y-%m-%d")
        self.ui.birthdate_input.setDate(initial_date)
        self.ui.city_input.setCurrentText(f"{editor[0][6]}")
        self.ui.favorite_color_input.setText(f"{editor[0][8]}")
        self.ui.password_input.setText(f"{editor[0][5]}")
        self.ui.confirm_password_input.setText(f"{editor[0][5]}")

        self.ui.show()

    def handle_excavating_information(self):
        data_manager_class.accounting_manager.export_account(self.current_user)
        QMessageBox.information(self, 'Success', 'Your transaction exported as transaction.csv')

    def handle_Delete_income(self):
        data_manager_class.accounting_manager.delete_records(self.current_user, "income")
        QMessageBox.information(self, 'Success', 'Your revenue transactions have been deleted')

    def handle_Delete_expense(self):
        data_manager_class.accounting_manager.delete_records(self.current_user, "expense")
        QMessageBox.information(self, 'Success', 'Your paid transactions have been deleted')

    def set_current_user(self, user):
        self.current_user = user

if __name__ == '__main__':
    app = QApplication(sys.argv)
    button_app = Setting()
    button_app.show()
    sys.exit(app.exec_())
