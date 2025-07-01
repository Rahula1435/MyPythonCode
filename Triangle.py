angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))

sum_angles = angle1 + angle2 + angle3

if sum_angles == 180:
    print("The triangle is valid")
else:
    print("The triangle is not valid")
