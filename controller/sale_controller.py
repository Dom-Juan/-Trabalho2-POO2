import sys

from models.sales.sale import Sale
from models.sales.item_sale import ItemSale

sys.path.append('..//..')

print(sys.path)


class SaleController(object):
  def __init__(self, **kwargs):
    """
    Purpose: value
    """
    self._sales_list: list = kwargs.get('sales_list')
    # end alternate constructor