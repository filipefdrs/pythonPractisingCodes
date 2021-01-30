age = int(input())
serviceTime = int(input())

if age == 65 or serviceTime == 30 or (age == 60 and serviceTime == 25):
    print("The employee can retire")
else:
    print("The employee can't retire")
