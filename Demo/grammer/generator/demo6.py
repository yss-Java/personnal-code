# class Goods:
#     @property
#     def price(self):
#         return "laowang"
#
# obj = Goods()
# result = obj.price  # 自动执行`@property`修饰的`price`方法，并获取方法的返回值
# print(result)

class Goods:
    """
    只有在python3中才有@xxx.setter  @xxx.deleter
    """
    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price

obj = Goods()
obj.price          # 获取商品价格
obj.price = 200    # 修改商品原价
del obj.price      # 删除商品原价
