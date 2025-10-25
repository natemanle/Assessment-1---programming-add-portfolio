months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
} #stores the values as pairs


month_number = int(input("Enter the month number (1-12): ")) #user gives a number from 1 to 12


if month_number in months: #depending on the users input it will give the respective day, if user goes over 12 text"Invalid month number. Please enter a number between 1 and 12." will appear
    print(f"Month {month_number} has {months[month_number]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
