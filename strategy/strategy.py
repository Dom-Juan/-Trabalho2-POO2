from abc import ABC, abstractmethod


# Classe abstrata Strategy.
class Strategy(ABC):
  @abstractmethod
  def filter_by_price(self, product_list: list):
    pass


# Usando o sort do sistema invertido para retorna uma nova lista do maior para o menor.
class ConcreteStrategyHighest(Strategy):
  def filter_by_price(self, product_list: list):
    return sorted(product_list, key=lambda x: x.value_price, reverse=True)


# Bubble Sorte para ordena do menor para o maior.
class ConcreteStrategyLowest(Strategy):
  def filter_by_price(self, product_list: list):
    n = len(product_list)
    for i in range(n):
      for j in range(0, n - i - 1):
        if product_list[j].value_price > product_list[j + 1].value_price:
          product_list[j], product_list[j + 1] = product_list[j + 1], product_list[j]
    return product_list