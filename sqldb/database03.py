#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT OR IGNORE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")

conn.execute("INSERT OR IGNORE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

conn.execute("INSERT OR IGNORE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

conn.execute("INSERT OR IGNORE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

conn.commit()
print("Records created successfully")
conn.close()

