"""
    날짜 : 2020/06/22
    이름 : 유효진
    내용 : 숫자형(연산자) 실습하기 교재 p40
"""

# 대입연산자
a = 1
b = c = d = 0
e, f, g = True, 1.23, '홍길동'

print('a :', a)
print('b :', b)
print('c :', c)
print('d :', d)
print('e :', e)
print('f :', f)
print('g :', g)

# 산술연산자
num1 = 1
num2 = 2
num3 = 3
num4 = 4

r1 = num1 + num2
r2 = num1 - num2
r3 = num2 * num3
r4 = num4 / num3    # 몫(실수)
r5 = num4 % num3
r6 = num2 ** num3   # 제곱
r7 = num4 // num3   # 몫(정수)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)
print('r5 :', r5)
print('r6 :', r6)
print('r7 :', r7)

# 복합대입연산자
num5, num6, num7, num8 = 5, 6, 7, 8
num5 += 5
num6 -= 6
num7 *= 7
num8 /= 8

print('num5 :', num5)
print('num6 :', num6)
print('num7 :', num7)
print('num8 :', num8)

# 비교연산자
num9, num10 = 9, 10

rs1 = (num9 > num10)
rs2 = (num9 < num10)
rs3 = (num9 >= num10)
rs4 = (num9 <= num10)
rs5 = (num9 == num10)
rs6 = (num9 != num10)

print('rs1 :', rs1)
print('rs2 :', rs2)
print('rs3 :', rs3)
print('rs4 :', rs4)
print('rs5 :', rs5)
print('rs6 :', rs6)

# 논리연산자
res1 = (num9 > 3) and (num10 > 5)
res2 = (num9 > 3) and (num10 < 5)
res3 = (num9 > 3) or (num10 > 5)
res4 = (num9 < 3) or (num10 < 5)
res5 = not(num9 > num10)

print('res1 :', res1)
print('res2 :', res2)
print('res3 :', res3)
print('res4 :', res4)
print('res5 :', res5)