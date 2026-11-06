import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection_obj = sqlite3.connect('reciepts.db')

# Create a cursor object to interact with the database
cursor_obj = connection_obj.cursor()

# Drop the RECIEPT table if it already exists (for clean setup)
cursor_obj.execute("DROP TABLE IF EXISTS RECIEPT")

# SQL query to create the table
table_creation_query = """
    CREATE TABLE RECIEPT (
        Id INTEGER PRIMARY KEY,
        User_Name CHAR(25),
        Date TEXT,
        Credit_Card_Number INT
    );
"""

# Execute the table creation query
cursor_obj.execute(table_creation_query)

# Confirm that the table has been created
print("Table is Ready")

# Close the connection to the database
connection_obj.close()