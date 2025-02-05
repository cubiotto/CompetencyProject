import sqlite3


class DatabaseConnection:
    def __init__(self, db_path):
        self.db_path = db_path

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()

    # Category Handle
    def insert_category(self, data):
        with self as cursor:
            cursor.execute("INSERT INTO Category (category_name) VALUES (?)", (data,))

    def get_categories(self):
        with self as cursor:
            cursor.execute("SELECT * FROM Category")
            return cursor.fetchall()
