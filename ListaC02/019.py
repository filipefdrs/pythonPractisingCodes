number = int(input())
counter = 0
control = ''

if number % 3 == 0:
    counter = counter + 1
    control = '3'
if number % 5 == 0:
    counter = counter + 1
    control = '5'

if counter == 1:
    print(number, "is divisible by", int(control))

if counter == 2:
    print(number, "is divisible by both")

if counter == 0:
    print(number, "isn't divisible by any of both")
