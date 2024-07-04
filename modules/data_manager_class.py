import sqlite3
from datetime import datetime
import pandas as pd

errors = []


class User():
    def __init__(self, fname="", lname="", phone="", username="", email="", password="", city="", birthday="",
                 security="") -> None:
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.username = username
        self.email = email
        self.password = password
        self.city = city
        self.birthday = birthday
        self.security = security


class Record():
    def __init__(self, record_type, username="", amount=0, date="", source="", description="", cost_type="") -> None:
        self.record_type = record_type
        self.username = username
        self.amount = amount
        self.date = date
        self.source = source
        self.description = description
        self.cost_type = cost_type


class DataManager():
    def __init__(self) -> None:
        self.connection = sqlite3.connect('./data/sqlite.db')
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        fname TEXT NOT NULL,
        lname TEXT NOT NULL,
        phone TEXT NOT NULL UNIQUE,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        city TEXT NOT NULL,
        birthday TEXT NOT NULL,
        security_question TEXT NOT NULL
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounting (
        username TEXT NOT NULL,
        amount REAL NOT NULL CHECK(amount > 0),
        date TEXT NOT NULL,
        source TEXT NOT NULL,
        description TEXT NOT NULL,
        cost_type TEXT NOT NULL,
        type TEXT NOT NULL CHECK(type IN ('income', 'expense')),
        FOREIGN KEY(username) REFERENCES users(username)
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
        username TEXT NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        FOREIGN KEY(username) REFERENCES users(username)
        );
        """)

    def is_user_exist(self, user: User):
        global errors
        errors = []

        phone_result = self.cursor.execute("""SELECT * FROM users WHERE phone=?""", (user.phone,))
        if phone_result.fetchone():
            errors.append("Phone number already exists")

        email_result = self.cursor.execute("""SELECT * FROM users WHERE email=?""", (user.email,))
        if email_result.fetchone():
            errors.append("Email already exists")

        username_result = self.cursor.execute("""SELECT * FROM users WHERE username=?""", (user.username,))
        if username_result.fetchone():
            errors.append("Username already exists")

        return errors

    def sign_up_user(self, user: User) -> None:
        self.cursor.execute(
            """INSERT INTO users (fname, lname, phone, username, email, password, city, birthday, security_question) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (user.fname, user.lname, user.phone, user.username, user.email, user.password, user.city, user.birthday,
             user.security))
        self.connection.commit()

    def log_in_user(self, user: User):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (user.username,))
        result = self.cursor.fetchone()
        if result:
            return {"result": True, "user_info": result} if result[5] == user.password else {"result": False,
                                                                                             "error": "wrong password"}
        else:
            return {"result": False, "error": "username not found"}

    def find_password(self, user: User):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (user.username,))
        result = self.cursor.fetchone()
        if result:
            return {"result": True, "password": result[5]} if result[8] == user.security else {"result": False,
                                                                                               "error": "wrong security answer"}
        else:
            return {"result": False, "error": "username not found"}


