from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class CreditCardPayment(Payment):
    def pay(self):
        print("Paying with credit card")


class PayPalPayment(Payment):
    def pay(self):
        print("Paying with PayPal")