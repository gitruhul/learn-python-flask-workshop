import os
import sqlite3

# filename to form database
def init_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(f"Database {db_file} is initialized at {os.path.realpath(os.path.dirname(__file__))}")
        return conn
    except Exception as e:
        print(f"Database {db_file} is not initialized. Error: {e}")
        return None

def create_table(conn, table, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print(f"Table {table} is created.")
    except Exception as e:
        print(f"Error while creating table {table}. {e}")
