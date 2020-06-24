from Ch05.sub2.Computer import Computer

class SmartPhone(Computer):
    def __init__(self, cpu, ram, hdd, brand, tel):
        Computer.__init__(self, cpu, ram, hdd)
        self.brand = brand
        self.tel = tel

    def call(self):
        print('%s 번호로 전화' % self.tel)

    def show(self):
        print('------------------')
        print('폰명 :', self.brand)
        print('CPU :', self.cpu)
        print('RAM :', self.ram)
        print('HDD :', self.hdd)
        print('전화번호 :', self.tel)
        print('------------------')