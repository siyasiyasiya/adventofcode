with open("input.txt", 'r') as f:
    wall = [list(line.strip('\n')) for line in f]
    print(wall)

#part 1
rows = len(wall)
cols = len(wall[0])

print(rows)
print(cols)
def valid_remove(i, j):
    count = 0
    if wall[i][j] == ".":
        return 0
    
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            
            nr, nc = i + dr, j + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if wall[nr][nc] == "@":
                        count += 1

    if count < 4:
        print(i, j)
        return 1

    return 0

rolls = 0
for i in range(0, rows):
    for j in range(0, cols):
        rolls += valid_remove(i, j)


print(rolls)