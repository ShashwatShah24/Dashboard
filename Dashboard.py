import sqlite3  
  
con = sqlite3.connect("DashboardProject.db")  
print("Database opened successfully")  
  
con.execute("create table ProjectTable (id INTEGER PRIMARY KEY AUTOINCREMENT, circle TEXT NOT NULL,authors TEXT NOT NULL,Description TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close()