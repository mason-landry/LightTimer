import sqlite3
import datetime

conn = sqlite3.connect('my_database.db')
conn.execute('CREATE TABLE settings (start TEXT, stop TEXT)')
conn.execute('CREATE TABLE users (user TEXT, password TEXT)')
conn.execute("insert into users(user, password) values ('admin', 'Weilerstrasse56')")

conn.execute("insert into settings(start, stop) values ('07:00:00', '23:00:00')")


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()