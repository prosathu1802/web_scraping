import sqlite3

conn = sqlite3.connect("mydatabase.db")

# Create a table
conn.execute('''CREATE TABLE celebs 
            (name text, networth int)''')
