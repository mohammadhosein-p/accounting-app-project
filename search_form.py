import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, \
    QComboBox, QSpinBox, QMessageBox, QButtonGroup, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QLocale
from math import inf
import git


class SearchFilterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(905, 700)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Search and Filter')
        self.setWindowIcon(QIcon('search.png'))
        self.setGeometry(700, 200, 800, 600)

        self.search_label = QLabel('Search:')
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter search term")

        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.handle_search)

        self.back_button = QPushButton('Back')

        self.day_checkbox = QCheckBox('Daily')
        self.month_checkbox = QCheckBox('Monthly')
        self.year_checkbox = QCheckBox('Yearly')
        self.income_checkbox = QCheckBox('Income')
        self.income_checkbox.setChecked(True)
        self.expense_checkbox = QCheckBox('Expense')
        self.expense_checkbox.setChecked(True)

        self.time_group = QButtonGroup(self)
        self.time_group.addButton(self.day_checkbox)
        self.time_group.addButton(self.month_checkbox)
        self.time_group.addButton(self.year_checkbox)
        self.time_group.setExclusive(True)

        self.amount_min_label = QLabel('Min Amount:')
        self.amount_min_input = QSpinBox()
        self.amount_min_input.setMaximum(1000000000)
        self.amount_min_input.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.amount_max_label = QLabel('Max Amount:')
        self.amount_max_input = QSpinBox()
        self.amount_max_input.setMaximum(1000000000)
        self.amount_max_input.setValue(1000000000)
        self.amount_max_input.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.field_combo = QComboBox()
        self.field_combo.addItems(['All Fields', 'Description', 'Source', 'Type'])

        self.results_table = QTableWidget()
        self.results_table.setColumnCount(7)
        self.results_table.setHorizontalHeaderLabels(
            ['Name', 'Amount', 'Date', 'source', 'Description', 'Type', 'Transaction type'])

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        back_layout = QHBoxLayout()
        back_layout.addWidget(self.back_button)

        filter_layout = QHBoxLayout()
        filter_layout.addWidget(self.day_checkbox)
        filter_layout.addWidget(self.month_checkbox)
        filter_layout.addWidget(self.year_checkbox)
        filter_layout.addWidget(self.income_checkbox)
        filter_layout.addWidget(self.expense_checkbox)

        amount_layout = QHBoxLayout()
        amount_layout.addWidget(self.amount_min_label)
        amount_layout.addWidget(self.amount_min_input)
        amount_layout.addWidget(self.amount_max_label)
        amount_layout.addWidget(self.amount_max_input)

        field_layout = QHBoxLayout()
        field_layout.addWidget(QLabel('Search In:'))
        field_layout.addWidget(self.field_combo)

        main_layout = QVBoxLayout()
        main_layout.addLayout(search_layout)
        main_layout.addLayout(filter_layout)
        main_layout.addLayout(amount_layout)
        main_layout.addLayout(field_layout)
        main_layout.addWidget(self.results_table)
        main_layout.addLayout(back_layout)

        self.setLayout(main_layout)

        self.apply_stylesheet()


    def apply_stylesheet(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #003C43;
                color: #E3FEF7;
                font-family: 'Times New Roman';
                font-size: 16px;
            }
            QLabel {
                color: #E3FEF7;
            }
            QLineEdit, QComboBox, QSpinBox {
                border: 2px solid #135D66;
                border-radius: 10px;
                padding: 5px;
                background-color: #E3FEF7;
                color: #003C43;
            }
            QLineEdit:focus, QComboBox:focus, QSpinBox:focus {
                border: 2px solid red;
            }
            QCheckBox {
                padding: 5px;
                color: #E3FEF7;
            }
            QPushButton {
                background-color: #77B0AA;
                color: white;
                padding: 10px;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #E3FEF7;
                color: #003C43;
            }
            QTableWidget {
                background-color: #E3FEF7;
                color: #003C43;
                border: 2px solid #135D66;
                border-radius: 10px;
            }
            QHeaderView::section {
                background-color: #135D66;
                color: #E3FEF7;
                padding: 5px;
                border: 1px solid #E3FEF7;
            }
        """)

    def handle_search(self):
        list_of_type = []
        time_limit = inf

        search_term = self.search_input.text()
        is_daily = self.day_checkbox.isChecked()
        is_monthly = self.month_checkbox.isChecked()
        is_yearly = self.year_checkbox.isChecked()
        is_income = self.income_checkbox.isChecked()
        is_expense = self.expense_checkbox.isChecked()
        min_amount = self.amount_min_input.value()
        max_amount = self.amount_max_input.value()
        search_field = self.field_combo.currentText()

        if len(search_term) == 0:
            QMessageBox.warning(self, 'Error', 'Please search for something')
            return

        if is_income:
            list_of_type.append("income")
        if is_expense:
            list_of_type.append("expense")

        if search_field == 'All Fields':
            list_of_field = ["*"]
        else:
            list_of_field = [search_field.lower()]

        if is_daily:
            time_limit = 1
        elif is_monthly:
            time_limit = 31
        elif is_yearly:
            time_limit = 365

        search_object = git.accounting_manager.searching("mehdi", search_term, min_amount, max_amount, list_of_type,
                                                         list_of_field, time_limit)
        if len(search_object) == 0:
            QMessageBox.warning(self, 'Error', 'This word not found')
        else:
            self.update_results_table(search_object)

    def update_results_table(self, results):
        self.results_table.setRowCount(len(results))
        for row_idx, row_data in enumerate(results):
            for col_idx, item in enumerate(row_data):
                self.results_table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    search_filter_app = SearchFilterApp()
    search_filter_app.show()
    sys.exit(app.exec_())
