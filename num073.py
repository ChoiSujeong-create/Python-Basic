'''
c = ord(input())
t = ord('a')
while t <= c:
    print(chr(t), end=' ')
    t += 1
'''
'''알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있다.
chr(정수값)을 이용하면 유니코드 문자로 출력할 수 있다.
print(..., end=' ') 와 같이 작성하면 값 출력 후 공백문자 ' '를 출력한다. 즉, 마지막에 줄을 바꾸지 않고 빈칸만 띄운다.'''

n = int(input())
while n > 0:
    n -= 1
    print(n)
