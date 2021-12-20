w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)
result = (w*h*b)/8/1024/1024
print(format(result, ".2f"), 'MB', sep=' ')

#round(실수, n)
# 소수점을 n번째 까지만 표현하고 반올림을 하고싶을때, round 함수를 사용하면된다.
# print(format(a, ".2f"))