class AccountingManager():
    def __init__(self, connection) -> None:
        self.connection = connection
        self.cursor = self.connection.cursor()

    def add_record(self, record: Record):
        self.cursor.execute(
            """INSERT INTO accounting (username, amount, date, source, description, cost_type, type) VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (record.username, record.amount, record.date, record.source, record.description, record.cost_type,
             record.record_type))
        self.connection.commit()

    def add_recordd(self, record: Record):
        self.cursor.execute(
            """INSERT INTO accounting (username, amount, date, source, description, cost_type, type) VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (record.username, record.amount, record.date, record.source, record.description, record.cost_type,
             record.record_type))
        self.connection.commit()

    def get_records_by_user(self, username):
        self.cursor.execute("SELECT * FROM accounting WHERE username=?", (username,))
        return self.cursor.fetchall()

    def get_income_by_user(self, username):
        self.cursor.execute("SELECT * FROM accounting WHERE username=? AND type='income'", (username,))
        return self.cursor.fetchall()

    def get_expenses_by_user(self, username):
        self.cursor.execute("SELECT * FROM accounting WHERE username=? AND type='expense'", (username,))
        return self.cursor.fetchall()

    def searching(self, username, search_term, min_amount, max_amount, list_of_type, list_of_field, time_limit):
        types_str = ','.join(['?' for _ in range(len(list_of_type))])
        query = f"SELECT {', '.join(list_of_field)} FROM accounting WHERE username=? AND amount BETWEEN ? AND ? AND type IN ({types_str})"
        parameters = (username, min_amount, max_amount, *list_of_type)
        self.cursor.execute(query, parameters)
        results1 = self.cursor.fetchall()

        query = f"SELECT * FROM accounting WHERE username=? AND amount BETWEEN ? AND ? AND type IN ({types_str})"
        parameters = (username, min_amount, max_amount, *list_of_type)
        self.cursor.execute(query, parameters)
        results = self.cursor.fetchall()

        primary_filter = []
        secondary_filter = []
        for Tuple in range(len(results)):
            for member in results[Tuple]:
                if list_of_field[0] == "*":
                    if search_term == member:
                        primary_filter.append(results[Tuple])
                else:
                    if search_term == member and search_term == results1[Tuple][0]:
                        primary_filter.append(results[Tuple])

        for Tuple in primary_filter:
            if days_between_today_and_date(Tuple[2]) <= time_limit:
                secondary_filter.append(Tuple)

        return secondary_filter

    def search_records(self, form_data):
        self.cursor.execute(' SELECT * FROM accounting WHERE username=? AND amount BETWEEN ? AND ? AND cost_type = ? AND type = ? ',
                            (form_data["user"], form_data['min_price'], form_data['max_price'],
                             form_data['data_type'], form_data["record_type"]))
        records = self.cursor.fetchall()
        return [record for record in records if
                form_data["start_date"] < datetime.strptime(record[2], '%Y-%m-%d') < form_data["end_date"]]

    def delete_account(self, username):
        self.cursor.execute("DELETE FROM users WHERE username = ?;", (username,))
        self.cursor.execute("DELETE FROM accounting WHERE username = ?;", (username,))
        self.connection.commit()

    def delete_records(self, username, type):
        self.cursor.execute("DELETE FROM accounting WHERE username = ? AND type = ?;", (username, type))
        self.connection.commit()

    def edit_information(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        information = self.cursor.fetchall()
        self.cursor.execute("DELETE FROM users WHERE username = ?;", (username,))
        self.connection.commit()
        return information
    
    def export_account(self, user_name):
        self.cursor.execute("SELECT * FROM accounting WHERE username=?", (user_name, ))
        result = self.cursor.fetchall()
        df = pd.DataFrame({
            "amount": [row[1] for row in result],
            "date": [row[2] for row in result],
            "source": [row[2] for row in result],
            "description": [row[3] for row in result],
            "cost_type": [row[4] for row in result],
            "type": [row[5] for row in result],
        })
        df.to_csv("./data/transaction.csv")


class CategoryManager():
    def __init__(self, data_manager) -> None:
        self.connection = data_manager.connection
        self.cursor = self.connection.cursor()

    def add_category(self, username, title, description):
        self.cursor.execute(
            """INSERT INTO categories (username, title, description) VALUES (?, ?, ?)""",
            (username, title, description))
        self.connection.commit()
        return {"result": True}

    def find_category(self, title):
        self.cursor.execute("SELECT * FROM categories WHERE title=?", (title,))
        result = self.cursor.fetchone()
        return {"result": True, "data": result} if result else {"result": False}

    def edit_category(self, title, des):
        self.cursor.execute(" UPDATE categories SET description = ? WHERE title = ?", (des, title))
        self.connection.commit()
        return {"result": True}

    def all_catogory_title(self, username):
        self.cursor.execute("SELECT * FROM categories WHERE username=? ", (username, ))
        result = self.cursor.fetchall()
        return result


def days_between_today_and_date(target_date):
    target_date = datetime.strptime(target_date, "%Y-%m-%d")
    today_date = datetime.today()
    delta = today_date - target_date
    return delta.days

data_manager = DataManager()
accounting_manager = AccountingManager(data_manager.connection)
category_manager = CategoryManager(data_manager)
