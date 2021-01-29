seconds = int(input())

hours = int(seconds/3600)
minuts = int((seconds - hours * 3600) / 60)
seconds = seconds - (hours * 3600 + minuts * 60)

print(hours, "hour(s)")
print(minuts, "minut(s)")
print(seconds, "second(s)")
