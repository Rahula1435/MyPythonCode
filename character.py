ch = input("Enter any character: ")

if 'A' <= ch <= 'Z':
    print("Capital Letter")
elif 'a' <= ch <= 'z':
    print("Small Case Letter")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special Symbol")
