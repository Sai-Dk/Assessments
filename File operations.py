
def file_read(file_name):
    with open(file_name, "r") as file:
        return file.read()
    
def file_write(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)

file_name = "User_data.txt"

user_input = input("Enter the text you want to store in a file: ")
file_write(file_name, user_input)

output = file_read(file_name)
print("Data stored in the file:")
print(output)
