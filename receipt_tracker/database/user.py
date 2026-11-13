import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection_obj = sqlite3.connect('receipts.db')

# Create a cursor object to interact with the database
cursor_obj = connection_obj.cursor()

cursor_obj.execute("DROP TABLE IF EXISTS User")

# SQL query to create the table
table_creation_query = """
    CREATE TABLE User (
        User_Id INTEGER PRIMARY KEY,
        User_Name CHAR(25),
        Credit_Card_Number INTEGER
    );
"""

# Execute the table creation query
cursor_obj.execute(table_creation_query)

# Confirm that the table has been created
print("Table is Ready")

# Close the connection to the database
connection_obj.close()