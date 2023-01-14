import random
import datetime
import PySimpleGUI as sg

class User(object):
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)
    self._user_code = random.sample(range(9999), 1)[0]  # Retorna uma lista de números inteiros sem repetição.
    self._name: str = kwargs['name']
    self._cpf: str = kwargs['cpf']
    self._rg: str = kwargs['rg']
    if kwargs['anniversary_date'] == (None or ''):
      self._anniversary_date: any = None
    else:
      self._anniversary_date: str = datetime.datetime.strptime(kwargs['anniversary_date'], '%d/%m/%Y').date().strftime('%d/%m/%Y')
    self._address: str = kwargs['address']
    self._cep: str = kwargs['cep']
    self._email: str = kwargs['email']
  # end constructor
  
  @property
  def user_code(self):
    return self._user_code

  @user_code.setter
  def user_code(self, value: int):
    """_summary_
    Args:
        value (int): _description_
    """   
    self._user_code = value
    pass
  
  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value: str):
    """_summary_
    Args:
        value (str): _description_
    """    
    self._name = value
    pass

  @property
  def cpf(self):
    return self._cpf

  @cpf.setter
  def cpf(self, value: str):
    """_summary_
    Args:
        value (str): _description_
    """    
    self._cpf = value
    pass

  @property
  def rg(self):
    return self._rg

  @rg.setter
  def rg(self, value: str):
    """_summary_
    Args:
        value (str): _description_
    """    
    self._rg = value
    pass

  @property
  def anniversary_date(self):
    return self._anniversary_date

  @anniversary_date.setter
  def anniversary_date(self, value: any):
    """_summary_
    Args:
        value (any): _description_
    """  
    self._anniversary_date = datetime.strptime(value, '%d/%m/%Y').date().strftime('%d/%m/%Y')
    pass

  @property
  def address(self):
    return self._address

  @address.setter
  def address(self, value: str):
    """_summary_
    Args:
        value (str): _description_
    """    
    self._address = value
    pass

  @property
  def cep(self):
    return self._cep

  @cep.setter
  def cep(self, value: str):
    """_summary_
    Args:
        value (str): _description_
    """    
    self._cep = value
    pass
  
  @property
  def email(self):
    return self._email

  @email.setter
  def email(self, value: str):
    """_summary_
    Args:
        value (str): _description_
    """    
    self._email = value
    pass
  
  def print_obj(self):
    self._layout = [
      [sg.Text(self.user_code)],
      [sg.Text(self.name)],
      [sg.Text(self.cpf)],
      [sg.Text(self.rg)],
      [sg.Text(self.anniversary_date)],
      [sg.Text(self.address)],
      [sg.Text(self.cep)],
      [sg.Text(self.email)],
      [sg.Button('Ok')]
    ]
    window = sg.Window("Print do Cliente.", self._layout, size=(640, 480), resizable=True, modal=True)
    while True:
      event, values = window.read()
      if event in ["Exit", sg.WIN_CLOSED, "Ok"]:
        break
    window.close()
    pass