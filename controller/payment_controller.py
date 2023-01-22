from models.payment_methods.pix import Pix
from models.payment_methods.money import Money
from models.payment_methods.credit_card import CreditCard


class PaymentController:
  def __init__(self, **kwargs):
    self._payment_list: list = kwargs.get('payment_list', [])

  @property
  def payment_list(self):
    return self._payment_list

  @payment_list.setter
  def payment_list(self, value):
    self._payment_list.append(value)
    pass

  def create_payment_credit_card(self, name: str, flag: str, card_number: str, quantity: float) -> object:
    cc: object = CreditCard(name=name, flag=flag, card_number=card_number, quantity=quantity)
    return cc

  def create_payment_money(self, quantity: float) -> object:
    m: object = Money(quantity=quantity)
    return m

  def create_payment_pix(self, pix_code: str, quantity: float) -> object:
    pix: object = Pix(pix_code=pix_code, quantity=quantity)
    return pix

  # Retorna um dicionário para ser usado na interface.
  def generate_payment_dict(self, payment_controller) -> dict:
    payment_dict: dict = {}
    for p in payment_controller.payment_list:
      payment_dict[p.name] = p
    return payment_dict