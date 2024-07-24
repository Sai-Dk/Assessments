my_dict = {
    'apple': 10,
    'banana': 20,
    'cherry': 30,
    'date': 40,
    'elderberry': 40
}

user_input = input("Enter the key you want to display from the dictionary: ")

def display_value(dictionary, key):
    if key in dictionary:
        value = dictionary[key]
        print(f"The value for key '{key}' is: {value}")
    else:
        print(f"Key '{key}' not found in the dictionary")

# Call the function to display the value
display_value(my_dict, user_input)


    






# Write a program to filter and display the values from dictionary based on given input
