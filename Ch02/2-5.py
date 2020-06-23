"""
    날짜 : 2020/06/22
    이름 : 유효진
    내용 : 딕셔너리 자료형 실습하기 교재 p88
"""

# 딕셔너리 생성
dic1 = {1: 'Python', 2: 'Java', 3: 'C', 4: 'C++'}   #java의 map(key:value), 형태는 JSON
dic2 = {
    'kor': '대한민국',
    'usa': '미국',
    'chi': '중국',
    'jpn': '일본',
    'spn': '스페인',
    'tai': '대만'
}
dic3 = {
    101: [1, 2, 3, 4, 5],
    102: ('서울', '대전', '대구', '부산', '광주'),
    103: {'p1':'김유신', 'p2':'이성계', 'p3':'이순신'}
}

# 딕셔너리 값 출력
print('dic1 :', dic1)
print('dic2 :', dic2)
print('dic3 :', dic3)

print('dic1[1] :', dic1[1])
print("dic2['kor'] :", dic2['kor'])
print("dic3[102][1] :", dic3[102][1])
print("dic3[103]['p3'] :", dic3[103]['p3'])

# 딕셔너리 값 추가
dic1[5] = 'R'
print('dic1 :', dic1)

dic2['aus'] = '호주'
print('dic2 :', dic2)

# 딕셔너리 값 제거
del dic1[3]
print('dic1 :', dic1)

# 딕셔너리 관련 함수 교재 p93 ~ p96

#Key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

#Value 리스트 만들기(values)
#Key, Value 쌍 얻기(items)
#Key: Value 쌍 모두 지우기(clear)
#Key로 Value 얻기(get)
#해당 Key가 딕셔너리 안에 있는지 조사하기(in)