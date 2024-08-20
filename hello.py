import sqlite3

connection = sqlite3.connect('my_database.db')

print('Hello, World!')

connection.close()