from models.payment_methods.payment import Payment


class Money(Payment):
  def __init__(self, **kwargs):
    super(Money, self).__init__()
    self.__name = "Dinheiro"
    self.__quantity: float = kwargs.get('quantity', 0)

  @property
  def name(self):
    return self.__name

  @property
  def quantity(self):
    return self.__quantity

  @quantity.setter
  def quantity(self, value: float):
    self.__quantity = value
    pass