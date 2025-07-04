import mysql.connector


my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="kokykoky123456654321@",
    database="alx_book_store"
)

if my_db.is_connected():
    print("Database 'alx_book_store' created successfully!")
else:
    print("Failed to connect to the database")
    
my_db.close()