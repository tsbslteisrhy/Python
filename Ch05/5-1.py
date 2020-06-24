"""
    날짜 : 2020/06/24
    이름 : 유효진
    내용 : 클래스 실습하기 교재 p183
"""

# 객체생성
from Ch05.sub1.Account import Account
from Ch05.sub2.Smartphone import SmartPhone

kb = Account('국민은행', '101-12-1111', '김유신', 10000)
wr = Account('우리은행', '101-12-2222', '김춘추', 10000)

kb.deposit(30000)
kb.withdraw(5000)
kb.show()

wr.deposit(25000)
wr.withdraw(7000)
wr.show()

# 클래스 상속
iphone = SmartPhone('아이폰7', 'A7', '4GB', '128GB', '010-1234-1111')
iphone.call()
iphone.calc()
iphone.internet()
iphone.show()