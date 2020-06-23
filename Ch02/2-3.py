"""
    날짜 : 2020/06/22
    이름 : 유효진
    내용 : 리스트 자료형 실습하기 교재 p72
"""

# 리스트(동적)
ls1 = [1, 2, 3, 4, 5]
print('ls1[0] :', ls1[0])
print('ls1[2] :', ls1[2])
print('ls1[4] :', ls1[4])

ls2 = [1, 3.14, True, '홍길동']    #파이썬은 서로 다른 타입의 데이터도 리스트에 저장 가능
print('ls2[1] :', ls2[1])
print('ls2[2] :', ls2[2])
print('ls2[3] :', ls2[3])

ls3 = [[1, 2, 3],
       [True, False, True],
       ['Apple', 'Banana', 'Grape']]
print('ls3[1] :', ls3[1])
print('ls3[2] :', ls3[2])
print('ls3[0][1] :', ls3[0][1])
print('ls3[2][1] :', ls3[2][1])

# 리스트 더하기
fr1 = ['사과', '오렌지']
fr2 = ['바나나', '포도', '수박']
fr3 = fr1 + fr2
print('fr3 :', fr3)
print('fr3[2] :', fr3[2])

# 리스트 수정, 변경, 삭제
numbers = [1, 2, 3, 4, 5]

numbers[1] = 7
print('numbers :', numbers)     #덮어쓰기

numbers[2:3] = [8, 9]
print('numbers :', numbers)     #추가

numbers[1:3] = []
print('numbers :', numbers)     #삭제

del numbers[1]
print('numbers :', numbers)     #삭제

# 리스트 관련 함수 교재 p80 ~ p84

#리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])
print(a)

#리스트 정렬(sort)
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)

#리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
a.reverse()
print(a)

#위치 반환(index)
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))
#print(a.index(0)) - 존재하지 않으면 error

#리스트에 요소 삽입(insert)
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

#리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
a.remove(3)
print(a)

#리스트 요소 끄집어내기(pop)
a = [1, 2, 3]
print(a.pop())       # 맨 마지막 요소 pop
print(a)

a = [1, 2, 3]
print(a.pop(1))
print(a)

#리스트에 포함된 요소 x의 개수 세기(count)
a = [1, 2, 3, 1]
print(a.count(1))

#리스트 확장(extend)
a = [1, 2, 3]
a.extend([4, 5])
print(a)

b = [6, 7]
a.extend(b)
print(a)

