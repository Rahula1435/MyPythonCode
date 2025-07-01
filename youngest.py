ram_age = int(input("Enter Ram's age: "))
sulaabh_age = int(input("Enter Sulaabh's age: "))
ajay_age = int(input("Enter Ajay's age: "))

if ram_age < sulaabh_age and ram_age < ajay_age:
    print("Ram is the youngest")
elif sulaabh_age < ram_age and sulaabh_age < ajay_age:
    print("Sulaabh is the youngest")
elif ajay_age < ram_age and ajay_age < sulaabh_age:
    print("Ajay is the youngest")
else:
    print("Two or more have the same youngest age")
