# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합 구하기
n = int(input())
n_sum = 0

for i in range(n+1):
    if i % 2 == 0:
        n_sum += i
print(n_sum)
