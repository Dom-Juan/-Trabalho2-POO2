from models.sales.sale import Sale
from models.sales.item_sale import ItemSale


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

  # Retorna vetor com os "vencedores" das transportadoras pela quantidade de produto transportado.
  def get_shipping_company_with_more_sales(self, sales_list: list, shipping_company_list: list):
    arr = (0, 0)
    winners: list = []
    current_count: int = 0
    current: object
    for sc in shipping_company_list:
        for i in sales_list:
          current = sc
          if current.code == i.shipping_company.code:
            current_count += 1
          else:
            arr = (current, current_count)
            current_count = 1
          if current_count > arr[1]:
            winners.append(current)
    print(winners, "\n", arr)
    seen = set()
    winners[:] = [i for i in winners if i not in seen and not seen.add(i)]
    return winners

  # Retorna vetor com os "vencedores" das fabricantes pela quantidade de produto vendido.
  def get_manufacturers_with_most_sold_products(self, sales_list: list, manufacturer_list: list):
    arr = (0, 0)
    winners: list = []
    current_count: int = 0
    current: object
    for m in manufacturer_list:
        for i in sales_list:
          for item_sale in i.item_sale_list:
            current = m
            if current.manufacturer_code == item_sale.product.manufacturer.manufacturer_code:
              current_count += 1
            else:
              arr = (current, current_count)
              current_count = 1
            if current_count > arr[1]:
              winners.append(current)
    print(winners, "\n", arr)
    seen = set()
    winners[:] = [i for i in winners if i not in seen and not seen.add(i)]
    return winners