import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, \
    QFormLayout, QComboBox, QDateEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QLocale, QDate
import modules.data_manager_class as data_manager_class
from datetime import datetime

today = datetime.today()
qdate_today = QDate(today.year, today.month, today.day)


class RecordIncome(QWidget):
    def __init__(self):
        self.current_user = ""
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Record income Form')
        self.setWindowIcon(QIcon('../source/growth.png'))
        self.setGeometry(700, 200, 550, 500)
        self.setFixedSize(580, 480)

        font = QFont('Times New Roman', 12)

        self.income_label = QLabel('Income :')
        self.income_label.setFont(font)
        self.income_input = QLineEdit()
        self.income_input.setPlaceholderText("Enter your Income")
        self.income_input.setMaxLength(20)

        self.source_label = QLabel('source of income :')
        self.source_label.setFont(font)
        self.source_input = QComboBox()
        self.source_input.setStyleSheet("background-color:#E3FEF7")

        self.date_label = QLabel('date of income :')
        self.date_label.setFont(font)
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDisplayFormat("yyyy-MM-dd")
        self.date_input.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.date_input.setStyleSheet("background-color:#E3FEF7")
        self.date_input.setMinimumDate(QDate(1970, 1, 1))
        self.date_input.setMaximumDate(qdate_today)

        self.description_label = QLabel('Description of income :')
        self.description_label.setFont(font)
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Enter your Description of income")
        self.description_input.setMaxLength(100)

        self.type_label = QLabel('Type of income :')
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
        layout.addRow(self.income_label, self.income_input)
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

    def add_categories(self):
        self.source_input.addItems([category[1] for category in data_manager_class.category_manager.all_catogory_title(self.current_user)])

    def handle_submit(self):
        record_type = "income"
        income = self.income_input.text()
        source = self.source_input.currentText()
        date = self.date_input.text()
        type = self.type_input.currentText()
        description = self.description_input.text()

        if not income or not date or source == "source of income" or type == "Type of income":
            QMessageBox.warning(self, 'Error', 'Please fill in all fields')

        elif not income.isnumeric() or float(income) < 0:
            QMessageBox.warning(self, 'Error', 'Income must be a positive number')

        else:
            QMessageBox.information(self, 'Success', 'Your income has been registered')
            transaction = data_manager_class.Record(record_type, self.current_user, income, date, source, description, type)
            data_manager_class.accounting_manager.add_record(transaction)

    def set_current_user(self, user):
        self.current_user = user


if __name__ == '__main__':
    app = QApplication(sys.argv)
    record_income_form = RecordIncome()
    record_income_form.show()
    sys.exit(app.exec_())
