#!/usr/bin/env python3.6
import sqlite3


conn = sqlite3.connect('list.db')


c = conn.cursor()


c.execute('''CREATE TABLE words
             (id, wordname)''')

c.execute("INSERT INTO words VALUES ('','ahmet')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
