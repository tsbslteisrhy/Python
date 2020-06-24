"""
    날짜 : 2020/06/24
    이름 : 유효진
    내용 : 외장함수 실습하기 교재 p262
"""
import time
import calendar as cal
import math
import random as rand

# time
r1 = time.time()    # milisecond
print('r1 :', r1)

r2 = time.ctime()
print('r2 :', r2)

now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)
print('%s년 %s월 %s일' % (year, month, date))

for i in range(2):
    print('i :', i)
    time.sleep(1)   # 스레드를 1초동안 sleep

# calendar
r3 = cal.calendar(2020)
print(r3)

r4 = cal.weekday(2020, 7, 16)
print(r4)

# math
r5 = math.ceil(1.2)
r6 = math.floor(1.8)
#반올림 round()은 내장함수
r7 = math.sqrt(9)
r8 = math.factorial(5)

print('r5 :', r5)
print('r6 :', r6)
print('r7 :', r7)
print('r8 :', r8)

# random
rs1 = rand.random() # 0 ~ 1 사이 실수
print('rs1 :', rs1)

rs2 = rs1 * 10 # 0 ~ 10 사이 실수
print('rs2 :', rs2)

rs3 = math.ceil(rs2) # 1 ~ 10 사이 정수
print('r3 :', rs3)