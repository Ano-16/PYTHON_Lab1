def is_leap_year(year):
    """Determine if the year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(month, year=None):
    month_days = {
        "january": 31,
        "february": 28,  # 29 in a leap year
        "march": 31,
        "april": 30,
        "may": 31,
        "june": 30,
        "july": 31,
        "august": 31,
        "september": 30,
        "october": 31,
        "november": 30,
        "december": 31
    }

    month = month.lower()  # Convert month name to lowercase

    if month not in month_days:
        raise ValueError("Invalid month name")

    if month == "february" and year is not None and is_leap_year(year):
        return 29

    return month_days[month]

month_name = input("Enter the month name: ").strip()

# For February, input year to check for leap year
if month_name.lower() == "february":
    year = int(input("Enter the year: "))
    days = get_days_in_month(month_name, year)
else:
    days = get_days_in_month(month_name)

print(f"The number of days in {month_name.capitalize()} is: {days}")
