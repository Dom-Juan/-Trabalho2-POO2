import random
import datetime


class Manufacturer(object):
  def __init__(self, **kwargs):
    self.__manufacturer_code = random.sample(range(999), 1)[0]  # Retorna uma lista de números inteiros sem repetição.
    self.__cnpj: str = kwargs.get('cnpj', '')
    self.__name: str = kwargs.get('name', '')
    self.__description: str = kwargs.get('description', '')
    self.__email: str = kwargs.get('email', '')
    self.__phone: str = kwargs.get('phone', '')
    self.__address: str = kwargs.get('address', '')

  @property
  def manufacturer_code(self):
    return self.__manufacturer_code

  @manufacturer_code.setter
  def manufacturer_code(self, value: int):
    self.__manufacturer_code = value
    pass

  @property
  def cnpj(self):
    return self.__cnpj

  @cnpj.setter
  def cnpj(self, value: str):
    self.__cnpj = value
    pass

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value: str):
    self.__name = value
    pass

  @property
  def description(self):
    return self.__description

  @description.setter
  def description(self, value: str):
    self.__description = value
    pass

  @property
  def email(self):
    return self.__email

  @email.setter
  def email(self, value: str):
    self.__email = value
    pass

  @property
  def phone(self):
    return self.__phone

  @phone.setter
  def phone(self, value: str):
    self.__phone = value
    pass

  @property
  def address(self):
    return self.__address

  @address.setter
  def address(self, value: str):
    self.__address = value
    pass