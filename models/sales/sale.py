import random
import datetime


class Sale(object):
  def __init__(self, **kwargs):
    self.__sale_code: int = random.sample(range(9999999), 1)[0]  # Retorna uma lista de números inteiros sem repetição.
    self.__client: object = kwargs.get('client', None)
    self.__manager: object = kwargs.get('manager', None)
    today = datetime.date.today()
    self.__sale_date: any = today.strftime("%d/%m/%Y")
    self.__delivery_date: any = today + datetime.timedelta(days=kwargs.get('delivery_days', 0))
    self.__item_sales_list: list = kwargs.get('item_list', [])
    self.__total_value_to_pay: float = kwargs.get('total_value_to_pay', 0.0)
    self.__discount_value: float = 0.0
    self.__payment_method: object = kwargs.get('payment_method', None)
    self.__shipping_company: object = kwargs.get('shipping_company', None)

  @property
  def sale_code(self):
    return self.__sale_code

  @sale_code.setter
  def sale_code(self, value: int):
    self.__sale_code = value
    pass

  @property
  def client(self):
    return self.__client

  @client.setter
  def client(self, obj: object):
    self.__client = obj
    pass

  @property
  def manager(self):
    return self.__manager

  @manager.setter
  def manager(self, obj: object):
    self.__manager = obj
    pass

  @property
  def sale_date(self):
    return self.__sale_date

  @sale_date.setter
  def sale_date(self, value: str):
    if value == (None or ''):
      self.__sale_date: str = self.__sale_date
    else:
      self.__sale_date: str = datetime.datetime.strptime(value, '%d/%m/%Y').date().strftime('%d/%m/%Y')
    pass

  @property
  def delivery_date(self):
    return self.__delivery_date

  @delivery_date.setter
  def delivery_date(self, value):
    if value == (None or ''):
      self.__delivery_date: str = self.__delivery_date
    else:
      self.__delivery_date: str = datetime.datetime.strptime(value, '%d/%m/%Y').date().strftime('%d/%m/%Y')
    pass

  @property
  def item_sale_list(self):
    return self.__item_sales_list

  @item_sale_list.setter
  def item_sale_list(self, value: list):
    self.__item_sales_list = value
    pass

  @property
  def discount_value(self):
    return self.__discount_value

  @discount_value.setter
  def discount_value(self, value: float):
    self.__discount_value = value
    pass

  @property
  def payment_method(self):
    return self.__payment_method

  @payment_method.setter
  def payment_method(self, obj: object):
    self.__payment_method = obj
    pass

  @property
  def shipping_company(self):
    return self.__shipping_company

  @shipping_company.setter
  def shipping_company(self, obj: object):
    self.__shipping_company = obj
    pass

  def add_obj_item_sale_list(self, value: object):
    self.__item_sales_list.append(value)
    pass

  def calc_total_sale_value(self)-> float:
    total_to_pay: float = 0.0
    for i in self.item_sale_list:
      total_to_pay = total_to_pay + i.item_value
    return total_to_pay - (total_to_pay * 0.03) if self.client.gold_client else total_to_pay

  def calc_delivery_date(self, value: int):
    # ??? precisa se já calculamos isso no construtor ?
    self.__delivery_date: any = datetime.datetime.strptime(
      self.sale_date, '%d/%m/%y %H:%M:%S') + datetime.timedelta(days=value)
    pass