import PySimpleGUI as sg

from models.payment_methods.credit_card import CreditCard
from models.payment_methods.money import Money
from models.payment_methods.pix import Pix
from models.products.clothing import Clothing
from models.products.domestic_appliance import DomesticAppliance
from models.products.eletronics import Eletronics
from models.products.furnitures import Furnitures
from strategy.context import Context
from strategy.strategy import ConcreteStrategyHighest, ConcreteStrategyLowest
from views.main_view import result_window


# Mostrar Objetos
# Monstrando os Clientes
def show_clients_view(e_comerce):
  user_list: list = e_comerce.client_list
  print(user_list)
  layout: list = []
  Col: list = []
  if None in user_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for client in user_list:
    if client is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(client.user_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(client.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('CPF:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(client.cpf), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('RG:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(client.rg), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Ano de nascimento:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(client.anniversary_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Endereço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(client.address), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('CEP:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(client.cep), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Email:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(client.email), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Cliente de Ouro:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(client.gold_client), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Data de registro:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(client.register_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([
    sg.Column(
      Col,
      size=(640, 750),
      element_justification='c',
      scrollable=True,
      vertical_scroll_only=True,
      expand_x=True,
      expand_y=True
    )
  ])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Clientes", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostrando todos os clientes que "são de ouro".
def show_golden_clients_view(e_comerce):
  user_list: list = e_comerce.client_list
  print(user_list)
  layout: list = []
  Col: list = []
  if None in user_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for client in user_list:
    if client is not None:
      if client.gold_client is True:
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(client.user_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append(
          [
            sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(client.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('CPF:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(client.cpf), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('RG:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(client.rg), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Ano de nascimento:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(client.anniversary_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Endereço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(client.address), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('CEP:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(client.cep), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Email:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(client.email), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Cliente de Ouro:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(client.gold_client), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Data de registro:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(client.register_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([
    sg.Column(
      Col,
      size=(640, 750),
      element_justification='c',
      scrollable=True,
      vertical_scroll_only=True,
      expand_x=True,
      expand_y=True
    )
  ])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Clientes", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Monstrando os Gerentes.
def show_managers_view(e_comerce):
  manager_list: list = e_comerce.manager_list
  print(manager_list)
  layout: list = []
  Col: list = []
  if None in manager_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for manager in manager_list:
    if manager is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(manager.user_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manager.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('CPF:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manager.cpf), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('RG:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manager.rg), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Ano de nascimento:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manager.anniversary_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Endereço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manager.address), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('CEP:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manager.cep), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Email:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manager.email), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Salário:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manager.wage), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('pis:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manager.pis), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Data de adimissão:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manager.register_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Gerentes", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra todas as vendas.
def show_sales_view(e_comerce: object, sale_controller: object):
  print(e_comerce.sales_list)
  layout: list = []
  Col: list = []
  if None in e_comerce.sales_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for sale in e_comerce.sales_list:
    if sale is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(sale.sale_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append([
        sg.Text('Cliente:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(sale.client.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append([
        sg.Text('Gerente:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(sale.manager.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append([
        sg.Text('Data de venda:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(sale.sale_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append([
        sg.Text('Data de entrega:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(sale.delivery_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append([
        sg.Text('Quantidade de itens pedido:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(int(sale_controller.get_item_amount(sale))), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
      ])
      Col.append([
        sg.Text('Valor total da compra:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(sale.calc_total_sale_value()), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append([
        sg.Text('Compra com desconto:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(sale.calc_total_sale_value()), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append([
        sg.Text('Forma de pagamento:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(sale.payment_method.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append([
        sg.Text('Transportadora:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(sale.shipping_company.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra as vendas feitas com dinheiro.
def show_sales_made_with_money_view(e_comerce: object, sale_controller: object):
  print(e_comerce.sales_list)
  layout: list = []
  Col: list = []
  if None in e_comerce.sales_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for sale in e_comerce.sales_list:
    if sale is not None:
      if isinstance(sale.payment_method, Money):
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.sale_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Cliente:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.client.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Gerente:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.manager.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Data de venda:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.sale_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Data de entrega:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.delivery_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Quantidade de itens pedido:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(int(sale_controller.get_item_amount(sale))), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ])
        Col.append([
          sg.Text('Valor total da compra:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.calc_total_sale_value()), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Compra com desconto:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.calc_total_sale_value()), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Forma de pagamento:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.payment_method.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Transportadora:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.shipping_company.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra as vendas feitas com cartão de crédito.
def show_sales_made_with_credit_card_view(e_comerce: object, sale_controller: object):
  print(e_comerce.sales_list)
  layout: list = []
  Col: list = []
  if None in e_comerce.sales_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for sale in e_comerce.sales_list:
    if sale is not None:
      if isinstance(sale.payment_method, CreditCard):
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.sale_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Cliente:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.client.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Gerente:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.manager.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Data de venda:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.sale_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Data de entrega:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.delivery_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Quantidade de itens pedido:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(int(sale_controller.get_item_amount(sale))), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ])
        Col.append([
          sg.Text('Valor total da compra:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.calc_total_sale_value()), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Compra com desconto:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.calc_total_sale_value()), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Forma de pagamento:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.payment_method.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Transportadora:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.shipping_company.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra as vendas feitas com pix.
def show_sales_made_with_pix_view(e_comerce: object, sale_controller: object):
  print(e_comerce.sales_list)
  layout: list = []
  Col: list = []
  if None in e_comerce.sales_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for sale in e_comerce.sales_list:
    if sale is not None:
      if isinstance(sale.payment_method, Pix):
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.sale_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Cliente:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.client.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Gerente:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.manager.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Data de venda:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.sale_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Data de entrega:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.delivery_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Quantidade de itens pedido:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(int(sale_controller.get_item_amount(sale))), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ])
        Col.append([
          sg.Text('Valor total da compra:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.calc_total_sale_value()), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Compra com desconto:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.calc_total_sale_value()), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Forma de pagamento:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.payment_method.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([
          sg.Text('Transportadora:', pad=(5, 5), size=(30, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(sale.shipping_company.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Modal de ajuda do mostrar as vendas na data X e o lucro nessa data.
def modal_show_sales_by_monthly_profit_view(sale_list: list, date: str) -> True:
  profits: float = 0.0
  Col: list = []
  for sale in sale_list:
    if sale is not None:
      if sale.sale_date == date:
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(sale.sale_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Cliente:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(sale.client.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Gerente:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(sale.manager.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Quantidade de Produtos:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(len(sale.item_sale_list)), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        for item in sale.item_sale_list:
          Col.append([
            sg.Text('Produto:', pad=(5, 5), size=(20, 1)),  # Label
            sg.Text(str(item.product.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
          ])
        Col.append([
          sg.Text('Data da venda:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(sale.sale_date), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Preço da venda:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(sale.calc_total_sale_value()), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Forma de pagamento:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(sale.payment_method.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        profits += sale.calc_total_sale_value()
      Col.append([sg.HSeparator()])
  Col.append([sg.HSeparator()])
  Col.append([
    sg.Text('Lucro total:', pad=(5, 5), size=(20, 1)),  # Label
    sg.Text(str(profits), pad=(5, 5), size=(45, 1))  # Valor do obj.
  ])
  Col.append([sg.HSeparator()])
  # Inicialização da interface.
  layout = []
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando todas as vendas e lucro total", layout, element_justification='c', resizable=True,
                     finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra as vendas na data X e o lucro nessa data.
def show_sales_by_monthly_profit_view(e_comerce):
  layout = [
    [sg.Text('Digite uma data válida:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Button('Mostrar', pad=(5, 5), size=(21, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Mostrar vendas e lucro em data", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read(close=True)
    if values is not None:
      if '' in values:
        result_window('Algum campo está vazio, tente novamente.')
        break
      if event in ["Exit", sg.WIN_CLOSED]:
        break
      if event == "Mostrar":
        modal_show_sales_by_monthly_profit_view(e_comerce.sales_list, str(values[0]))
        break
  window.close()


# Modal da visualização do cliente X
def modal_show_sales_by_client_view(sale_list: list, client: object) -> True:
  profits: float = 0.0
  Col: list = []
  for sale in sale_list:
    if sale is not None:
      if sale.client.user_code == client.user_code:
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(sale.sale_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Cliente:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(sale.client.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Gerente:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(sale.manager.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Quantidade de Produtos:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(len(sale.item_sale_list)), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        for item in sale.item_sale_list:
          Col.append([
            sg.Text('Produto:', pad=(5, 5), size=(20, 1)),  # Label
            sg.Text(str(item.product.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
          ])
        Col.append([
          sg.Text('Data da venda:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(sale.sale_date), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Preço da venda:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(sale.calc_total_sale_value_with_discount()), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Forma de pagamento:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(sale.payment_method.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        profits += sale.calc_total_sale_value_with_discount()
        Col.append([sg.HSeparator()])
  Col.append([sg.HSeparator()])
  Col.append([
    sg.Text('Total pago pelo cliente:', pad=(5, 5), size=(20, 1)),  # Label
    sg.Text(str(profits), pad=(5, 5), size=(45, 1))  # Valor do obj.
  ])
  Col.append([sg.HSeparator()])
  # Inicialização da interface.
  layout = []
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando todas as vendas e lucro total", layout, element_justification='c', resizable=True,
                     finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra as vendas de um cliente X.
def show_sales_by_client_view(e_comerce: object, user_controller: object):
  client_dict: dict = user_controller.generate_dict_client(e_comerce)
  layout = [
    [
      sg.Text('Selecione o Cliente:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
      sg.Combo(list(client_dict), size=(31, 1), key="client", expand_x=True, expand_y=True)
    ],
    [
      sg.Button('Mostrar', pad=(5, 5), size=(21, 1), button_color=('white', 'green4'), expand_x=True, expand_y=True)
    ]
  ]
  window = sg.Window("Mostrar vendas e lucro em data", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read(close=True)
    if values is not None:
      if '' in values:
        result_window('Algum campo está vazio, tente novamente.')
        break
      if event in ["Exit", sg.WIN_CLOSED]:
        break
      if event == "Mostrar":
        modal_show_sales_by_client_view(e_comerce.sales_list, client_dict[str(values['client'])])
        break
  window.close()


# Mostra todos os produtos.
def show_products_view(product_list):
  print(product_list)
  layout: list = []
  Col: list = []
  if None in product_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for product in product_list:
    if product is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(product.product_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Descrição:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.description), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Data de criação:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.manufacture_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Preço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.value_price), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Disponível:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.available), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Fabricante:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.manufacturer.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra todos os produtos pelo preço mais alto.
def show_products_by_highest_view(product_list):
  print(product_list)
  layout: list = []
  Col: list = []
  if None in product_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  context = Context(ConcreteStrategyHighest())
  product_list = context.filter_alg(product_list)
  for product in product_list:
    if product is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(product.product_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Descrição:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.description), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Data de criação:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.manufacture_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Preço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.value_price), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Disponível:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.available), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Fabricante:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.manufacturer.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra todos os produtos pelo preço mais barato.
def show_products_by_lowest_view(product_list):
  print(product_list)
  layout: list = []
  Col: list = []
  if None in product_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  context = Context(ConcreteStrategyLowest())
  product_list = context.filter_alg(product_list)
  for product in product_list:
    if product is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(product.product_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Descrição:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.description), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Data de criação:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.manufacture_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Preço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.value_price), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Disponível:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.available), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Fabricante:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(product.manufacturer.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra todos os produtos do tipos Móveis.
def show_furnitures_products_view(product_list):
  print(product_list)
  layout: list = []
  Col: list = []
  if None in product_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for product in product_list:
    if product is not None:
      # layout da página.
      if isinstance(product, Furnitures):
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(product.product_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append(
          [
            sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Descrição:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.description), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Data de criação:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.manufacture_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Preço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.value_price), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Disponível:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.available), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Fabricante:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.manufacturer.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra todos os produtos do tipo Eletrodomésticos.
def show_domestic_appliance_products_view(product_list):
  print(product_list)
  layout: list = []
  Col: list = []
  if None in product_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for product in product_list:
    if product is not None:
      if isinstance(product, DomesticAppliance):
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(product.product_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append(
          [
            sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Descrição:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.description), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Data de criação:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.manufacture_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Preço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.value_price), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Disponível:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.available), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Fabricante:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.manufacturer.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra todos os produtos do tipos eletrônicos.
def show_eletronics_products_view(product_list):
  print(product_list)
  layout: list = []
  Col: list = []
  if None in product_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for product in product_list:
    if product is not None:
      if isinstance(product, Eletronics):
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(product.product_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append(
          [
            sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Descrição:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.description), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Data de criação:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.manufacture_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Preço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.value_price), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Disponível:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.available), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Fabricante:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.manufacturer.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra todos os produtos do tipos Roupa.
def show_clothing_products_view(product_list):
  print(product_list)
  layout: list = []
  Col: list = []
  if None in product_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for product in product_list:
    if product is not None:
      if isinstance(product, Clothing):
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
          sg.Text(str(product.product_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
        ])
        Col.append(
          [
            sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Descrição:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.description), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Data de criação:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.manufacture_date), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Preço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.value_price), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Disponível:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.available), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append(
          [
            sg.Text('Fabricante:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
            sg.Text(str(product.manufacturer.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
          ]
        )
        Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra todas as fabricantes.
def show_manufacturer_view(manufacturer_list):
  print(manufacturer_list)
  layout: list = []
  Col: list = []
  if None in manufacturer_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for manufacturer in manufacturer_list:
    if manufacturer is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(manufacturer.manufacturer_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append([
        sg.Text('CNPJ:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(manufacturer.cnpj), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manufacturer.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Descrição:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manufacturer.description), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Email:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manufacturer.email), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Telefone:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manufacturer.phone), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Endereço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manufacturer.address), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra sem repetição, os vencedores das fabricantes que mais venderam produtos.
def show_most_manufacturer_product_sold_view(manufacturer_list: list, sales_list: list, sale_controller: object):
  most_manufacturer_product_sold_list = sale_controller.get_manufacturers_with_most_sold_products(
    sales_list, manufacturer_list
  )
  layout: list = []
  Col: list = []
  if None in most_manufacturer_product_sold_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for manufacturer in most_manufacturer_product_sold_list:
    if manufacturer is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(manufacturer.manufacturer_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append([
        sg.Text('CNPJ:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(manufacturer.cnpj), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manufacturer.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Descrição:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manufacturer.description), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Email:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manufacturer.email), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Telefone:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manufacturer.phone), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Endereço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(manufacturer.address), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra todos as transportadoras.
def show_shipping_company_view(shipping_company_list):
  print(shipping_company_list)
  layout: list = []
  Col: list = []
  if None in shipping_company_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for company in shipping_company_list:
    if company is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(company.code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append([
        sg.Text('CNPJ:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(company.cnpj), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(company.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Email:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(company.email), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Telefone:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(company.phone_number), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Endereço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(company.address), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Tempo de entrega em dias:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(company.delivery_time), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra sem repetição, os vencedores das transportadoras que mais transportaram produtos.
def show_most_shipping_made_view(sale_controller: object, sales_list: object, shipping_company_list: object):
  most_shipping_made_list = sale_controller.get_shipping_company_with_more_sales(sales_list, shipping_company_list)
  layout: list = []
  Col: list = []
  if None in most_shipping_made_list:
    result_window('Erro, nenhum resultado pego!')
    return False
  for company in most_shipping_made_list:
    if company is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(company.code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append([
        sg.Text('CNPJ:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),  # Label
        sg.Text(str(company.cnpj), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Nome: ', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(company.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Email:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(company.email), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Telefone:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(company.phone_number), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Endereço:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(company.address), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Tempo de entrega em dias:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(company.delivery_time), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 750),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Produtos", layout, element_justification='c', resizable=True, finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostrar todos os pagamentos
def show_payments_view(payment_controller):
  layout = []
  Col = []
  if None in payment_controller.payment_list:
    result_window('Erro, existe NULL/None no vetor.')
    return False
  for payment in payment_controller.payment_list:
    Col.append([sg.HSeparator()])
    Col.append(
      [
        sg.Text('ID:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
        sg.Text(str(payment.recipe_note), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
      ]
    )
    if isinstance(payment, CreditCard):
      Col.append(
        [
          sg.Text('Nome no cartão:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(payment.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Bandeira:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(payment.flag), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Número do cartão:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(payment.card_number), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
    elif isinstance(payment, Pix):
      Col.append(
        [
          sg.Text('Tipo:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(payment.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
      Col.append(
        [
          sg.Text('Código PIX:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(payment.pix_code), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
    elif isinstance(payment, Money):
      Col.append(
        [
          sg.Text('Tipo:', pad=(5, 5), size=(20, 1), expand_x=True, expand_y=True),
          sg.Text(str(payment.name), pad=(5, 5), size=(45, 1), expand_x=True, expand_y=True)
        ]
      )
    Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [
      sg.Column(
        Col,
        size=(640, 800),
        element_justification='c',
        scrollable=True,
        vertical_scroll_only=True,
        expand_x=True,
        expand_y=True
      )
    ]
  )
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os métodos de pagamento", layout, element_justification='c',
                     resizable=True, finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()
# FIM Mostrar Objetos
