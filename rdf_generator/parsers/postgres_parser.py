import psycopg2
from psycopg2.extras import RealDictCursor


class PostgreSQLParser:
    def __init__(self, host, database, user, password, port=5432):
        """
        Initialize the PostgreSQL connection.
        """
        self.conn = None
        try:
            self.conn = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password,
                port=port
            )
            print(f"Connected to the database: {database}")
        except Exception as e:
            raise Exception(f"Error connecting to the database: {e}")

    def fetch_data(self, query):
        """
        Execute a SQL query and fetch data as a list of dictionaries.
        """
        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            raise Exception(f"Error executing query: {e}")

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
