def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True # divisible by 400, so its a leap year
            else:
                return False # divisible by 100 but not by 400, so its not a leap year
        else:
            return True # divisible by 4 but not by 100, so its a leap year
    else:
        return False # not divisible by 4, so its not a leap year
    
year = int(input("Enter a year: "))
if leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")