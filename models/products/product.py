from __future__ import annotations

import random
import datetime

from abc import ABC, abstractmethod


class Product(ABC):
  def __init__(self, **kwargs):
    self._product_code: int = random.sample(range(999999), 1)[0]  # Retorna uma lista de números inteiros sem repetição.
    self._name: str = kwargs.get('name', None)
    self._description: str = kwargs.get('description', None)
    if kwargs['manufacture_date'] == (None or ''):
      self._manufacture_date: any = None
    else:
      self._manufacture_date: str = datetime.datetime.strptime(
        kwargs['manufacture_date'],
        '%d/%m/%Y'
      ).date().strftime('%d/%m/%Y')
    self._value_price: float = kwargs.get('value_price', 0)
    self._manufacturer: object = kwargs.get('manufacturer', None)
    self._available: bool = kwargs.get('available', True)

  @property
  @abstractmethod
  def product_code(self):
    return self._product_code

  @product_code.setter
  @abstractmethod
  def product_code(self, value: int):
    self._product_code = value
    pass

  @property
  @abstractmethod
  def name(self):
    return self._name

  @name.setter
  @abstractmethod
  def name(self, value: str):
    self._name = value
    pass

  @property
  @abstractmethod
  def description(self):
    return self._description

  @description.setter
  @abstractmethod
  def description(self, value: str):
    self._description = value
    pass

  @property
  @abstractmethod
  def value_price(self):
    return self._value_price

  @value_price.setter
  @abstractmethod
  def value_price(self, value: float):
    self._value_price = value
    pass

  @property
  @abstractmethod
  def manufacturer(self):
    return self._manufacturer

  @manufacturer.setter
  @abstractmethod
  def manufacturer(self, value: str):
    self._manufacturer = value
    pass

  @property
  @abstractmethod
  def available(self):
    return self._available

  @available.setter
  @abstractmethod
  def available(self, value: bool):
    self._available = value
    pass

  @property
  @abstractmethod
  def manufacture_date(self):
    return self._manufacture_date

  @manufacture_date.setter
  @abstractmethod
  def manufacture_date(self, value: any):
    """_summary_
    Args:
        value (any): _description_
    """
    self._manufacture_date = datetime.datetime.strptime(value, '%d/%m/%Y').date().strftime('%d/%m/%Y')
    pass