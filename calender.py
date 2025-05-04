# Ask user for the month number
while True:
    month = int(input("Enter month number (1-12): "))

# Check days based on the month

    if month in [1, 3, 5, 7, 8, 10, 12]:
        print("31 days")
        break
    elif month in [4, 6, 9, 11]:
        print("30 days")
        break
    elif month == 2:
        print("28 or 29 days (February)")
        break
    else:
        print("Invalid month number!")
