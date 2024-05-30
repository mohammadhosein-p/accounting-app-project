css_code = """
            QTableWidget {
            color: #E3FEF7;
            }
            QRadioButton {
                color: #E3FEF7;
                font-size: 20px;
                font-weight: bold;
                font-family: 'Times New Roman';
                spacing: 10px;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
            }
            QRadioButton::indicator:unchecked {
                border: 2px solid #E3FEF7;
                background-color: #003C43;
                border-radius: 10px;
            }
            QRadioButton::indicator:checked {
                border: 2px solid #77B0AA;
                background-color: #77B0AA;
                border-radius: 10px;
            }
            QWidget {
                background-color: #003C43;
            }
            QLabel {
                color: #E3FEF7;
                font-size: 14px;
            }
            QComboBox, QDateEdit {
                border: 3px solid #135D66;
                border-top-left-radius: 10px; border-bottom-left-radius: 10px;
                padding: 5px;
                background-color: #E3FEF7;
            }
            QLineEdit {
                border: 3px solid #135D66;
                border-radius: 10px;
                padding: 5px;
                background-color: #E3FEF7;
                font-size: 20px;
                font-weight: bold;
                font-family: 'Times New Roman';
            }
            QLineEdit:focus, QComboBox:focus, QDateEdit:focus {
                border: 3px solid red;
            }
            QTextEdit {
                border: 3px solid #135D66;
                border-radius: 10px;
                padding: 10px;
                background-color: #E3FEF7;
                font-size: 20px;
                font-weight: bold;
                font-family: 'Times New Roman';
            }
            QTextEdit:focus {
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
            QLineEdit, QComboBox, QSpinBox {
                border: 2px solid #135D66;
                border-radius: 10px;
                padding: 5px;
                background-color: #E3FEF7;
                color: #003C43;
            }
        """