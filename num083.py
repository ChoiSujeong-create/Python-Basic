#  3 6 9 게임의 왕이 되자(설명)
r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
cnt = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            cnt += 1
print(cnt)
