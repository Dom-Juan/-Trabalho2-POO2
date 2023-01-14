import sys

from models.products.clothing import Clothing
from models.products.domestic_appliance import DomesticAppliance
from models.products.eletronics import Eletronics
from models.products.furnitures import Furnitures

sys.path.append('..//..')

print(sys.path)


class ProductController(object):
  def __init__(self, **kwargs):
    """
    Purpose: value
    """
    self._product_list: list = kwargs.get('product_list')
    # end alternate constructor

  def create_product_clothing(self, name: str, description: str,
                     manufacture_date: str, value_price: float, manufacturer: object,
                     available: bool) -> object:
    product: object = None
    for p in self._product_list:
      if p.name == name:
        return False
      else:
        product = Clothing(
          name,
          description,
          manufacture_date,
          value_price,
          manufacturer,
          available
        )
    return product

  def create_product_domestic_appliance(self, name: str, description: str,
                              manufacture_date: str, value_price: float, manufacturer: object,
                              available: bool) -> object:
    product: object = None
    for p in self._product_list:
      if p.name == name:
        return False
      else:
        product = DomesticAppliance(
          name,
          description,
          manufacture_date,
          value_price,
          manufacturer,
          available
        )
    return product

  def create_product_furnitures(self, name: str, description: str,
                                          manufacture_date: str, value_price: float, manufacturer: object,
                                          available: bool) -> object:
    product: object = None
    for p in self._product_list:
      if p.name == name:
        return False
      else:
        product = Furnitures(
          name,
          description,
          manufacture_date,
          value_price,
          manufacturer,
          available
        )
    return product

  def create_product_eletronics(self, name: str, description: str,
                                    manufacture_date: str, value_price: float, manufacturer: object,
                                    available: bool) -> object:
    product: object = None
    for p in self._product_list:
      if p.name == name:
        return False
      else:
        product = Eletronics(
          name,
          description,
          manufacture_date,
          value_price,
          manufacturer,
          available
        )
    return product