import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon

class ThemeChanger(QWidget):
    def __init__(self):
        super().__init__()
        self.palette_1 = ["#003C43", "#135D66", "#77B0AA", "#E3FEF7"]
        self.palette_2 = ["#112D4E", "#DBE2EF", "#3F72AF", "#F9F7F7"]
        self.palette_3 = ["#E1F0DA", "#D4E7C5", "#BFD8AF", "#99BC85"]
        self.using_palette = self.palette_1  # Initialize using_palette

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Theme Changer')
        self.setWindowIcon(QIcon('menu.png'))
        self.setFixedSize(400, 500)

        self.theme_1_btn = QPushButton("Theme 1", self)
        self.theme_2_btn = QPushButton("Theme 2", self)
        self.theme_3_btn = QPushButton("Theme 3", self)
        self.back_btn = QPushButton("Back", self)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.theme_1_btn)
        main_layout.addWidget(self.theme_2_btn)
        main_layout.addWidget(self.theme_3_btn)
        main_layout.addWidget(self.back_btn)
        main_layout.setSpacing(15)

        self.theme_1_btn.clicked.connect(self.change_to_theme1)
        self.theme_2_btn.clicked.connect(self.change_to_theme2)
        self.theme_3_btn.clicked.connect(self.change_to_theme3)

        self.setLayout(main_layout)
        self.apply_stylesheet()
        
    def change_to_theme1(self):
        self.using_palette = self.palette_1
        self.apply_stylesheet()  # Apply the new stylesheet

    def change_to_theme2(self):
        self.using_palette = self.palette_2
        self.apply_stylesheet()  # Apply the new stylesheet
        
    def change_to_theme3(self):
        self.using_palette = self.palette_3
        self.apply_stylesheet()  # Apply the new stylesheet

    def apply_stylesheet(self):
        self.setStyleSheet(self.generate_css_code())

    def generate_css_code(self):
        return f"""
                    QTableWidget {{
                        background-color: {self.using_palette[3]};
                        color: {self.using_palette[2]};
                        border: 2px solid {self.using_palette[1]};
                        border-radius: 10px;
                    }}
                    QHeaderView::section {{
                        background-color: {self.using_palette[1]};
                        color: {self.using_palette[3]};
                        padding: 5px;
                        border: 1px solid {self.using_palette[3]};
                    }}
                    QRadioButton {{
                        color: {self.using_palette[3]};
                        font-size: 20px;
                        font-weight: bold;
                        font-family: 'Times New Roman';
                        spacing: 10px;
                    }}
                    QRadioButton::indicator {{
                        width: 20px;
                        height: 20px;
                    }}
                    QRadioButton::indicator:unchecked {{
                        border: 2px solid {self.using_palette[3]};
                        background-color: {self.using_palette[0]};
                        border-radius: 10px;
                    }}
                    QRadioButton::indicator:checked {{
                        border: 2px solid {self.using_palette[2]};
                        background-color: {self.using_palette[2]};
                        border-radius: 10px;
                    }}
                    QWidget {{
                        background-color: {self.using_palette[0]};
                    }}
                    QLabel {{
                        color: {self.using_palette[3]};
                        font-size: 14px;
                    }}
                    QComboBox, QDateEdit {{
                        border: 3px solid {self.using_palette[1]};
                        border-top-left-radius: 10px; border-bottom-left-radius: 10px;
                        padding: 5px;
                        background-color: {self.using_palette[3]};
                    }}
                    QLineEdit {{
                        border: 3px solid {self.using_palette[1]};
                        border-radius: 10px;
                        padding: 5px;
                        background-color: {self.using_palette[3]};
                        font-size: 15px;
                        font-weight: bold;
                        font-family: 'Times New Roman';
                    }}
                    QLineEdit:focus, QComboBox:focus, QDateEdit:focus {{
                        border: 3px solid red;
                    }}
                    QTextEdit {{
                        border: 3px solid {self.using_palette[1]};
                        border-radius: 10px;
                        padding: 10px;
                        background-color: {self.using_palette[3]};
                        font-size: 20px;
                        font-weight: bold;
                        font-family: 'Times New Roman';
                    }}
                    QTextEdit:focus {{
                        border: 3px solid red;
                    }}
                    QPushButton {{
                        background-color: {self.using_palette[2]};
                        color: white;
                        padding: 10px;
                        text-align: center;
                        margin: 4px 2px;
                        border-radius: 10px;
                        font-size: 20px;
                        font-weight: bold;
                        font-family: 'Times New Roman';
                    }}
                    QPushButton:hover {{
                        background-color: #EEEEEE;
                        color: {self.using_palette[0]};
                    }}
                    QCalendarWidget QToolButton {{
                        background-color: {self.using_palette[0]};
                        color: {self.using_palette[3]};
                        border: none;
                        border-radius: 5px;
                        padding: 5px;
                    }}
                    QCalendarWidget QToolButton:hover {{
                        background-color: {self.using_palette[0]};
                        color: {self.using_palette[3]};
                    }}
                    QCalendarWidget QWidget {{
                        background-color: {self.using_palette[0]};
                    }}
                    QCalendarWidget QAbstractItemView:enabled {{
                        color: {self.using_palette[0]};
                        background-color: {self.using_palette[3]};
                        selection-background-color: {self.using_palette[2]};
                        selection-color: #FFFFFF;
                    }}
                    QLineEdit, QComboBox, QSpinBox {{
                        border: 2px solid {self.using_palette[1]};
                        border-radius: 10px;
                        padding: 5px;
                        background-color: {self.using_palette[3]};
                        color: {self.using_palette[0]};
                    }}
                """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    theme_changer = ThemeChanger()
    theme_changer.show()
    sys.exit(app.exec_())
