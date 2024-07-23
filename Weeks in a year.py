from datetime import datetime

user_input = input("Enter the year and month (YYYY-MM format): ")

try:
    
    date_obj = datetime.strptime(user_input, "%Y-%m").date()
    
    next_year = date_obj.year + 1
    jan1_current_year = datetime(date_obj.year, 1, 1).date()
    jan1_next_year = datetime(next_year, 1, 1).date()
    
    days_in_year = (jan1_next_year - jan1_current_year).days
    

    weeks = days_in_year // 7
    
    print(f"Weeks in {user_input}: {weeks}")

except ValueError:
    print("Please provide the year and month in the correct format (YYYY-MM)")

