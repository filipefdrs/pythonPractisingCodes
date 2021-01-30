grade1 = float(input())
grade2 = float(input())

if grade1 >= 0.0 and grade2 >= 0.0 and grade1 <= 10.0 and grade2 <= 10.0:
    print("Average is", (grade1 + grade2) / 2.0)
else:
    print("One or both is(are) invalid.")
