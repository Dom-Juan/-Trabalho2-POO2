import datetime


from models.products.product import Product


class Eletronics(Product):
  def __init__(self, **kwargs):
    super(self, Eletronics).__init__(kwargs)

  def calc_value(self):
    return self.value_price * 3.5