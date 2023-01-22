from models.factory.concrete_creator import ConcreteCreatorClothing, ConcreteCreatorDomesticAppliance,\
  ConcreteCreatorEletronics, ConcreteCreatorFurnitures


class ProductController(object):
  def __init__(self, **kwargs):
    """
    Purpose: value
    """
    # end alternate constructor

  def create_product_clothing(
      self,
      name: str,
      description: str,
      manufacture_date: str,
      value_price: float,
      manufacturer: object,
      available: bool
    ) -> object:
    creator: object = ConcreteCreatorClothing()
    product: object = creator.factory_method(
      name=name,
      description=description,
      manufacture_date=manufacture_date,
      value_price=value_price,
      manufacturer=manufacturer,
      available=available
    )
    return product



  def create_product_domestic_appliance(
      self,
      name: str,
      description: str,
      manufacture_date: str,
      value_price: float,
      manufacturer: object,
      available: bool
  ) -> object:
    creator: object = ConcreteCreatorDomesticAppliance()
    product: object = creator.factory_method(
      name=name,
      description=description,
      manufacture_date=manufacture_date,
      value_price=value_price,
      manufacturer=manufacturer,
      available=available
    )
    return product


  def create_product_furnitures(
      self,
      name: str,
      description: str,
      manufacture_date: str,
      value_price: float,
      manufacturer: object,
      available: bool
  ) -> object:
    creator: object = ConcreteCreatorFurnitures()
    product: object = creator.factory_method(
      name=name,
      description=description,
      manufacture_date=manufacture_date,
      value_price=value_price,
      manufacturer=manufacturer,
      available=available
    )
    return product

  def create_product_eletronics(
      self,
      name: str,
      description: str,
      manufacture_date: str,
      value_price: float,
      manufacturer: object,
      available: bool
  ) -> object:
    creator: object = ConcreteCreatorEletronics()
    product: object = creator.factory_method(
      name=name,
      description=description,
      manufacture_date=manufacture_date,
      value_price=value_price,
      manufacturer=manufacturer,
      available=available
    )
    return product

  # Retorna um dicionário para ser usado na interface.
  def generate_dict_products(self, e_comerce) -> dict:
    products_dict: dict = {}
    for p in e_comerce.product_list:
      products_dict[p.name] = p
      print(products_dict[p.name])
    return products_dict