import PySimpleGUI as sg
import sys

from models.product_manufacturer.manufacturer import Manufacturer
from models.shipping_company.shipping_company import ShippingCompany
from views.main_view import result_window

sys.path.append('..\\')


# INÍCIO DA LÓGICA DE CRIAÇÃO DE OBJETOS.
# Criar Clientes.
def create_client_view(user_controller:object):
  layout: list = [
    [
      sg.Text('Nome completo', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('CPF', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('RG', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Data de nascimento', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Endereço', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('CEP', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Email', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Cliente de ouro', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'), expand_x=True, expand_y=True)
    ]
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
  layout: list = [
    [
      sg.Text('Nome completo', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('CPF', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('RG', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Data de nascimento', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Endereço', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('CEP', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Email', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Salário', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Text('PIS', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), expand_x=True, expand_y=True)
    ],
    [
      sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'), expand_x=True, expand_y=True)
    ]
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


# Criar uma Venda
def create_sale_view(sale_controller: object, e_comerce: object, payment_controller, user_controller: object):
  client_dict: dict = {}          # dicionário para selecionar o cliente.
  manager_dict: dict = {}         # dicionário pra selecionar o objecto.
  shipping_company_dict: dict = {}# dicionário pra seleciona a transportadora.
  item_list: list = []            # lista de produtos.
  total_value_to_pay: float = 0.0 # Total a pagar dos produtos, calculado conforme os produtos são adicioandos.
  payment_method: object = None   # Pagamento a ser adicionado
  for c in e_comerce.client_list:
    client_dict[c.name] = c
  for m in user_controller.get_all_managers():
    print(m.name)
    manager_dict[m.name] = m
  for sp in e_comerce.shipping_company_list:
    shipping_company_dict[sp.name] = sp
  products_dict: dict = {}
  for p in e_comerce.product_list:
    products_dict[p.name] = p
    print(products_dict[p.name])
  payment_dict: dict = {}
  for p in payment_controller.payment_list:
    payment_dict[p.name] = p
  layout: list = [
    [
      sg.Text('Cliente:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.Combo(list(client_dict), size=(31, 1), key="client", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Gerente:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.Combo(list(manager_dict), size=(31, 1), key="manager", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Disconto', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="discount_value", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Transportadora:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.Combo(list(shipping_company_dict), size=(31, 1), key="shipping_company", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Lista de produtos:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.Combo(list(products_dict), size=(31, 1), key="product", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Tipo de pagamento:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.Combo(list(payment_dict), size=(31, 1), key="payment", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Quantidade:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="amount", expand_x=True, expand_y=True)
    ],
    [
      sg.Button('Criar', pad=(5, 5), size=(30, 1), button_color=('white', 'green4'), expand_x=True, expand_y=True)
    ],
    [
      sg.Button('Cancelar', pad=(5, 5), size=(30, 1), button_color=('white', 'red4'), expand_x=True, expand_y=True)
    ]
  ]
  window = sg.Window("Criar Cliente", layout, element_justification='c', resizable=True, margins=(5, 5))
  if sale_controller is None:
    result_window('Erro, controller não foi criado direito...')
    return False
  else:
    while True:
      event, values = window.read(close=True)
      if '' in values or None in values:
          result_window('Algum campo está vazio, tente novamente.')
          break
      if event in ["Cancelar", sg.WIN_CLOSED]:
          break
      if event == "Criar":
        print(f"GUI loop, ")
        # Pegando info da gui.
        client: object = client_dict[str(values['client'])]
        manager: object = manager_dict[str(values['manager'])]
        shipping_company: object = shipping_company_dict[str(values['shipping_company'])]
        choosen_product: object = products_dict[str(values['product'])]
        # Adicionando ItemSale obj.
        item: object = sale_controller.create_item_sale(choosen_product, amount=float(values['amount']))
        # Adicionando método de pagamento.
        payment_method: object = payment_dict[str(values['payment'])]
        if item is not None:
          item_list.append(item)
          for i in item_list:
            total_value_to_pay += i.item_value
          return sale_controller.create_sale(
            client=client,
            manager=manager,
            delivery_days=shipping_company.delivery_time,
            item_sales_list=item_list,
            total_value_to_pay=total_value_to_pay,
            payment_method=payment_method,
            shipping_company=shipping_company,
          )
      window.close()


# Criar um produto
def create_product_view(product_controller, manufacturer_list):
  product: object = None
  manufacturer_dict: dict = {}
  for m in manufacturer_list:
    manufacturer_dict[m.name] = m
  layout = [
    [
      sg.Text('Nome:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(33, 1), key="input1", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Descrição:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(33, 1), key="input2", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Data de fabricação:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(33, 1), key="input3", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Preço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(33, 1), key="input4", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Fabricante:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.Combo(list(manufacturer_dict), size=(31, 1), key="input5", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Disponível:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(33, 1), key="input6", expand_x=True, expand_y=True)
    ],
    [
      sg.T("Tipo:"),
      sg.Radio('Móvel', "RADIO1", key="key1"),
      sg.Radio('Eletrodomésticos', "RADIO2", key="key2"),
      sg.Radio('Eletronicos', "RADIO3", key="key3"),
      sg.Radio('Vestuario', "RADIO5", key="key4")
     ],
    [
      sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'), expand_x=True, expand_y=True),
      sg.Button('Resetar valores', pad=(5, 5), size=(20, 1), button_color=('white', 'yellow4'), expand_x=True, expand_y=True),
      sg.Button('Cancelar', pad=(5, 5), size=(20, 1), button_color=('white', 'red4'), expand_x=True, expand_y=True),
    ],
  ]
  window = sg.Window("Adicionar Produto", layout, element_justification='c', resizable=True, margins=(5, 5))
  if product_controller is None:
    result_window('Erro, controller não foi criado direito...')
    return False
  else:
    # Mostrando a GUI, outras funções podem ser chamada.
    while True:
      event, values = window.read(close=True)
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
          result_window('Erro ao criar o produto! Algo deu errado...')
          break
        elif product is False:
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
def create_manufacturer_view(manufacturer_list) -> object:
  layout = [
    [
      sg.Text('CNPJ:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="input1", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Nome:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="input2", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Email:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="input3", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Telefone', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="input4", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Endereço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="input5", expand_x=True, expand_y=True)
    ],
    [
      sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'), expand_x=True, expand_y=True),

      sg.Button('Cancelar', pad=(5, 5), size=(20, 1), button_color=('white', 'red4'), expand_x=True, expand_y=True),
    ],
  ]
  window = sg.Window("Adicionar Fabricante", layout, element_justification='c', resizable=True, margins=(5, 5))
  if manufacturer_list is None:
    result_window('Erro, controller não foi criado direito...')
    return False
  else:
    # Mostrando a GUI, outras funções podem ser chamada.
    while True:
      event, values = window.read(close=True)
      print(event)
      print(values)
      if event == sg.WIN_CLOSED or event == "Cancelar":
        break
      if event in ['Criar']:
        manufacturer: object = Manufacturer(
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
    window.close()


# Criar Transportadora.
def create_shipping_company_view(shipping_company_list):
  layout = [
    [
      sg.Text('CNPJ:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="cnpj", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Nome:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="name", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Email:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="email", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Telefone:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="phone_number", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Endereço', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="address", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Tempo de entrega:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="delivery_time", expand_x=True, expand_y=True)
    ],
    [
      sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'), expand_x=True, expand_y=True),
      sg.Button('Cancelar', pad=(5, 5), size=(20, 1), button_color=('white', 'red4'), expand_x=True, expand_y=True),
    ],
  ]
  window = sg.Window("Adicionar Transportadora", layout, element_justification='c', resizable=True, margins=(5, 5))
  if shipping_company_list is None:
    result_window('Erro, lista não foi criado direito...')
    return False
  else:
    # Mostrando a GUI, outras funções podem ser chamada.
    while True:
      event, values = window.read(close=True)
      print(event)
      if event == sg.WIN_CLOSED or event == "Cancelar":
        break
      elif event in ['Criar']:
        c: object = ShippingCompany(
          cnpj=values['cnpj'],
          name=values['name'],
          email=values['email'],
          phone_number=values['phone_number'],
          address=values['address'],
          delivery_time=values['delivery_time']
        )
        if c is None:
          result_window('Erro ao criar o produto! Algo deu errado...')
          break
        elif c is False:
          result_window('Erro ao criar o produto! Produto já existe')
          break
        else:
          result_window('Produto adicionado!')
          return c
    window.close()


# Criar Método de dinheiro
def create_payment_money_view(payment_controller):
  layout = [
    [
      sg.Text('Quantidade:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="input1", expand_x=True, expand_y=True)
    ],
    [
      sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'), expand_x=True, expand_y=True),
      sg.Button('Cancelar', pad=(5, 5), size=(20, 1), button_color=('white', 'red4'), expand_x=True, expand_y=True),
    ],
  ]
  window = sg.Window("Adicionar Fabricante", layout, element_justification='c', resizable=True, margins=(5, 5))
  # Mostrando a GUI, outras funções podem serem chamada.
  while True:
    event, values = window.read(close=True)
    print(event)
    print(values)
    if event == sg.WIN_CLOSED or event == "Cancelar":
      break
    elif event in ['Criar']:
      return payment_controller.create_payment_money(
        values['input1']
      )
  window.close()


# Criar Método de PIX
def create_payment_pix_view(payment_controller):
  layout = [
    [
      sg.Text('Código PIX:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="input1", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Quantidade:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="input2", expand_x=True, expand_y=True)
    ],
    [
      sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'), expand_x=True, expand_y=True),
      sg.Button('Cancelar', pad=(5, 5), size=(20, 1), button_color=('white', 'red4'), expand_x=True, expand_y=True),
    ],
  ]
  window = sg.Window("Adicionar Fabricante", layout, element_justification='c', resizable=True, margins=(5, 5))
  # Mostrando a GUI, outras funções podem serem chamada.
  while True:
    event, values = window.read(close=True)
    print(event)
    print(values)
    if event == sg.WIN_CLOSED or event == "Cancelar":
      break
    elif event in ['Criar']:
      return payment_controller.create_payment_pix(
        values['input1'],
        values['input2']
      )
  window.close()


# Criar Cartão de Crédito
def create_payment_credit_card_view(payment_controller):
  layout = [
    [
      sg.Text('Nome no cartão:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="input1", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Bandeira:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="input2", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Número:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="input3", expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Quantidade:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.InputText(size=(32, 1), key="input4", expand_x=True, expand_y=True)
    ],
    [
      sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'), expand_x=True, expand_y=True),
      sg.Button('Cancelar', pad=(5, 5), size=(20, 1), button_color=('white', 'red4'), expand_x=True, expand_y=True),
    ],
  ]
  window = sg.Window("Adicionar Fabricante", layout, element_justification='c', resizable=True, margins=(5, 5))
  # Mostrando a GUI, outras funções podem serem chamada.
  while True:
    event, values = window.read(close=True)
    print(event)
    print(values)
    if event == sg.WIN_CLOSED or event == "Cancelar":
      break
    elif event in ['Criar']:
      return payment_controller.create_payment_credit_card(
        values['input1'],
        values['input2'],
        values['input3'],
        values['input4']
      )
  window.close()
# FIM DA LÓGICA DE CRIAÇÃO DE OBJETOS.