import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QSlider, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


default_palette = ["#003C43", "#135D66", "#77B0AA", "#E3FEF7"]
class ThemeChanger(QWidget):
    def __init__(self):
        super().__init__()
        self.palette_1 = ["#003C43", "#135D66", "#77B0AA", "#E3FEF7"]
        self.palette_2 = ["#112D4E", "#DBE2EF", "#3F72AF", "#F9F7F7"]
        self.palette_3 = ["#E1F0DA", "#D4E7C5", "#BFD8AF", "#99BC85"]
        self.using_palette = self.palette_1 
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
        self.apply_stylesheet()

    def change_to_theme2(self):
        self.using_palette = self.palette_2
        self.apply_stylesheet()
        
    def change_to_theme3(self):
        self.using_palette = self.palette_3
        self.apply_stylesheet()

    def apply_stylesheet(self):
        self.setStyleSheet(generate_css_code(using_palette=self.using_palette))

class FontChanger(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 200)
        self.setWindowTitle("Font setting")
        self.setWindowIcon(QIcon('../source/setting.png'))
        self.setStyleSheet(generate_css_code())
        self.font_family = "Times New Roman"
        self.font_size = 18

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        slider_layout = QHBoxLayout()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(12)
        self.slider.setMaximum(24)
        self.slider.setValue(18)
        self.slider.valueChanged.connect(self.update_fontSize)
        slider_layout.addWidget(self.slider)

        self.font_size_label = QLabel(str(self.slider.value()))
        slider_layout.addWidget(self.font_size_label)

        layout.addLayout(slider_layout)

        font_layout = QHBoxLayout()
        self.fonts = ["Arial", "Times New Roman", "Courier New"]
        self.font_buttons = QButtonGroup(self)

        for font in self.fonts:
            radio_button = QRadioButton(font)
            font_layout.addWidget(radio_button)
            self.font_buttons.addButton(radio_button)

        self.font_buttons.buttonClicked.connect(self.update_font)
        layout.addLayout(font_layout)

        self.confirm_button = QPushButton("Submit")
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)


    def update_fontSize(self, value):
        self.font_size = value
        self.font_size_label.setText(str(value))
        self.confirm_selection()

    def update_font(self):
        selected_button = self.font_buttons.checkedButton()
        if selected_button:
            self.font_family = selected_button.text()
            self.confirm_selection()

    def confirm_selection(self):
        self.setStyleSheet(generate_css_code(font_family=self.font_family, font_size=int(self.font_size)))


def generate_css_code(using_palette=default_palette, font_family="Times New Roman", font_size=18):
    return f"""
                QTableWidget {{
                    background-color: {using_palette[3]};
                    color: {using_palette[2]};
                    border: 2px solid {using_palette[1]};
                    font-size: {font_size}px;
                    font-family: {font_family};
                    border-radius: 10px;
                }}
                QHeaderView::section {{
                    background-color: {using_palette[1]};
                    color: {using_palette[3]};
                    padding: 5px;
                    border: 1px solid {using_palette[3]};
                }}
                QRadioButton {{
                    color: {using_palette[3]};
                    font-size: {font_size}px;
                    font-weight: bold;
                    font-family: {font_family};
                    spacing: 10px;
                }}
                QRadioButton::indicator {{
                    width: 20px;
                    height: 20px;
                }}
                QRadioButton::indicator:unchecked {{
                    border: 2px solid {using_palette[3]};
                    background-color: {using_palette[0]};
                    border-radius: 10px;
                }}
                QRadioButton::indicator:checked {{
                    border: 2px solid {using_palette[2]};
                    background-color: {using_palette[2]};
                    border-radius: 10px;
                }}
                QWidget {{
                    font-family: {font_family};
                    font-size: {font_size}px;
                    background-color: {using_palette[0]};
                }}
                QLabel {{
                    font-size: {font_size}px;
                    font-family: {font_family};
                    color: {using_palette[3]};
                }}
                QComboBox, QDateEdit {{
                    border: 3px solid {using_palette[1]};
                    border-top-left-radius: 10px; border-bottom-left-radius: 10px;
                    padding: 5px;
                    background-color: {using_palette[3]};
                }}
                QLineEdit {{
                    border: 3px solid {using_palette[1]};
                    border-radius: 10px;
                    padding: 5px;
                    background-color: {using_palette[3]};
                    font-size: {font_size}px;
                    font-weight: bold;
                    font-family: {font_family};
                }}
                QLineEdit:focus, QComboBox:focus, QDateEdit:focus {{
                    border: 3px solid red;
                }}
                QTextEdit {{
                    border: 3px solid {using_palette[1]};
                    border-radius: 10px;
                    padding: 10px;
                    background-color: {using_palette[3]};
                    font-size: {font_size}px;
                    font-weight: bold;
                    font-family: {font_family};
                }}
                QTextEdit:focus {{
                    border: 3px solid red;
                }}
                QPushButton {{
                    background-color: {using_palette[2]};
                    color: white;
                    padding: 10px;
                    text-align: center;
                    margin: 4px 2px;
                    border-radius: 10px;
                    font-size: {font_size}px;
                    font-weight: bold;
                    font-family: {font_family};
                }}
                QPushButton:hover {{
                    background-color: #EEEEEE;
                    color: {using_palette[0]};
                }}
                QCalendarWidget QToolButton {{
                    background-color: {using_palette[0]};
                    color: black;
                    border: none;
                    border-radius: 5px;
                    padding: 5px;
                }}
                QCalendarWidget QToolButton:hover {{
                    background-color: {using_palette[0]};
                    color: {using_palette[3]};
                }}
                QCalendarWidget QWidget {{
                    background-color: {using_palette[0]};
                }}
                QCalendarWidget QAbstractItemView:enabled {{
                    color: {using_palette[0]};
                    background-color: {using_palette[3]};
                    selection-background-color: {using_palette[2]};
                    selection-color: #FFFFFF;
                }}
                QLineEdit, QComboBox, QSpinBox {{
                    border: 2px solid {using_palette[1]};
                    border-radius: 10px;
                    padding: 5px;
                    background-color: {using_palette[3]};
                    font-size: {font_size}px;
                    font-family: {font_family};
                    color: {using_palette[0]};
                }}
            """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # theme_changer = ThemeChanger()
    my_font_changer = FontChanger()
    # theme_changer.show()
    my_font_changer.show()
    sys.exit(app.exec_())
