import random

class ShippingCompany(object):
  def __init__(self, **kwargs):
    """
    Purpose: value
    """
    self.__code: int = random.sample(range(9999), 1)[0]
    self.__cnpj: str = kwargs.get('cnpj', None)
    self.__name: str = kwargs.get('name', None)
    self.__email: str = kwargs.get('email', None)
    self.__phone_number: str = kwargs.get('phone_number', None)
    self.__address: str = kwargs.get('address', None)
    self.__delivery_time: int = kwargs.get('delivery_time', None)
  # end alternate constructor
  
  @property
  def code(self):
    return self.__code
  
  @property
  def cnpj(self):
    return self.__cnpj

  @cnpj.setter
  def cnpj(self, value: int):
    self.cnpj = value
    pass
  
  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self, value: str):
    self.__name = value
  
  @property
  def email(self):
    return self.__email
  
  @email.setter
  def email(self, value: str):
    self.__email = value
  
  @property
  def phone_number(self):
    return self.__phone_number
  
  @phone_number.setter
  def phone_number(self, value: str):
    self.__phone_number = value
  
  @property
  def address(self):
    return self.__address
  
  @address.setter
  def address(self, value: str):
    self.__address = value
  
  @property
  def delivery_time(self):
    return self.__delivery_time
  
  @delivery_time.setter
  def delivery_time(self, value: int):
    self.__delivery_time = value

if __name__ == '__main__':
  print("DEBUG Shipping Company")
  sc = ShippingCompany(
    cnpj="232.4214.231/001",
    name="AAAAAAAAAAA Transportadora",
    email="a_transportadora@gmail.com",
    phone_number="55 11 1545-4841",
    address="AAAAA",
    delivery_time=12,
    )
  print(sc.code)
  print(sc.cnpj)
  print(sc.name)
  print(sc.email)
  print(sc.phone_number)
  print(sc.address)
  print(sc.delivery_time)