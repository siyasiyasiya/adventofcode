with open("input.txt", 'r') as f:
    wall = [list(line.strip('\n')) for line in f]
    print(wall)

#part 1
rows = len(wall)
cols = len(wall[0])

remove = []

def valid_remove(i, j):
    count = 0
    if wall[i][j] == "." or wall[i][j] == "x":
        return 0
    
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            
            nr, nc = i + dr, j + dc
            if 0 <= nr < rows and 0 <= nc < cols and wall[nr][nc] == "@":
                    count += 1

    if count < 4:
        remove.append((i, j))
        return 1

    return 0

rolls = 0
for i in range(0, rows):
    for j in range(0, cols):
        rolls += valid_remove(i, j)

print(rolls)

#part 2
rolls = 0
run = -1
while not run == 0:
    run = 0
    remove = []
    for i in range(0, rows):
        for j in range(0, cols):
            run += valid_remove(i, j)

    for i, j in remove:
        wall[i][j] = "x"

    rolls += run

print(rolls)