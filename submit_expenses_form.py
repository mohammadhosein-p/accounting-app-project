import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, \
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
        self.current_user = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Record expenses Form')
        self.setWindowIcon(QIcon("expense.png"))
        self.setGeometry(700, 200, 550, 500)
        self.setFixedSize(580, 480)

        font = QFont('Times New Roman', 12)

        self.expenses_label = QLabel('expenses :')
        self.expenses_label.setFont(font)
        self.expenses_input = QLineEdit()
        self.expenses_input.setPlaceholderText("Enter your expenses")
        self.expenses_input.setMaxLength(20)

        self.source_label = QLabel('source of expenses :')
        self.source_label.setFont(font)
        self.source_input = QComboBox()
        print(self.current_user)
        self.source_input.addItems([category[0] for category in data_manager_class.category_manager.all_catogory_title(self.current_user)])
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
            ["Cash", "Digital currency", "Cheque"])
        self.type_input.setStyleSheet("background-color:#E3FEF7")

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.handle_submit)
        self.submit_button.setFixedWidth(200)

        self.Back_button = QPushButton('Back')
        self.Back_button.setFixedWidth(200)

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
        layout.addWidget(self.Back_button)
        self.setLayout(layout)


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
            transaction = data_manager_class.Record(record_type, self.current_user, expenses, date, source, description,type)
            data_manager_class.accounting_manager.add_recordd(transaction)

    def set_current_user(self, user):
        self.current_user = user


if __name__ == '__main__':
    app = QApplication(sys.argv)
    record_expenses_form = RecordExpenses()
    record_expenses_form.show()
    sys.exit(app.exec_())
