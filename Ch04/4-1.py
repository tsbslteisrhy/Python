"""
    날짜 : 2020/06/23
    이름 : 유효진
    내용 : 함수 실습하기 교재 p150
"""

# 함수정의
def f(x):
    y = 2 * x + 3
    return y

# 함수 호출
r1 = f(1)
r2 = f(2)
r3 = f(3)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)

# 타입1 - 매개변수 O, 리턴값 O
def type1(x, y):
    z = x + y
    return z

# 타입2 - 매개변수 X, 리턴값 O
def type2():
    tot = 0
    for k in range(11):
        tot += k
    return tot

# 타입3 - 매개변수 O, 리턴값 X
def type3(items):
    tot = 0
    for i in items:
        tot += i
    print('items 합 :', tot)

# 타입4 - 매개변수 X, 리턴값 X
def type4():
    result = type1(1, 2)
    print('result :', result)

# 함수호출
rs1 = type1(2, 3)
print('rs1 :',rs1)

rs2 = type2()
print('rs2 :',rs2)

type3([1, 2, 3, 4, 5])
type3((1, 2, 3, 4, 5))

type4()