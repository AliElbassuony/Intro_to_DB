import mysql.connector


try:
  mydb = mysql.connector.connect(host="localhost",user="root",passwd="password",database="alx_book_store")
  if mydb.is_connected():
     cursor = mydb.cursor()
     cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
     print("Database 'alx_book_store' created successfully!")
     cursor.close()
     mydb.close()
except mysql.connector.Error as e:
     print(f"Error while connecting to MySQL: {e}")
