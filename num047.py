# 정수 2개(a, b)를 입력받아 a를 2^b배 곱한 값으로 출력
a, b = input().split()
print(int(a)*(1 << int(b)))
