import sys

sys.path.append('..//..')

print(sys.path)

from models.users.client import Client
from models.users.manager import Manager

class UserController(object):
  def __init__(self, **kwargs):
    """
    Purpose: value
    """
    self._client_list:list = kwargs.get('client_list')
    self._manager_list:list = kwargs.get('manager_list')
    # end alternate constructor
  # Clientes.
  def new_user_client(self, name:str, cpf:str, rg:str, anniversary_date:any,
    address:str, cep:str, email:str, gold_client:str):
    """
    Purpose: Create a new user client
    """
    for c in self._client_list:
      if (c.cpf == cpf or c.rg == rg) or c.email == email:
        return False
      else:
        break
    if gold_client:
      gold_client = True
    else: gold_client = False
    c:object = Client(
      name=name,
      cpf=cpf,
      rg=rg,
      anniversary_date=anniversary_date,
      address=address,
      cep=cep,
      email=email,
      gold_client=gold_client
      )
    self._client_list.add(c)
    return c

  def get_all_clients(self):
    return self._client_list
  # FIM Clientes.

  # Gerentes.
  def new_user_manager(self, name:str, cpf:str, rg:str, anniversary_date:any,
    address:str, cep:str, email:str, wage:float, pis:str):
    """
    Purpose: Create a new user client
    """
    for m in self._manager_list:
      if (m.cpf == cpf or m.rg == rg) or m.email == email:
        return False
      else:
        break
    m:object = Manager(
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
    self._manager_list.add(m)
    return m

  def get_all_managers(self):
    return self._manager_list
  # Fim Gerentes.
if __name__ == '__main__':
  print("DEBUG: UserController")
  control = UserController()
  c:object = control.new_user_client(
    name="Client",
    cpf="484.154.465-41",
    rg="34.132.123-1",
    anniversary_date="06/06/1998",
    address="AAAAA",
    cep="12304-34",
    email="a@email.com",
    gold_client=False
    )
  m:object = control.new_user_manager(
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