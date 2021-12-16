# 정수 3개 입력받아 합과 평균 출력
n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
print(n1+n2+n3, format((n1+n2+n3)/3, ".2f"))
