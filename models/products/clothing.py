

from models.products.product import Product



class Clothing(Product):
  def __init__(self, **kwargs):
    super(self, Clothing).__init__(kwargs)

  def calc_value(self):
    return self.value_price + (self.value_price * 0.0115)