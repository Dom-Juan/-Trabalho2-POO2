from models.payment_methods.payment import Payment


class Money(Payment):
  def __init__(self, **kwargs):
    super(Money, self).__init__()
    self.__quantity: float = kwargs.get('quantity', 0)

  @property
  def quantity(self):
    return self.__quantity

  @quantity.setter
  def quantity(self, value: float):
    self.__quantity = value
    pass