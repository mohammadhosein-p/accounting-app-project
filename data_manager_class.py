import sqlite3
from datetime import datetime

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
    def __init__(self, record_type, username="", amount=0, date="", source="", description="") -> None:
        self.record_type = record_type
        self.username = username
        self.amount = amount
        self.date = date
        self.source = source
        self.description = description


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

        # Check if phone number already exists
        phone_result = self.cursor.execute("""SELECT * FROM users WHERE phone=?""", (user.phone,))
        if phone_result.fetchone():
            errors.append("Phone number already exists")

        # Check if email already exists
        email_result = self.cursor.execute("""SELECT * FROM users WHERE email=?""", (user.email,))
        if email_result.fetchone():
            errors.append("Email already exists")

        # Check if username already exists
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

    def log_in_user(self, user:User):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (user.username, ))
        result =  self.cursor.fetchone()
        if result:
            return {"result": True, "user_info": result} if result[5] == user.password else {"result": False, "error": "wrong password"}
        else:
            return {"result": False, "error": "username not found"}

    def find_password(self, user:User):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (user.username ,))
        result = self.cursor.fetchone()
        if result:
            return {"result": True, "password": result[5]} if result[8]==user.security else {"result": False, "error": "wrong security answer"}
        else:
            return {"result": False, "error": "username not found"}


class AccountingManager():
    def __init__(self, connection) -> None:
        self.connection = connection
        self.cursor = self.connection.cursor()

    def add_record(self, record: Record):
        self.cursor.execute(
            """INSERT INTO accounting (username, amount, date, source, description, type) VALUES (?, ?, ?, ?, ?, ?)""",
            (record.username, record.amount, record.date, record.source, record.description, record.record_type))
        self.connection.commit()

    def add_recordd(self, record: Record):
        self.cursor.execute(
            """INSERT INTO accounting (username, amount, date, source, description, type) VALUES (?, ?, ?, ?, ?, ?)""",
            (record.username, record.amount, record.date, record.source, record.description, record.record_type))
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

        # return results
        filtered_results = []
        z = []
        for i in range(len(results)):
            for j in results[i]:
                if list_of_field[0] == "*":
                    if search_term == j:
                        filtered_results.append(results[i])
                else:
                    if search_term == j and search_term == results1[i][0]:
                        filtered_results.append(results[i])

        for i in filtered_results:
            if days_between_today_and_date(i[2]) <= time_limit:
                z.append(i)

        return z

class CategoryManager():
    def __init__(self, data_manager) -> None:
        self.connection = data_manager.connection
        self.cursor = self.connection.cursor()

    def add_category(self, username, title, description):
        self.cursor.execute(
        """INSERT INTO categories (username, title, description) VALUES (?, ?, ?)""",
        (username, title, description))
        self.connection.commit()
        return {"result" : True}

    def find_category(self, title):
        self.cursor.execute("SELECT * FROM categories WHERE title=?", (title,))
        result = self.cursor.fetchone()
        return {"result": True, "data": result} if result else {"result": False}

    def edit_category(self, title, des):
        self.cursor.execute(" UPDATE categories SET description = ? WHERE title = ?", (des, title))
        self.connection.commit()
        return {"result" : True}
    
    def all_catogory_title(self):
        self.cursor.execute("SELECT title FROM categories WHERE username=? ",("username", ))
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

# test commands
# data_manager.sign_up_user(User("a", "b", "091521", "as", "asd", "qwerty", "asd", "asdf", "qe"))
# print(data_manager.find_password(User(username="as", security="qe")))
# print(data_manager.is_user_exist(User(phone="09", username="a", email="asd")))
# print(data_manager.log_in_user(User(username="as", password="qwerty")))
# accounting_manager = AccountingManager(data_manager.connection)
# data_manager.sign_up_user(
#     User("ali", "Doe", "09152541", "alidoe", "johrerg", "password123", "sdfg", "1990-01-01", "sdfvcx"))
# accounting_manager.add_record(
#     Record(username="alidoe", amount=1000.0, date="2024-05-28", source="salary", description="fhnfnfd",
#            record_type="income"))
# print(accounting_manager.get_records_by_user("alidoe"))
