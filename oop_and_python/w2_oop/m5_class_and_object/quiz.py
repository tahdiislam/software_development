def call():
    print('calling someone i dont know')
    return 'call done'


class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']


    def call(self):
        print('calling someone i know')



my_phone = Phone()
call()
class A:
    def __init__(self, value):
        value = 3
        self.value = value

    def change(self):
        self.value = 12


ans = []
a = A(13)
ans.append(a.value)
a.change()
ans.append(a.value)
print(ans)

# 5th quiz
# class Shop:
#     cart = []

#     def __init__(self, buyer):
#         self.buyer = buyer

#     def add_to_cart(self, item):
#         self.cart.append(item)


# p1 = Shop('meh jabeeeen')
# p1.add_to_cart('shoes')
# p1.add_to_cart('phone')


# nisho = Shop('noisho')
# nisho.add_to_cart('cap')
# nisho.add_to_cart('watch')
# print(nisho.cart)

# 6th quiz
class Shop:
    shopping_mall = 'Jamuna'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)


p1 = Shop('meh jabeeeen')
p1.add_to_cart('shoes')
p1.add_to_cart('phone')


nisho = Shop('noisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)

# 8th quiz

class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'Sending SMS to: {phone+5}'
        return text


my_phone = Phone()
result = my_phone.send_sms(41524, 'Missy, I missed to miss you')
print(result)