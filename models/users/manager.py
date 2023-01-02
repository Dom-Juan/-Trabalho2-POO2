import datetime
import PySimpleGUI as sg


from user import User

class Manager(User):
  def __init__(self, **kwargs):
    super(Manager, self).__init__(**kwargs)
    today = datetime.date.today()
    self._register_date = today.strftime("%d/%m/%Y")  # Data de adimissão
    self._wage:float = kwargs.get('wage')
    self.pis:str = kwargs['pis']
    pass
  # end alternate constructor
  
  @property
  def register_date(self):
    return self._register_date

  @register_date.setter
  def register_date(self, value):
    self._register_date = value
    pass
  
  @property
  def wage(self):
    return self._wage

  @wage.setter
  def wage(self, value:float):
    self._wage = value
    pass
  
  @property
  def pis(self):
    return self._pis

  @pis.setter
  def pis(self, value:str):
    self._pis = value
    pass

if __name__ == '__main__':
  print("DEBUG")
  m = Manager(
    name="Manager",
    cpf="484.154.465-41",
    rg="34.132.123-1",
    anniversary_date="06/06/1998",
    address="AAAAA",
    cep="12304-34",
    email="b@email.com",
    wage=5500.50,
    pis="sdasda"
    )
  m.print_obj()
  print(m.wage)