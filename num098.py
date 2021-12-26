d = []
for i in range(10):
    d.append(list(map(int, input().split())))
x, y = 1, 1

while True:
    if d[x][y] == 0:
        d[x][y] = 9
    elif d[x][y] == 2:
        d[x][y] = 9
        break

    if d[x][y+1] != 1:
        y = y+1
    elif d[x][y+1] == 1:
        if d[x+1][y] != 1:
            x = x+1
        elif d[x+1][y] == 1:
            break

for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()
