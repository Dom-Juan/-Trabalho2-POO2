class ItemSale(object):
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)
    self.__product: object = kwargs.get('product', None)
    self.__item_value: float = kwargs.get('item_value', 0.0)
    self.__quantity: int = kwargs.get('quantity', 0)

  @property
  def product(self):
    return self.__product

  @product.setter
  def product(self, obj: object):
    self.__product = obj
    pass

  @property
  def item_value(self):
    return self.__item_value

  @item_value.setter
  def item_value(self, value: float):
    self.__item_value = value
    pass

  @property
  def quantity(self):
    return self.__quantity

  @quantity.setter
  def quantity(self, value: int):
    self.__quantity = value
    pass