a, m, d, n = input().split()
a = int(a)
m = int(m)
n = int(n)
d = int(d)

for i in range(1, n):
    a = (a*m)+d
print(a)
