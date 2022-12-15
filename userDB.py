import sqlite3  
  
con = sqlite3.connect("UserDB.db")  
print("Database opened successfully")  
  
con.execute("create table user(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL,subject TEXT NOT NULL, message TEXT NOT NULL)")  
# con.execute("alter table MYAT add phone INTEGER NOT NULL")  
  
print("Table created successfully")  
  
con.close()  