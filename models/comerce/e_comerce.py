
class EComerce(object):
  def __init__(self, **kwargs):
    self.__name = 'Atacado da Tristeza UNESP'
    self.__sales_list:list = kwargs.get('sales_list')
    self.__product_list:list = kwargs.get('product_list')
    self.__manufacturer_list:list = kwargs.get('manufacturer_list')
    self.__shipping_company_list:list = kwargs.get('shipping_company_list')
    self.__client_list:list = kwargs.get('client_list')
    self.__managers_list:list = kwargs.get('managers_list')
    self.__config = None
    # end alternate constructor
  @property
  def name(self):
    """_summary_
    Returns:
      _type_: _description_
    """    
    return self.__name
  
  @name.setter
  def name(self, value:str):
    """_summary_
    Args:
      value (str): _description_
    """    
    self.__name = value
  
  @property
  def client_list(self):
    """_summary_
    Returns:
        _type_: _description_
    """    
    return self.__client_list
  
  @client_list.setter
  def client_list(self, value:object):
    self.__client_list.append(value)
