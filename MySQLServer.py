import mysql.connector
# from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',    
            password='your_password' 
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        else:
            print("Failed to connect to MySQL server.")
    
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


create_database()
