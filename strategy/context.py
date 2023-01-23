from strategy.strategy import Strategy


# Classe Context utilizada para definir o tipo do Strategy.
class Context:
  def __init__(self, strategy: Strategy) -> None:
    """Context constructor, pode adicionado na hora de criação ou modificado depois"""
    self._strategy = strategy

  # Getter
  @property
  def strategy(self) -> Strategy:
    return self._strategy

  # Setter
  @strategy.setter
  def strategy(self, strategy: Strategy) -> None:
    self._strategy = strategy
    pass

  def filter_alg(self, product_list: list) -> list:
    new_product_list = self.strategy.filter_by_price(product_list)
    return new_product_list

