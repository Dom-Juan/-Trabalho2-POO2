from models.payment_methods.pix import Pix
from models.payment_methods.money import Money
from models.payment_methods.credit_card import CreditCard


class PaymentController():
  def __init__(self, **kwargs):
    self._payment_list: list = kwargs.get('payment_list', [])

  @property
  def payment_list(self):
    return self._payment_list

  @payment_list.setter
  def payment_list(self, value):
    self._payment_list.append(value)
    pass

  def create_payment_credit_card(self, name: str, flag: str, card_number: str, quantity: float):
    return CreditCard(name=name, flag=flag, card_number=card_number, quantity=quantity)

  def create_payment_money(self, quantity: float):
    return Money(quantity=quantity)

  def create_payment_pix(self, pix_code: str, quantity: float):
    return Pix(pix_code=pix_code, quantity=quantity)