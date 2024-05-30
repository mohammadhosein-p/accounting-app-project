import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, \
    QFormLayout, QComboBox, QDateEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QLocale, QDate
import data_manager_class
from datetime import datetime
today = datetime.today()
qdate_today = QDate(today.year, today.month, today.day)

class RecordExpenses(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Record expenses Form')
        self.setWindowIcon(QIcon("expense.png"))
        self.setGeometry(700, 200, 550, 500)
        self.setFixedSize(580, 480)

        # Set font for labels
        font = QFont('Times New Roman', 12)

        # Create widgets
        self.expenses_label = QLabel('expenses :')
        self.expenses_label.setFont(font)
        self.expenses_input = QLineEdit()
        self.expenses_input.setPlaceholderText("Enter your expenses")
        self.expenses_input.setMaxLength(20)

        self.source_label = QLabel('source of expenses :')
        self.source_label.setFont(font)
        self.source_input = QComboBox()
        self.source_input.addItems([category[0] for category in data_manager_class.category_manager.all_catogory_title()])
        self.source_input.setStyleSheet("background-color:#E3FEF7")

        self.date_label = QLabel('date of expenses :')
        self.date_label.setFont(font)
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDisplayFormat("yyyy-MM-dd")
        self.date_input.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.date_input.setStyleSheet("background-color:#E3FEF7")
        self.date_input.setMinimumDate(QDate(1970, 1, 1))
        self.date_input.setMaximumDate(qdate_today)

        self.description_label = QLabel('Description of expenses :')
        self.description_label.setFont(font)
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Enter your Description of expenses")
        self.description_input.setMaxLength(100)

        self.type_label = QLabel('Type of expenses :')
        self.type_label.setFont(font)
        self.type_input = QComboBox()
        self.type_input.addItems(
            ["Type of expenses", "Cash", "Digital currency", "Cheque"])
        self.type_input.setStyleSheet("background-color:#E3FEF7")

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.handle_submit)
        self.submit_button.setFixedWidth(200)

        self.empty_label = QLabel('')

        layout = QFormLayout()
        layout.addRow(self.expenses_label, self.expenses_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.source_label, self.source_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.date_label, self.date_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.description_label, self.description_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.type_label, self.type_input)
        layout.addRow(self.empty_label)
        layout.addRow(self.empty_label)
        layout.addWidget(self.submit_button)
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

    def handle_submit(self):
        record_type = "expense"
        expenses = self.expenses_input.text()
        source = self.source_input.currentText()
        date = self.date_input.text()
        type = self.type_input.currentText()
        description = self.description_input.text()

        if not expenses or not date or source == "source of expenses" or type == "Type of expenses":
            QMessageBox.warning(self, 'Error', 'Please fill in all fields')

        elif not expenses.isnumeric() or float(expenses) < 0:
            QMessageBox.warning(self, 'Error', 'expenses must be a positive number')

        else:
            QMessageBox.information(self, 'Success', 'Your expenses has been registered')
            transaction = data_manager_class.Record(record_type, "mehdi", expenses, date, source, description)
            data_manager_class.accounting_manager.add_recordd(transaction)
            # Here you can add more logic to handle the sign up process (e.g., saving the user information)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    record_expenses_form = RecordExpenses()
    record_expenses_form.show()
    sys.exit(app.exec_())
