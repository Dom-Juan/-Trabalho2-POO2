from models.payment_methods.payment import Payment


class CreditCard(Payment):
  def __int__(self, **kwargs):
    self.__name: str = kwargs.get('name', None)
    self.__flag: str = kwargs.get('flag', None)
    self.__card_number:str = kwargs.get('card_number', None)
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