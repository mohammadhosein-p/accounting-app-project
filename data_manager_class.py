import sqlite3

class User():
    def __init__(self, fname="", lname="", phone="", username="", email="", password="", city="", birthday="", security="") -> None:
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
    def __init__(self, record_type, username="", amount=0 , date="", source="", description="") -> None:
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

    def is_user_exist(self, user:User):
        prams_to_check = ["phone", "username", "email"]
        for pram in prams_to_check:
            self.cursor.execute(f"SELECT * FROM users WHERE {pram}=? ", (getattr(user, pram), ))
            result = self.cursor.fetchone()
            if result:
                return {"result": True, "duplicate": pram}
        return {"result":False}

    def sign_up_user(self, user:User)->None:
        self.cursor.execute(
        """INSERT INTO users (fname, lname, phone, username, email, password, city, birthday, security_question) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (user.fname, user.lname, user.phone, user.username, user.email, user.password, user.city, user.birthday, user.security))
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

    def add_record(self, record:Record):
        self.cursor.execute(
        """INSERT INTO accounting (username, amount, date, source, description, type) VALUES (?, ?, ?, ?, ?, ?)""",
        (record.username, record.amount, record.date, record.source, record.description, record.record_type))
        self.connection.commit()

    def get_records_by_user(self, username):
        self.cursor.execute("SELECT * FROM accounting WHERE username=?", (username,))
        result = self.cursor.fetchall()
        return {"result": True, "data": result} if result else {"result": False}

    def get_income_by_user(self, username):
        self.cursor.execute("SELECT * FROM accounting WHERE username=? AND type='income'", (username,))
        result = self.cursor.fetchall()
        return {"result": True, "data": result} if result else {"result": False}
    
    def get_expenses_by_user(self, username):
        self.cursor.execute("SELECT * FROM accounting WHERE username=? AND type='expense'", (username,))
        result = self.cursor.fetchall()
        return {"result": True, "data": result} if result else {"result": False}
    
# if __name__ =="__main__":
#     data_manager = DataManager()
   
#     # test commands
#     data_manager.sign_up_user(User("a", "b", "091521", "as", "asd", "qwerty", "asd", "asdf", "qe"))
#     print(data_manager.find_password(User(username="as", security="qe")))
#     print(data_manager.is_user_exist(User(phone="09", username="a", email="asd")))
#     print(data_manager.log_in_user(User(username="as", password="qwerty")))
#     accounting_manager = AccountingManager(data_manager.connection)
#     data_manager.sign_up_user(User("ali", "Doe", "09152541", "alidoe", "johrerg", "password123", "sdfg", "1990-01-01", "sdfvcx"))
#     accounting_manager.add_record(Record(username="alidoe", amount=1000.0, date="2024-05-28", source="salary", description="fhnfnfd", record_type="income"))
#     print(accounting_manager.get_records_by_user("alidoe"))
