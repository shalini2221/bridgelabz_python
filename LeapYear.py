import C:\Users\hp\Downloads\BL Python programs\Utility.py
Utility utility = new Utility()

def is_leap_year(year):
    
    if year < 1582:
        return "Invalid input: Year must be 1582 or later (Gregorian calendar)."
    elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a Leap Year."
    else:
        return f"{year} is Not a Leap Year."

def main():
    try:
        year = utility.inputInteger()
        result = is_leap_year(year)
        print(result)
    except ValueError:
        print("Invalid input: Please enter a valid integer year.")

if __name__ == "__main__":
    main()
