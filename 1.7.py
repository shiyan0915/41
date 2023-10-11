class Goods:
    def __init__(self,number,name,price,count,count_remaining):
        self.number = number
        self.name = name
        self.price = price
        self.count = count
        self.count_remanining = count_remaining
    def display(self):
        print(f'商品序号为{self.number}，商品名为{self.name},单价是{self.price},总数量是{self.count},剩余数量是{self.count_remaining}')
    def income(self):
        print('商品价值:',(count-count_remaining) * price)
    def setdata(self):
        print(f'修改商品序号为{self.number}，商品名为{self.name},单价是{self.price},总数量是{self.count},剩余数量是{self.count_remaining}')
