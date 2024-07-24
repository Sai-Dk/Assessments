
my_list = [21, 18, 6, 24, 31]

def insert(x, idx):
    if idx <= len(my_list):
        my_list.insert(idx, x)
        print("List after insertion at index:", my_list)
    else:
        print("Index out of range")

def delete(x):
    if x in my_list:
        my_list.remove(x)
    else:
        print("Element not found in the list")
    return my_list


def add(x):
    my_list.append(x)
    return my_list


def sort_list():
    my_list.sort()
    return my_list


def remove_by_index(x):
    if x < len(my_list):
        my_list.pop(x)
    else:
        print("Index out of range")
    return my_list


def reverse_list():
    my_list.reverse()
    return my_list

# Dictionary mapping operation codes to function names
operations = {
    1: insert,
    2: delete,
    3: add,
    4: sort_list,
    5: remove_by_index,
    6: reverse_list,
}

def switch(operation_code):
    try:
        operation_code = int(operation_code)
        if operation_code in operations:
            if operation_code == 1 or operation_code == 3:
                number = int(input("Enter the number to operate on: "))
                index = int(input("Enter the index to insert at: "))
                operations[operation_code](number, index)
            elif operation_code == 2:
                number = int(input("Enter the number to delete: "))
                operations[operation_code](number)
                print("List after deletion",my_list)
            elif operation_code == 4 or operation_code == 6:
                result = operations[operation_code]()
                print("Resulting list:", result)
            elif operation_code == 5:
                index = int(input("Enter the index to remove: "))
                operations[operation_code](index)
            else:
                print("Invalid operation code")
        else:
            print("Invalid operation code")
    except ValueError:
        print("Invalid input. Please enter a valid operation code.")


user_input = input("""Enter the operation you want to perform:
                 1-insert, 2-delete, 3-add, 4-sort, 5-remove, 6-reverse
                 """)


switch(user_input)
