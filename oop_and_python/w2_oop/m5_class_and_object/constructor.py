class Phone:
    manufactured = "China"

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f"sending to {phone}, message: {sms}"
        return text


# def p(dic)

my_phone = Phone("Me", "samsung", 30000)
print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = Phone("her", "Nokia", 2000)
print(her_phone.owner, her_phone.brand, her_phone.price)
