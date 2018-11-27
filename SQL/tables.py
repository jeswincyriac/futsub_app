import sqlite3

conn=sqlite3.connect('Main.db')

c=conn.cursor()


#c.execute('''CREATE TABLE channel1 (channel_name text NOT NULL PRIMARY KEY, no_subs INTEGER, avg_viewers INTEGER, avg_rating INTEGER)''')

#c.execute('''CREATE TABLE customers1 (cust_name text NOT NULL PRIMARY KEY)''')


c.execute('''CREATE TABLE ratings3 ( channel_name text, cust_name text, ratings INTEGER, FOREIGN KEY (channel_name) REFERENCES "channel1" ([channel_name]),FOREIGN KEY (cust_name) REFERENCES "customer"([cust_name]) )''')




# Run the file and remove the comments from it, thereadter.
conn.commit()
# updated
conn.close()
