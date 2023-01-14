import datetime

from models.users.user import User


class Client(User):
  def __init__(self, **kwargs):
    super(Client, self).__init__(**kwargs)
    today = datetime.date.today()
    self._register_date: str = today.strftime("%d/%m/%Y")
    self._gold_client: bool = kwargs['gold_client']
    pass
  # end alternate constructor

  @property
  def register_date(self):
    return self._register_date

  @register_date.setter
  def register_date(self, value: str):
    if value == (None or ''):
      self._register_date: str = self._register_date
    else:
      self._register_date: str = datetime.datetime.strptime(value, '%d/%m/%Y').date().strftime('%d/%m/%Y')
    pass
  
  @property
  def gold_client(self):
    return self._gold_client

  @gold_client.setter
  def gold_client(self, value: int):
    self._gold_client = value
    pass

if __name__ == '__main__':
  print("DEBUG")
  u = Client(
    name="Client",
    cpf="484.154.465-41",
    rg="34.132.123-1",
    anniversary_date="06/06/1998",
    address="AAAAA",
    cep="12304-34",
    email="a@email.com",
    gold_client=False
    )
  u.print_obj()