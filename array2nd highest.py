array_length = int(input("Enter the length of the array: "))

array = []
for i in range(array_length):
    value = int(input("Enter the value to input: "))
    array.append(value)

print("Array:", array)

# Check if array has at least two elements
if len(array) >= 2:
    array.sort()
    print("Second highest of the array is:", array[-2])
else:
    print("Array should have at least two elements to find the second highest.")


    















