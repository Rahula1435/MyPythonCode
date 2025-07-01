marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("Percentage:", percentage)

if percentage >= 60:
    print("First Division")
elif percentage >= 50:
    print("Second Division")
elif percentage >= 40:
    print("Third Division")
else:
    print("Fail")
