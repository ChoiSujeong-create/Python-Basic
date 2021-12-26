h, w = map(int, input().split())
n = int(input())
mylist = []
for i in range(h):
    mylist.append([])
    for j in range(w):
        mylist[i].append(0)

for j in range(n):
    i, d, x, y = map(int, input().split())
    if d == 0:
        for k in range(i):
            mylist[(x-1)][(y-1)+k] = 1
    elif d == 1:
        for k in range(i):
            mylist[(x-1)+k][(y-1)] = 1

for i in range(h):
    for j in range(w):
        print(mylist[i][j], end=' ')
    print(end='\n')
