import PySimpleGUI as sg
import sys

from models.product_manufacturer.manufacturer import Manufacturer

sys.path.append('..\\')


# Mensagem de sucesso
def result_window(text) -> None:
  layout = [
    [sg.Text(text, key="new")],
    [sg.Button('Ok', pad=(5, 5), size=(20, 1))]
  ]
  window = sg.Window(
    "Alerta!",
    layout,
    size=(320, 120),
    element_justification='c',
    resizable=True,
    modal=True
    )
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Ok"]:
      break
  window.close()

# INÍCIO DA LÓGICA DE CRIAÇÃO DE OBJETOS.
# Criar Clientes.
def create_client_view(user_controller:object):
  layout = [
    [sg.Text('Nome completo', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('CPF', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('RG', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Data de nascimento', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Endereço', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('CEP', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Email', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Cliente de ouro', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Criar Cliente", layout, element_justification='c', resizable=True, margins=(5, 5))
  if user_controller == None:
    result_window('Erro, controller não foi criado direito...')
    return False
  else:
    while True:
      event, values = window.read(close=True)
      if '' in values or None in values:
          result_window('Algum campo está vazio, tente novamente.')
          break
      if event in ["Exit", sg.WIN_CLOSED]:
          break
      if event == "Criar":
        print(f"GUI loop, ")
        return user_controller.new_user_client(
          name=values[0],
          cpf=values[1],
          rg=values[2],
          anniversary_date=values[3],
          address=values[4],
          cep=values[5],
          email=values[6],
          gold_client=values[7],
        )
      window.close()
# Criar Gerentes.
def create_manager_view(user_controller:object):
  layout = [
    [sg.Text('Nome completo', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('CPF', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('RG', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Data de nascimento', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Endereço', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('CEP', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Email', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Salário', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('PIS', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Criar Cliente", layout, element_justification='c', resizable=True, margins=(5, 5))
  if user_controller is None:
    result_window('Erro, controller não foi criado direito...')
    return False
  else:
    while True:
      event, values = window.read(close=True)
      if '' in values or None in values:
          result_window('Algum campo está vazio, tente novamente.')
          break
      if event in ["Exit", sg.WIN_CLOSED]:
          break
      if event == "Criar":
        print(f"GUI loop, ")
        return user_controller.new_user_manager(
          name=values[0],
          cpf=values[1],
          rg=values[2],
          anniversary_date=values[3],
          address=values[4],
          cep=values[5],
          email=values[6],
          wage=values[7],
          pis=values[8],
        )
      window.close()


# Criar um produto
def create_product_view(product_controller, manufacturer_list):
  product: object = None
  manufacturer_dict: dict = {}
  for m in manufacturer_list:
    manufacturer_dict[m.name] = m
  layout = [
    [sg.Text('Nome:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1), key="input1")],
    [sg.Text('Descrição:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1), key="input2")],
    [sg.Text('Data de fabricação:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1), key="input3")],
    [sg.Text('Preço:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1), key="input4")],
    [sg.Text('Fabricante', pad=(5, 5), size=(20, 1)), sg.Combo(list(manufacturer_dict), size=(32, 1), key="input5")],
    [sg.Text('Disponível:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1), key="input6")],
    [
      sg.T("Tipo:"),
      sg.Radio('Móvel', "RADIO1", key="key1", default=True),
      sg.Radio('Eletrodomésticos', "RADIO2", key="key2"),
      sg.Radio('Eletronicos', "RADIO3", key="key3"),
      sg.Radio('Vestuario', "RADIO5", key="key4")
     ],
    [
      sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4')),
      sg.Button('Resetar valores', pad=(5, 5), size=(20, 1), button_color=('white', 'yellow4')),
      sg.Button('Cancelar', pad=(5, 5), size=(20, 1), button_color=('white', 'red4')),
    ],
  ]
  window = sg.Window("Adicionar Produto", layout, element_justification='c', resizable=True, margins=(5, 5))
  if product_controller is None:
    result_window('Erro, controller não foi criado direito...')
    return False
  else:
    # Mostrando a GUI, outras funções podem serem chamada.
    while True:
      event, values = window.read()
      print(event)
      if event == sg.WIN_CLOSED or event == "Cancelar":
        break
      elif event in ['Criar']:
        manufacturer: object = manufacturer_dict[str(values['input5'])]
        if values['key1'] is True:
          product = product_controller.create_product_furnitures(
            values['input1'],
            values['input2'],
            values['input3'],
            values['input4'],
            manufacturer,
            values['input6'],
          )
        elif values['key2'] is True:
          product = product_controller.create_product_domestic_appliance(
            values['input1'],
            values['input2'],
            values['input3'],
            values['input4'],
            manufacturer,
            values['input6'],
          )
        elif values['key3'] is True:
          product = product_controller.create_product_eletronics(
            values['input1'],
            values['input2'],
            values['input3'],
            values['input4'],
            manufacturer,
            values['input6'],
          )
        elif values['key4'] is True:
          product = product_controller.create_product_clothing(
            values['input1'],
            values['input2'],
            values['input3'],
            values['input4'],
            manufacturer,
            values['input6'],
          )
        if product is None:
          result_window('Erro ao criar o produto! Produto já existe')
          break
        else:
          result_window('Produto adicionado!')
          return product
      elif event in ['Resetar valores']:
        # Resetando os inputs
        window.find_element("input1").Update('')
        window.find_element("input2").Update('')
        window.find_element("input3").Update('')
        window.find_element("input4").Update('')
        window.find_element("input5").Update('')
        window.find_element("input6").Update('')
        # Resetando os botões Radios.
        window["key1"].reset_group()
        window["key2"].reset_group()
        window["key3"].reset_group()
        window["key4"].reset_group()
        continue
    window.close()


# Criar Fabricante
def create_manufacturer_view(manufacturer_list)-> object:
  manufacturer: object = None
  layout = [
    [sg.Text('CNPJ:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1), key="input1")],
    [sg.Text('Nome:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1), key="input2")],
    [sg.Text('Email:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1), key="input3")],
    [sg.Text('Telefone', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1), key="input4")],
    [sg.Text('Endereço:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1), key="input5")],
    [
      sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4')),
      sg.Button('Resetar valores', pad=(5, 5), size=(20, 1), button_color=('white', 'yellow4')),
      sg.Button('Cancelar', pad=(5, 5), size=(20, 1), button_color=('white', 'red4')),
    ],
  ]
  window = sg.Window("Adicionar Fabricante", layout, element_justification='c', resizable=True, margins=(5, 5))
  if manufacturer_list is None:
    result_window('Erro, controller não foi criado direito...')
    return False
  else:
    # Mostrando a GUI, outras funções podem serem chamada.
    while True:
      event, values = window.read()
      print(event)
      print(values)
      if event == sg.WIN_CLOSED or event == "Cancelar":
        break
      elif event in ['Criar']:
        manufacturer = Manufacturer(
          cnpj=values['input1'],
          name=values['input2'],
          email=values['input3'],
          phone=values['input4'],
          address=values['input5'],
        )
        if manufacturer is None:
          result_window('Erro ao criar o produto! Produto já existe')
          return None
        return manufacturer
      elif event in ['Resetar valores']:
        # Resetando os inputs
        window.find_element("input1").Update('')
        window.find_element("input2").Update('')
        window.find_element("input3").Update('')
        window.find_element("input4").Update('')
        window.find_element("input5").Update('')
        continue
    window.close()

# Criar Cartão de crédito
def create_payment_money_view(payment_controller):
  pass


def create_payment_pix_view(payment_controller):
  pass


def create_payment_credit_card_view(payment_controller):
  pass
# FIM DA LÓGICA DE CRIAÇÃO DE OBJETOS.