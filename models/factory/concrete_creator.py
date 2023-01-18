from models.factory.product_factory import Creator

from models.products.clothing import Clothing
from models.products.domestic_appliance import DomesticAppliance
from models.products.eletronics import Eletronics
from models.products.furnitures import Furnitures


class ConcreteCreatorClothing(Creator):
  def factory_method(self, **kwargs) -> object:
    return Clothing(
      name=kwargs.get('name', ''),
      description=kwargs.get('description', ''),
      manufacture_date=kwargs.get('manufacture_date', '01/01/1970'),
      value_price=kwargs.get('value_price', 0),
      manufacturer=kwargs.get('manufacturer', ''),
      available=kwargs.get('available', True)
    )


class ConcreteCreatorDomesticAppliance(Creator):
  def factory_method(self, **kwargs) -> object:
    return DomesticAppliance(
      name=kwargs.get('name'),
      description=kwargs.get('description', None),
      manufacture_date=kwargs['manufacture_date'],
      value_price=kwargs.get('value_price', 0),
      manufacturer=kwargs.get('manufacturer', None),
      available=kwargs.get('available', True)
    )


class ConcreteCreatorEletronics(Creator):
  def factory_method(self, **kwargs) -> object:
    return Eletronics(
      name=kwargs.get('name'),
      description=kwargs.get('description', None),
      manufacture_date=kwargs['manufacture_date'],
      value_price=kwargs.get('value_price', 0),
      manufacturer=kwargs.get('manufacturer', None),
      available=kwargs.get('available', True)
    )


class ConcreteCreatorFurnitures(Creator):
  def factory_method(self, **kwargs) -> object:
    return Furnitures(
      name=kwargs.get('name'),
      description=kwargs.get('description', None),
      manufacture_date=kwargs['manufacture_date'],
      value_price=kwargs.get('value_price', 0),
      manufacturer=kwargs.get('manufacturer', None),
      available=kwargs.get('available', True)
    )