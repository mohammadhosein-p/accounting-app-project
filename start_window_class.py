from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont
import sys

app = QApplication(sys.argv)

class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 300)
        self.setWindowTitle("Start Window")
        self.setStyleSheet("""
            QWidget {
                background-color: #003C43;  
            }
            QPushButton {
                border: None;
                background-color: #76ABAE; 
                border-radius: 8px; 
                color: #EEEEEE;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #EEEEEE;
                color: #003C43;
            }
        """)
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
        self.sign_up_btn.clicked.connect(self.create_sign_up_page)
        self.login_btn.clicked.connect(self.create_login_page)

    def create_sign_up_page(self):
        print("sign up")
        
    def create_login_page(self):
        print("log in")
        

window = StartWindow()
window.show()
sys.exit(app.exec())