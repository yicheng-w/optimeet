import sqlite3

conn = sqlite3.connect("./db/database.db")

c = conn.cursor()

create_base = "CREATE TABLE %s (%s)" # no user input needed, use %s

 # password = hexstring of hash
c.execute(create_base % ("events", "id INTEGER, auth_code TEXT, name TEXT"))

# note will be html source code with markup
c.execute(create_base % ("people", "id INTEGER, name TEXT, long REAL, lat REAL"))
