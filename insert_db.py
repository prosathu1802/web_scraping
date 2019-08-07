import sqlite3

conn = sqlite3.connect("mydatabase.db")
a = "Im a Data"
b= "Im also a Data"
conn.execute("INSERT INTO celebs VALUES " + str((a, 100000000 )))
conn.execute("INSERT INTO celebs VALUES ('b', 230000 )")
# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it
# Just be sure any changes have been commited or they will be lost.
conn.close()
