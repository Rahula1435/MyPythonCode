year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leep year")
else:
    print(f"{year} is'nt a leap year")
