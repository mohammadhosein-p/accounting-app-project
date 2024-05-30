import sys
from datetime import datetime, timedelta
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QComboBox, QTableWidget, QTableWidgetItem, QFormLayout, QSpinBox, QMessageBox, QButtonGroup, QGridLayout, QRadioButton, QDateEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QLocale, QDate
from data_manager_class import *
from css_properties import css_code

class Reporting(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Reporting Section")
        self.setGeometry(700, 200, 800, 600)
        self.setStyleSheet(css_code)

        self.grid = QGridLayout(self)

        self.default_filter_radiobtn = QRadioButton("Default Filter", self)
        self.default_filter_radiobtn.setChecked(True)
        self.grid.addWidget(self.default_filter_radiobtn, 0, 0)

        self.custom_filter_radiobtn = QRadioButton("Custom Filter", self)
        self.grid.addWidget(self.custom_filter_radiobtn, 0, 1)

        self.filter_group = QButtonGroup(self)
        self.filter_group.addButton(self.default_filter_radiobtn)
        self.filter_group.addButton(self.custom_filter_radiobtn)

        self.radiobtn_container = QVBoxLayout()
        self.grid.addLayout(self.radiobtn_container, 1, 0)

        self.day_radio = QRadioButton("Today", self)
        self.month_radio = QRadioButton("This month", self)
        self.year_radio = QRadioButton("This year", self)
        self.radiobtn_container.addWidget(self.day_radio)
        self.radiobtn_container.addWidget(self.month_radio)
        self.radiobtn_container.addWidget(self.year_radio)

        self.date_filter_group = QButtonGroup(self)
        self.date_filter_group.addButton(self.day_radio)
        self.date_filter_group.addButton(self.month_radio)
        self.date_filter_group.addButton(self.year_radio)

        current_date = datetime.now()

        self.start_date_label = QLabel('Start Date :')
        self.start_date_label.setFont(QFont("Times New Roman", 12))
        self.grid.addWidget(self.start_date_label, 1, 1)
        self.start_input = QDateEdit()
        self.start_input.setCalendarPopup(True)
        self.start_input.setDisplayFormat("yyyy-MM-dd")
        self.start_input.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.start_input.setStyleSheet("background-color:#E3FEF7")
        self.start_input.setMinimumDate(QDate(1999, 1, 1))
        self.start_input.setMaximumDate(QDate(current_date.year, current_date.month, current_date.day))
        self.grid.addWidget(self.start_input, 1, 2)

        self.end_date_label = QLabel('End Date :')
        self.end_date_label.setFont(QFont("Times New Roman", 12))
        self.grid.addWidget(self.end_date_label, 2, 1)
        self.end_input = QDateEdit()
        self.end_input.setCalendarPopup(True)
        self.end_input.setDisplayFormat("yyyy-MM-dd")
        self.end_input.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.end_input.setStyleSheet("background-color:#E3FEF7")
        self.end_input.setMinimumDate(QDate(2010, 1, 1))
        self.end_input.setMaximumDate(QDate(current_date.year, current_date.month, current_date.day))
        self.grid.addWidget(self.end_input, 2, 2)

        self.price_range_start_label = QLabel("Start range: ")
        self.grid.addWidget(self.price_range_start_label, 3, 0)

        self.price_range_end_label = QLabel("End range: ")
        self.grid.addWidget(self.price_range_end_label, 4, 0)

        self.price_start = QSpinBox()
        self.price_start.setMaximum(1000000000)
        self.grid.addWidget(self.price_start, 3, 1)
        
        self.price_end = QSpinBox()
        self.price_end.setMaximum(1000000000)
        self.grid.addWidget(self.price_end, 4, 1)

        self.type_label = QLabel("Type: ", self)
        self.grid.addWidget(self.type_label, 5, 0)
        self.type_input = QComboBox()
        self.type_input.addItems(
            ["Cash", "Digital currency", "Cheque"])
        self.type_input.setStyleSheet("background-color:#E3FEF7")
        self.grid.addWidget(self.type_input, 5, 1)

        self.hbox = QHBoxLayout()
        self.grid.addLayout(self.hbox, 6, 0)
        self.income_radio = QRadioButton("Income", self)
        self.expense_radio = QRadioButton("Expense", self)
        self.hbox.addWidget(self.income_radio)
        self.hbox.addWidget(self.expense_radio)

        self.type_group = QButtonGroup(self)
        self.type_group.addButton(self.income_radio)
        self.type_group.addButton(self.expense_radio)

        self.submit_btn = QPushButton("Submit", self)
        self.grid.addWidget(self.submit_btn, 7, 0, 1, 3)

        self.results_table = QTableWidget()
        self.results_table.setColumnCount(6)
        self.results_table.setHorizontalHeaderLabels(['Username', 'Amount', 'Date', 'Source', 'Description', 'Source'])
        self.grid.addWidget(self.results_table, 8, 0, 8, 3)

        self.start_input.setVisible(False)
        self.start_date_label.setVisible(False)
        self.end_input.setVisible(False)
        self.end_date_label.setVisible(False)
        self.day_radio.setVisible(True)
        self.month_radio.setVisible(True)
        self.year_radio.setVisible(True)

        self.default_filter_radiobtn.toggled.connect(self.default_mode)
        self.custom_filter_radiobtn.toggled.connect(self.custom_mode)
        self.price_start.editingFinished.connect(self.set_minimum_price)
        self.price_end.editingFinished.connect(self.set_maximum_price)
        self.start_input.dateChanged.connect(self.set_minimum_date)
        self.submit_btn.clicked.connect(self.submit_form)

    def default_mode(self):
        self.start_input.setVisible(False)
        self.start_date_label.setVisible(False)
        self.end_input.setVisible(False)
        self.end_date_label.setVisible(False)
        self.day_radio.setVisible(True)
        self.month_radio.setVisible(True)
        self.year_radio.setVisible(True)
    
    def custom_mode(self):
        self.start_input.setVisible(True)
        self.start_date_label.setVisible(True)
        self.end_input.setVisible(True)
        self.end_date_label.setVisible(True)
        self.day_radio.setVisible(False)
        self.month_radio.setVisible(False)
        self.year_radio.setVisible(False)

    def set_minimum_price(self):
        self.price_end.setMinimum(self.price_start.value())

    def set_maximum_price(self):
        self.price_start.setMaximum(self.price_end.value())

    def set_minimum_date(self):
        start_date = self.start_input.date()
        self.end_input.setMinimumDate(start_date)

    def set_maximum_date(self):
        end_date = self.end_input.date()
        self.start_input.setMaximumDate(end_date)

    def submit_form(self):
        if self.default_filter_radiobtn.isChecked():
            if self.day_radio.isChecked():
                start_date = datetime.now() - timedelta(days=1)
                end_date = datetime.now()
            elif self.month_radio.isChecked():
                start_date = datetime.now() - timedelta(days=30)
                end_date = datetime.now()
            elif self.year_radio.isChecked():
                start_date = datetime.now() - timedelta(days=365)
                end_date = datetime.now()
        else:
            start_date = datetime.strptime(self.start_input.date().toString("yyyy-MM-dd"), "%Y-%m-%d")
            end_date = datetime.strptime(self.end_input.date().toString("yyyy-MM-dd"), "%Y-%m-%d")
        
        min_price = self.price_start.value()
        max_price = self.price_end.value()
        record_type = "income" if self.income_radio.isChecked() else "expense"
        data_type = self.type_input.currentText()

        if start_date and end_date and min_price is not None and max_price is not None and record_type and data_type:
            form_data = {
                'start_date': start_date,
                'end_date': end_date,
                'min_price': min_price,
                'max_price': max_price,
                'record_type': record_type,
                'data_type': data_type
            }
            results = accounting_manager.search_records(form_data)
            self.populate_table(results)
        else:
            QMessageBox.warning(self, "Input Error", "Please fill all the fields")

    def populate_table(self, records):
        self.results_table.setRowCount(0)
        for record in records:
            row_position = self.results_table.rowCount()
            self.results_table.insertRow(row_position)
            self.results_table.setItem(row_position, 0, QTableWidgetItem(str(record[0])))
            self.results_table.setItem(row_position, 1, QTableWidgetItem(str(record[1])))
            self.results_table.setItem(row_position, 2, QTableWidgetItem(record[2]))
            self.results_table.setItem(row_position, 3, QTableWidgetItem(str(record[3])))
            self.results_table.setItem(row_position, 4, QTableWidgetItem(record[4]))
            self.results_table.setItem(row_position, 5, QTableWidgetItem(record[5]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # data_manager = DataManager()
    # accounting_manager = AccountingManager(data_manager)
    window = Reporting()
    window.show()
    sys.exit(app.exec_())
