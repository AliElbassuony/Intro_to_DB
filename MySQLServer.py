import mysql.connector
from mysql.connector import Error

try:
  mydb = mysql.connector.connect(host="localhost",user="root",passwd="password",database="alx_book_store")
  if mydb.is_connected():
     print("Database 'alx_book_store' created successfully!")
     mydb.close()
except Error as e:
     print(f"Error while connecting to MySQL: {e}")
