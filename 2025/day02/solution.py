with open("input.txt") as f:
    ranges = f.read().strip().split(",")

#part 1
sum = 0
for r in ranges:
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])

    for i in range(start, end + 1):
        num = str(i)
        length = len(num)
        mid = length // 2

        first = num[:mid]
        sec = num[mid:]

        if first == sec:
            sum += i

print(sum)

#part 2
import re 

sum = 0
for r in ranges:
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])

    for i in range(start, end + 1):
        num = str(i)
        pattern = r"^(\d+)\1+$" 
        if bool(re.match(pattern, num)):
            sum += i

print(sum)
