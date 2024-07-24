import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123654",
  database="mydatabase"
)


cursor = mydb.cursor()

# Create users table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        address VARCHAR(255) NOT NULL
    )
''')

# Function to insert user into the database
def insert_user(name, email, address):
    try:
        sql = "INSERT INTO users (name, email, address) VALUES (%s, %s, %s)"
        val = (name, email, address)
        cursor.execute(sql, val)
        mydb.commit()
        print("User inserted successfully!")
    except mysql.connector.Error as err:
        if err.errno == 1062:  # MySQL error number for duplicate entry
            print(f"Error: Email ID '{email}' already exists.")
        else:
            print(f"Error: {err}")

# Get user input
name = input("Enter name: ")
email = input("Enter email ID: ")
address = input("Enter address: ")

# Call insert_user function
insert_user(name, email, address)

# Close cursor and connection
cursor.close()
mydb.close()




