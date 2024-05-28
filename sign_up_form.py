import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, \
    QFormLayout, QComboBox, QDateEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QLocale, QDate
from validator import Validator
import git


class SignUpForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sign Up Form')
        self.setWindowIcon(QIcon('add-user.png'))  # Optional: Set an icon for the window
        self.setGeometry(700, 200, 550, 500)
        self.setFixedSize(580, 780)

        # Set font for labels
        font = QFont('Times New Roman', 12)

        # Create widgets
        self.first_name_label = QLabel('First Name :')
        self.first_name_label.setFont(font)
        self.first_name_input = QLineEdit()
        self.first_name_input.setPlaceholderText("Enter your first name")
        self.first_name_input.setMaxLength(20)

        self.last_name_label = QLabel('Last Name :')
        self.last_name_label.setFont(font)
        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Enter your last name")
        self.last_name_input.setMaxLength(20)

        self.birthdate_label = QLabel('Birth Date :')
        self.birthdate_label.setFont(font)
        self.birthdate_input = QDateEdit()
        self.birthdate_input.setCalendarPopup(True)
        self.birthdate_input.setDisplayFormat("yyyy-MM-dd")
        self.birthdate_input.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.birthdate_input.setStyleSheet("background-color:#E3FEF7")
        self.birthdate_input.setMinimumDate(QDate(1920, 1, 1))
        self.birthdate_input.setMaximumDate(QDate(2005, 12, 31))

        self.favorite_color_label = QLabel('Favorite Color :')
        self.favorite_color_label.setFont(font)
        self.favorite_color_input = QLineEdit()
        self.favorite_color_input.setPlaceholderText("Enter your favorite color")
        self.favorite_color_input.setMaxLength(20)

        self.city_label = QLabel('City :')
        self.city_label.setFont(font)
        self.city_input = QComboBox()
        self.city_input.addItems(
            ["Select your city", "Tehran", "Mashhad", "Isfahan", "Shiraz", "Tabriz", "Behshahr", "Karaj", "Rasht",
             "Kerman"])
        self.city_input.setStyleSheet("background-color:#E3FEF7")

        self.email_label = QLabel('Email :')
        self.email_label.setFont(font)
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setMaxLength(50)

        self.password_label = QLabel('Password :')
        self.password_label.setFont(font)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setMaxLength(20)

        self.confirm_password_label = QLabel('Confirm Password :')
        self.confirm_password_label.setFont(font)
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setPlaceholderText("Confirm your password")
        self.confirm_password_input.setMaxLength(20)

        self.mobile_label = QLabel('Mobile Number :')
        self.mobile_label.setFont(font)
        self.mobile_input = QLineEdit()
        self.mobile_input.setPlaceholderText("Enter your mobile number")
        self.mobile_input.setMaxLength(11)

        self.username_label = QLabel('Username :')
        self.username_label.setFont(font)
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setMaxLength(20)

        self.signup_button = QPushButton('Sign Up')
        self.signup_button.clicked.connect(self.handle_signup)
        self.signup_button.setFixedWidth(200)

        self.empty_label = QLabel('')

        # Set layout
        layout = QFormLayout()
        layout.addRow(self.first_name_label, self.first_name_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.last_name_label, self.last_name_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.mobile_label, self.mobile_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.email_label, self.email_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.username_label, self.username_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.birthdate_label, self.birthdate_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.city_label, self.city_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.favorite_color_label, self.favorite_color_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.password_label, self.password_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.confirm_password_label, self.confirm_password_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.empty_label)
        layout.addWidget(self.signup_button)

        self.setLayout(layout)

        # Set stylesheet with the provided color palette and rounded borders
        self.setStyleSheet("""
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
            QLineEdit{
                border: 3px solid #135D66;
                border-radius: 10px;
                padding: 5px;
                background-color: #E3FEF7;
            }
            QLineEdit:focus, QComboBox:focus, QDateEdit:focus {
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

    def handle_signup(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        favorite_color = self.favorite_color_input.text()
        birthday = self.birthdate_input.text()
        city = self.city_input.currentText()
        email = self.email_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        mobile = self.mobile_input.text()
        username = self.username_input.text()

        if not first_name or not last_name or not favorite_color or city == "Select your city" or not email or not username or not password or not confirm_password or not mobile:
            QMessageBox.warning(self, 'Error', 'Please fill in all fields')

        elif not Validator.validate_name(first_name) or not Validator.validate_name(last_name):
            QMessageBox.warning(self, 'Error', 'The name must contain only English letters')

        elif not Validator.validate_mobile_number(mobile):
            QMessageBox.warning(self, 'Error',
                                'The mobile number must start with 09 and must be 11 digits and is a number')
        elif not Validator.validate_email(email):
            QMessageBox.warning(self, 'Error', 'The email format entered is incorrect')

        elif not Validator.validate_username(username):
            QMessageBox.warning(self, 'Error', 'The username must contain only English letters and digits')

        elif not Validator.validate_password(password):
            QMessageBox.warning(self, 'Error',
                                'The password must have at least one lowercase English letter and one uppercase English letter and one symbol and one digit and have at least 6 digits')

        elif password != confirm_password:
            QMessageBox.warning(self, 'Error', 'Passwords do not match')

        else:
            person = git.User(first_name, last_name, mobile, username, email, password, city, birthday, favorite_color)
            git.data_manager.sign_up_user(person)
            QMessageBox.information(self, 'Success', f'Signed up as {first_name} {last_name}')
            # Here you can add more logic to handle the sign up process (e.g., saving the user information)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    signup_form = SignUpForm()
    signup_form.show()
    sys.exit(app.exec_())