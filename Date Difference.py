from datetime import datetime


date1 = input("Enter a date (DD-MM-YYYY format): ")
date2= input("Enter a date (DD-MM-YYYY format): ")

try:
    date_obj = datetime.strptime(date1, "%d-%m-%Y").date()
    date_obj2=datetime.strptime(date2, "%d-%m-%Y").date()
except ValueError:
    print("Incorrect format. Please enter date in DD-MM-YYYY format.")
except NameError:
    print("You Forgot to give one of the dates")    

difference=date_obj-date_obj2
print(f"Difference between two dates is {difference.days}days "
