class Phone:
    print = 30000
    brand = "samsung"
    color = "black"
    features = ["camera", "speaker", "calling", "hammer"]

    def call(self):
        print("calling one person")

    def send_smd(self, phone, sms):
        
        text = f"sending sms to {phone} and message {sms}"
        return text


new_phone = Phone()
new_phone.call()
snd_sms = new_phone.send_smd("8343434322", "Missy, I missed to miss you")
print(snd_sms)