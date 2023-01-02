from models.payment_methods.payment import Payment


class Pix(Payment):
  def __int__(self, **kwargs):
    super().__int__()
    self.__pix_code: str = kwargs.get('pix_code', 'null')
    self.__quantity: float = kwargs.get('quantity', 0)
    # end constructor

  @property
  def pix_code(self):
    return self.__pix_code

  @pix_code.setter
  def pix_code(self, value: str):
    self.__pix_code = value
    pass

  @property
  def quantity(self):
    return self.__quantity

  @quantity.setter
  def quantity(self, value: float):
    self.__quantity = value
    pass