with open("input.txt") as f:
    batteries = f.read().strip().split("\n")

#part 1 
joltage = 0
for battery in batteries:
    first = 0

    for i in range(0, len(battery) - 1):
        if int(battery[i]) > int(battery[first]):
            first = i
        
    second = first + 1
    for i in range(first + 1, len(battery)):
        if int(battery[i]) > int(battery[second]):
            second = i
    
    joltage += int(battery[first] + battery[second])


print(joltage)

#part 2
joltage = 0
for battery in batteries:
    jolt = ""
    last = -1

    for i in range(0, 12):
        current = last + 1
        for j in range(current, len(battery) - 11 + i):
            if int(battery[j]) > int(battery[current]):
                current = j

        last = current
        jolt += battery[last]
    
    joltage += int(jolt)


print(joltage)