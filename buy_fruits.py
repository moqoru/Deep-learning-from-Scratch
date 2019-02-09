# name : MOQORU(Youngjune Seo)
# date : 2019-02-09

class AddLayer:
    def __init__(self):
        pass
    def forward(self, x, y):
        out = x + y
        return out
    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy
    
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y
        return out
    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x
        return dx, dy

# buy 2 apples
apple = 100
apple_num = 2
tax = 1.1

mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

apple_price = mul_apple_layer.forward(apple, apple_num) # x = 100, y = 2
price = mul_tax_layer.forward(apple_price, tax) # x = 200, y = 1.1

print(price)

dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice) # 1 * 1.1, 1 * 200
dapple, dapple_num = mul_apple_layer.backward(dapple_price) # 1.1 * 2, 1.1 * 100

print(dapple, dapple_num, dtax)

# buy 2 bananas & 3 oranges
banana = 100
banana_num = 2
orange = 150
orange_num = 3
tax2 = 1.1

mul_banana_layer = MulLayer()
mul_orange_layer = MulLayer()
add_banana_orange_layer = AddLayer()
mul_tax2_layer = MulLayer()

banana_price = mul_banana_layer.forward(banana, banana_num)
orange_price = mul_orange_layer.forward(orange, orange_num)
all_price = add_banana_orange_layer.forward(banana_price, orange_price)
real_price = mul_tax2_layer.forward(all_price,tax2)

print(real_price)

dreal_price = 1
dall_price, dtax2 = mul_tax2_layer.backward(dreal_price)
dbanana_price, dorange_price = add_banana_orange_layer.backward(dall_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)
dbanana, dbanana_num = mul_banana_layer.backward(dbanana_price)

print(dbanana_num, dbanana, dorange, dorange_num, dtax2)
