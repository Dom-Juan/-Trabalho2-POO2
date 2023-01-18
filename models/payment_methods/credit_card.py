from models.payment_methods.payment import Payment


class CreditCard(Payment):
  def __init__(self, **kwargs):
    super(CreditCard, self).__init__()
    self.__name: str = kwargs.get('name', None)
    self.__flag: str = kwargs.get('flag', None)
    self.__card_number: str = kwargs.get('card_number', None)
    self.__quantity: float = kwargs.get('quantity', 0)

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value: str):
    self.__name = value
    pass

  @property
  def flag(self):
    return self.__flag

  @flag.setter
  def flag(self, value: str):
    self.__flag = value
    pass

  @property
  def card_number(self):
    return self.__card_number

  @card_number.setter
  def card_number(self, value: str):
    self.__card_number = value
    pass

  @property
  def quantity(self):
    return self.__quantity
  
  @quantity.setter
  def quantity(self, value: float):
    self.__quantity = value
    pass


if __name__ == '__main__':
  c: object = CreditCard(name='AAAA', flag='Nubank', card_number='123', quantity=9)
  print(c.name, c.flag)