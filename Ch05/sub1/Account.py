# 클래스 정의
class Account:
    # 멤버변수 (__init 생성자에서 선언)
    def __init__(self, bank, id, name, money):
        self.bank = bank
        self.id = id
        self.name = name
        self.money = money

    # 멤버함수
    def deposit(self, money):
        self.money += money

    def withdraw(self, money):
        self.money -= money

    def show(self):
        print('---------------------')
        print('은 행 명 :', self.bank)
        print('계좌번호 :', self.id)
        print('입 금 주 :', self.name)
        print('현재잔액 :', self.money)
        print('---------------------')