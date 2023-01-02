import random
import datetime


class Product(object):
  def __init__(self, **kwargs):
    self._product_code: int = random.sample(range(999999), 1)[0]  # Retorna uma lista de números inteiros sem repetição.
    self._name: str = kwargs.get('name', None)
    self._description: str = kwargs.get('description', None)
    if kwargs['anniversary_date'] == (None or ''):
      self._manufacture_date: any = None
    else:
      self._manufacture_date: str = datetime.datetime.strptime(
        kwargs['manufacture_date'],
        '%d/%m/%Y'
      ).date().strftime('%d/%m/%Y')
    self._value_price: float = kwargs.get('value_price', 0)
    self._manufacturer: object = kwargs.get('manufacturer', None)
    self._available: bool = True

  @property
  def product_code(self):
    return self._product_code

  @product_code.setter
  def product_code(self, value: int):
    self._product_code = value
    pass

  @property
  def description(self):
    return self._description

  @description.setter
  def description(self, value: str):
    self._description = value
    pass

  @property
  def value_price(self):
    return self._value_price

  @value_price.setter
  def value_price(self, value: float):
    self._value_price = value
    pass

  @property
  def manufacturer(self):
    return self._manufacturer

  @manufacturer.setter
  def manufacturer(self, value: str):
    self._manufacturer = value
    pass

  @property
  def available(self):
    return self._available

  @available.setter
  def available(self, value: bool):
    self._available = value
    pass

  @property
  def manufacture_date(self):
    return self._manufacture_date

  @manufacture_date.setter
  def manufacture_date(self, value: any):
    """_summary_
    Args:
        value (any): _description_
    """
    self._manufacture_date = datetime.strptime(value, '%d/%m/%Y').date().strftime('%d/%m/%Y')
    pass