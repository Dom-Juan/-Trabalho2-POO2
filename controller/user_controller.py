import sys
from models.users.client import Client
from models.users.manager import Manager


class UserController(object):
  def __init__(self, **kwargs):
    """
    Purpose: value
    """
    self._client_list: list = kwargs.get('client_list')
    self._manager_list: list = kwargs.get('manager_list')
    # end alternate constructor

  # Clientes.
  def new_user_client(self, name: str, cpf: str, rg: str, anniversary_date: any,
                      address: str, cep: str, email: str, gold_client: bool):
    """
    Purpose: Create a new user client
    """
    for c in self._client_list:
      if (c.cpf == cpf or c.rg == rg) or c.email == email:
        return False
      else:
        continue
    if gold_client is True:
      gold_client = True
    else:
      gold_client = False
    client: object = Client(
      name=name,
      cpf=cpf,
      rg=rg,
      anniversary_date=anniversary_date,
      address=address,
      cep=cep,
      email=email,
      gold_client=gold_client
    )
    self._client_list.append(client)
    return client

  def get_all_clients(self):
    return self._client_list
  # FIM Clientes.

  # Gerentes.
  def new_user_manager(self, name: str, cpf: str, rg: str, anniversary_date: any,
                       address: str, cep: str, email: str, wage: float, pis: str):
    """
    Purpose: Create a new user client
    """
    for m in self._manager_list:
      if (m.cpf == cpf or m.rg == rg) or m.email == email:
        return False
      else:
        break
    manager: object = Manager(
      name=name,
      cpf=cpf,
      rg=rg,
      anniversary_date=anniversary_date,
      address=address,
      cep=cep,
      email=email,
      wage=wage,
      pis=pis
    )
    self._manager_list.append(manager)
    return manager

  def get_all_managers(self):
    return self._manager_list
  # Fim Gerentes.

  # Retorna um dicionário para ser usado na interface.
  def generate_dict_client(self, e_comerce) -> dict:
    client_dict: dict = {}
    for c in e_comerce.client_list:
      client_dict[c.name] = c
    return client_dict

  # Retorna um dicionário para ser usado na interface.
  # o getter to manager list estava retornando client, arrumado já!
  def generate_dict_manager(self, e_comerce) -> dict:
    manager_dict: dict = {}
    for m in e_comerce.manager_list:
      manager_dict[m.name] = m
    return manager_dict

if __name__ == '__main__':
  print("DEBUG: UserController")
  control = UserController()
  c: object = control.new_user_client(
    name="Client",
    cpf="484.154.465-41",
    rg="34.132.123-1",
    anniversary_date="06/06/1998",
    address="AAAAA",
    cep="12304-34",
    email="a@email.com",
    gold_client=False
  )
  m: object = control.new_user_manager(
    name="Client",
    cpf="484.154.465-41",
    rg="34.132.123-1",
    anniversary_date="06/06/1998",
    address="AAAAA",
    cep="12304-34",
    email="a@email.com",
    wage=5534.23,
    pis="ASDASFASF"
  )
  c.print_obj()
  m.print_obj()
