import sqlite3

conn=sqlite3.connect('Main.db')

c=conn.cursor()

print(c.execute('''SELECT * from ratings3''').fetchall())

conn.commit()
# updated
conn.close()
