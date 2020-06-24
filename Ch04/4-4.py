"""
    날짜 : 2020/06/23
    이름 : 유효진
    내용 : 함수고급 실습하기
"""

# 기본값 매개변수
def hello(name='홍길동', age=17):
    print('이름 : %s' % name)
    print('나이 : %d' % age)

hello()
hello('김유신')
hello('김춘추', 25)

# 가변 매개변수 -java는 변수 이름 뒤에 '...'  붙이면 가변 매개변수가 된다
def total( *num ):
    tot = 0
    for k in num:
        tot += k
    return tot

r1 = total(1)
r2 = total(1, 2, 3)
r3 = total(1, 2, 3, 4, 5)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)

# 여러개의 값을 반환하는 함수
def multi_result(a, b):
    x = a + b
    y = a * b
    return x, y

res1, res2 = multi_result(2, 3)
res3 = multi_result(2, 3)
print('res1:', res1)
print('res2:', res2)
print('res3:', res3)

# 함수 지역변수, 전역변수
var1 = 1

def scope_test():
    global var1     #전역변수 var1을 함수내에서 참조하겠다.
    var1 = var1 + 1
    print('var1 :', var1)

scope_test()

# 함수를 변수에 저장해서 호출하기
def my_print(msg):
    print('msg :', msg)

my1 = my_print
my2 = my_print

my1('my1 변수의 함수 실행')
my2('my2 변수의 함수 실행')

def plus(a, b):
    return a+b

def minus(a, b):
    return a-b

list = [plus, minus]
rs1 = list[0](1, 2)
rs2 = list[1](2, 3)

print('rs1 :', rs1)
print('rs2 :', rs2)