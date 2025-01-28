import sqlite3

class SQLParser:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def fetch_data(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
