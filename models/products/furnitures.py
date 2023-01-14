

from models.products.product import Product



class Furnitures(Product):
  def __init__(self, **kwargs):
    super(self, Furnitures).__init__(kwargs)

  def calc_value(self):
    return self.value_price + (self.value_price * 0.0525)