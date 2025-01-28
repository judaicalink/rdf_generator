import mysql.connector
from mysql.connector import Error


class MySQLParser:
    def __init__(self, host, database, user, password, port=3306):
        """
        Initialize the MySQL connection.
        """
        self.conn = None
        try:
            self.conn = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password,
                port=port
            )
            if self.conn.is_connected():
                print(f"Connected to the database: {database}")
        except Error as e:
            raise Exception(f"Error connecting to the database: {e}")

    def fetch_data(self, query):
        """
        Execute a SQL query and fetch data as a list of dictionaries.
        """
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            raise Exception(f"Error executing query: {e}")
        finally:
            cursor.close()

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Database connection closed.")

