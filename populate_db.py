import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file} successfully.")
        return conn
    except sqlite3.Error as e:
        print(f"Error while connecting to database: {e}")
    return conn

def create_table(conn, create_table_sql):
    """Create a table from the create_table_sql statement"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(f"Error while creating table: {e}")

def execute_sql_file(conn, sql_file):
    """Execute SQL queries from a .sql file"""
    try:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        
        cursor = conn.cursor()
        cursor.executescript(sql_script)
        print(f"SQL script from {sql_file} executed successfully.")
    except sqlite3.Error as e:
        print(f"Error while executing SQL script: {e}")
    except FileNotFoundError:
        print(f"The file {sql_file} was not found.")

def main():
    database = "db.sqlite3"
    sql_file = "users.sql"

    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    """

    # Create a database connection
    conn = create_connection(database)

    # If connection is successful, create tables
    if conn is not None:
        # Create users table
        create_table(conn, sql_create_users_table)
        execute_sql_file(conn,sql_file)
    else:
        print("Error! Cannot create the database connection.")

    # Close the connection when done
    if conn:
        conn.close()

if __name__ == '__main__':
    main()
