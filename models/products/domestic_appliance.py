

from models.products.product import Product


class DomesticAppliance(Product):
  def __init__(self, **kwargs):
    super(self, DomesticAppliance).__init__(kwargs)

  def calc_value(self):
    return self.value_price + (self.value_price * 0.0075)

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value: str):
    self._name = value
    pass

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
    self._manufacture_date = datetime.datetime.strptime(value, '%d/%m/%Y').date().strftime('%d/%m/%Y')
    pass