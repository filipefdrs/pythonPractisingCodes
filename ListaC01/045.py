letterNumber  = ord(input())

counter = 0
sentinel = 65
while sentinel >= 65 and sentinel <= 90 and sentinel != letterNumber:
    counter = counter + 1
    sentinel = sentinel + 1

lowerCase = chr(97 + counter)
print(lowerCase)
