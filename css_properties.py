palette_1 = ["#003C43", "#135D66", "#77B0AA", "#E3FEF7"]
palette_2 = ["#112D4E", "#DBE2EF", "#3F72AF", "#F9F7F7"]
using_palette = palette_1

css_code = f"""
            QTableWidget {{
                background-color: {using_palette[3]};
                color: {using_palette[0]};
                border: 2px solid {using_palette[1]};
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
                background-color: {using_palette[0]};
            }}
            QLabel {{
                color: {using_palette[3]};
                font-size: 14px;
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
                font-size: 20px;
                font-weight: bold;
                font-family: 'Times New Roman';
            }}
            QLineEdit:focus, QComboBox:focus, QDateEdit:focus {{
                border: 3px solid red;
            }}
            QTextEdit {{
                border: 3px solid {using_palette[1]};
                border-radius: 10px;
                padding: 10px;
                background-color: {using_palette[3]};
                font-size: 20px;
                font-weight: bold;
                font-family: 'Times New Roman';
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
                font-size: 20px;
                font-weight: bold;
                font-family: 'Times New Roman';
            }}
            QPushButton:hover {{
                background-color: #EEEEEE;
                color: {using_palette[0]};
            }}
            QCalendarWidget QToolButton {{
                background-color: {using_palette[0]};
                color: {using_palette[0]};
                border: none;
                border-radius: 5px;
                padding: 5px;
            }}
            QCalendarWidget QToolButton:hover {{
                background-color: {using_palette[0]};
                color: {using_palette[0]};
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
                color: {using_palette[0]};
            }}
        """