class Payment_FGA:
    def pay_FGA(self_FGA):
        print("Processing payment")

class CashPayment_FGA(Payment_FGA):
    def pay_FGA(self_FGA):
        print("Payment made using cash")

class CardPayment_FGA(Payment_FGA):
    def pay_FGA(self_FGA):
        print("Payment made using credit card")

payments_FGA = [CashPayment_FGA(), CardPayment_FGA()]
for p_FGA in payments_FGA:
    p_FGA.pay_FGA()

