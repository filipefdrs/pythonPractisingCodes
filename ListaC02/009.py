salary = float(input())
loanProvision = float(input())

if loanProvision > salary * 0.2:
    print("Not given loan")
else:
    print("Given loan")
