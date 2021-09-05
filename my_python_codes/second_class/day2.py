import sqlite3
conn = sqlite3.connect(r'lesson3.db')
cursor = conn.cursor()
cursor.execute(""" DELETE TABLE Clients """)
result = cursor.fetchall()
# list(map(lambda x: print(x), result))
conn.commit()

