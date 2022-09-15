class Purse:

    def __init__(self, valuta, name='Unknown'):
        self.money=0.00
        self.valuta=valuta
        self.name=name
    
    def top_up_balance(self, howmoney):
        self.money=self.money+howmoney

    def top_down_balance(self, howmoney):
        if self.money-howmoney<0:
            print('Pietrūkst naudas makā')
            raise ValueError ('Pietrūkst naudas makā')
        self.money=self.money-howmoney

    def info(self):
        print(self.money)
    
    def __del__(self):
        print('Maks izdzēsts')
        #return self.money

x=Purse('USD')
y=Purse('EUR', 'Bill')
x.top_up_balance(100)
x.money=200
x.info()


#x.money=100
#print(y.info())
#print(x.info())
