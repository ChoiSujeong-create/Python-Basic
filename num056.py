'''2개의 정수값이 입력될 때,
그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.
'''
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and (not b)) or ((not a) and b))

'''참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을
 XOR(exclusive or, 배타적 논리합) 연산이라고도 부른다.'''
