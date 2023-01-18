import random


class Payment:
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)
    self.__recipe_code = self._user_code = random.sample(range(9999999), 1)[0]
  
  @property
  def recipe_note(self):
    return self.__recipe_code
  
  @recipe_note.setter
  def recipe_note(self, value: int):
    self.__recipe_code = value
    pass