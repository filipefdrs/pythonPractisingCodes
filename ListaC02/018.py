number1 = None
number2 = None
op = None
print("================Calculator================")
print("|1 - Add                                 |")
print("|2 - Subtraction                         |")
print("|3 - Product                             |")
print("|4 - Division                            |")
print("==========================================")
op = int(input("Enter operation number: "))

if op == 1:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    print("Sum is", number1 + number2)
elif op == 2:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    print("Subtraction is", number1 - number2)
elif op == 3:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    print("Product is", number1 * number2)
elif op == 4:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    try:
        print("Division is", number1 / number2)
    except Exception as e:
        print("Division by zero is impossible")
else:
    print("Invalid operation")
