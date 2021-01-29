readHours = int(input())
readMinuts = int(input())
readSeconds = int(input())
elapsedSeconds = int(input())

seconds = elapsedSeconds

hours = int(seconds / 3600)
minuts = int((seconds - hours * 3600) / 60)
seconds = seconds - (hours * 3600 + minuts * 60)

endHours = readHours + hours
endMinuts = readMinuts + minuts
endSeconds = readSeconds + seconds

if endSeconds >= 60:
    endMinuts = endMinuts + int(endSeconds / 60)
    endSeconds = endSeconds - int(endSeconds / 60) * 60

if endMinuts >= 60:
    endHours = endHours + int(endMinuts / 60)
    endMinuts = endMinuts - int(endMinuts / 60) * 60

print(endHours, "hour(s)")
print(endMinuts, "minut(s)")
print(endSeconds, "second(s)")
