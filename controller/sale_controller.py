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
    self._item_sale_list: list = kwargs.get('item_sale_list')
    # end alternate constructor

  def create_sale(
      self,
      client,
      manager,
      delivery_days,
      item_sales_list,
      total_value_to_pay,
      payment_method,
      shipping_company,
      discount_value
  ) -> object:
    sale_made = Sale(
      client=client,
      manager=manager,
      delivery_days=int(delivery_days),
      item_list=item_sales_list,
      total_value_to_pay=total_value_to_pay,
      payment_method=payment_method,
      shipping_company=shipping_company
    )
    sale_made.discount_value = discount_value
    self._sales_list.append(sale_made)
    return sale_made

  def create_item_sale(self, product: object, amount: float) -> object:
    new_value_price: float = float(product.value_price) * amount if amount > 0 else float(product.value_price)
    item_sale = ItemSale(product=product, item_value=new_value_price, quantity=amount)
    self._item_sale_list.append(item_sale)
    return item_sale

  # Retorna a quantidade de itens numa venda.
  def get_item_amount(self, sale):
    quantity: int = 0
    for i in sale.item_sale_list:
      quantity += i.quantity
    return quantity