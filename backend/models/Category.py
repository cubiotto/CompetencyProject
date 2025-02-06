from tkinter import messagebox


class Category:
    def __init__(self,db_connection, category_id=None, category_name=None):
        self.db_connection = db_connection
        self.category_id = category_id
        self.category_name = category_name

    def save_category(self):
        """Insert a new category into the database."""
        if self.category_id is None:
            with self.db_connection as cursor:
                cursor.execute('INSERT INTO Category(category_name) VALUES (?)', (self.category_name,))
                self.category_id = cursor.lastrowid
        else:
            raise ValueError('Category already exists')

    def update_category(self,new_category_name):
        """Update the category name in the database."""
        if self.category_id is not None:
            with self.db_connection as cursor:
                cursor.execute('UPDATE Category SET category_name = ? WHERE category_id = ?', (new_category_name, self.category_id))
                self.category_name = new_category_name
        else:
            raise ValueError('Cannot update a category without an ID')

    @staticmethod
    def fetch_all(db_connection):
        """Fetch all categories from the database."""
        with db_connection as cursor:
            cursor.execute("SELECT * FROM Category")
            rows = cursor.fetchall()
            return [Category(db_connection, category_id=row['category_id'], category_name=row['category_name']) for row in rows]

    @staticmethod
    def fetch_by_id(db_connection, category_id):
        """Fetch a category by its ID."""
        with db_connection as cursor:
            cursor.execute("SELECT * FROM Category WHERE category_id = ?", (category_id,))
            row = cursor.fetchone()
            if row:
                return Category(db_connection, category_id=row['category_id'], category_name=row['category_name'])
            return None

    def __repr__(self):
        return f"Category(category_id={self.category_id}, category_name='{self.category_name}')"