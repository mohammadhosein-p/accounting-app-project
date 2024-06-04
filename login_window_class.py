from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QLineEdit, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from data_manager_class import *
import sys
from css_properties import css_code

app = QApplication(sys.argv)


class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)
        self.setWindowTitle("Login Page")
        self.setStyleSheet(css_code)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.grid = QGridLayout(central_widget)

        self.user_name_label = QLabel("Username:", self)
        self.user_name_label.setFont(QFont("New Times Roman", 14))
        self.user_name_label.setStyleSheet("color: #E3FEF7; margin: 0 50px 0 20px")
        self.grid.addWidget(self.user_name_label, 0, 0)

        self.user_name_input = QLineEdit(self)
        self.user_name_input.setFont(QFont("New Times Roman", 14))
        self.user_name_input.setPlaceholderText("Username")
        self.user_name_input.setMaxLength(30)

        self.grid.addWidget(self.user_name_input, 0, 1, 1, 2)

        self.password_label = QLabel("Password:", self)
        self.password_label.setFont(QFont("New Times Roman", 14))
        self.password_label.setStyleSheet("color: #E3FEF7; margin: 0 50px 0 20px")
        self.grid.addWidget(self.password_label, 1, 0)

        self.password_input = QLineEdit(self)
        self.password_input.setFont(QFont("New Times Roman", 14))
        self.password_input.setPlaceholderText("Password")
        self.password_input.setMaxLength(30)

        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.grid.addWidget(self.password_input, 1, 1, 1, 2)

        self.submit_btn = QPushButton("Submit", self)
        self.submit_btn.setFixedSize(120, 50)

        self.grid.addWidget(self.submit_btn, 2, 2)

        self.sign_up_label = QLabel("Don't have an account?", self)
        self.sign_up_label.setFixedSize(200, 40)
        self.sign_up_label.setFont(QFont("New Times Roman", 8))
        self.sign_up_label.setStyleSheet("color: #E3FEF7; margin-left: 30px; margin-top: 5px;")
        self.grid.addWidget(self.sign_up_label, 2, 0)

        self.sign_up_btn = QPushButton("Sign Up", self)
        self.sign_up_btn.setFixedSize(100, 50)
        self.sign_up_btn.setFont(QFont("New Times Roman", 8))

        self.back_btn = QPushButton("Back", self)
        self.back_btn.setFixedSize(80, 50)
        self.grid.addWidget(self.back_btn, 3, 3)

        self.grid.addWidget(self.sign_up_btn, 2, 1)

        self.forget_password_btn = QPushButton("Forget Password", self)
        self.forget_password_btn.setFixedSize(170, 50)

        self.grid.addWidget(self.forget_password_btn, 3, 0)

        self.security_question_label = QLabel("your favorite color?", self)
        self.security_question_label.setFont(QFont("New Times Roman", 10))
        self.security_question_label.setStyleSheet("color: #E3FEF7; margin: 0 10px 0 10px")
        self.grid.addWidget(self.security_question_label, 3, 1)
        self.security_question_label.setVisible(False)

        self.security_question_input = QLineEdit(self)
        self.security_question_input.setPlaceholderText("color")

        self.grid.addWidget(self.security_question_input, 3, 2)
        self.security_question_input.setVisible(False)

        self.forget_password_btn.clicked.connect(self.show_security_question)

    def show_security_question(self):
        self.security_question_input.setVisible(True)
        self.security_question_label.setVisible(True)
        self.forget_password_btn.setText("Check Password")
        self.forget_password_btn.clicked.connect(self.forget_password_check)

    def forget_password_check(self):
        response = data_manager.find_password(
            User(username=self.user_name_input.text(), security=self.security_question_input.text()))
        if response['result']:
            QMessageBox.information(self, "Info", "your password added")
            self.password_input.setText(response['password'])
        else:
            QMessageBox.warning(self, "Error", response["error"])

    def login_check(self):
        response = data_manager.log_in_user(
            User(username=self.user_name_input.text(), password=self.password_input.text()))
        if response["result"]:
            QMessageBox.information(self, "Info", f"you logged in as:\n{response['user_info']}")
            return True
        else:
            QMessageBox.warning(self, "Error", response["error"])
            return False


if __name__ == "__main__":
    data_manager = DataManager()
    window = LoginPage()
    window.show()
    sys.exit(app.exec())
