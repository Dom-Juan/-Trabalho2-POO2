import PySimpleGUI as sg  # Interface.
import sys  # Sistema.
import pyglet  # Helper para ajudar nos arquivos.
import ctypes  # Tipos da linguagem C.
import platform  # Biblioteca de paltaforma.

from controller.sale_controller import SaleController

# import de classes
sys.path.append('../')

# Controllers
from controller.user_controller import UserController
from controller.payment_controller import PaymentController
from controller.product_controller import ProductController
from controller.save_controller import save_config
from controller.load_controller import load_config

# Views
# Criação de obj.
from views.view_create_obj import create_client_view, create_manager_view, create_manufacturer_view, \
  create_payment_money_view, \
  create_payment_pix_view, create_payment_credit_card_view, create_product_view, create_sale_view, \
  create_shipping_company_view
# Mostrar os obj.
from views.view_show_obj import show_clients_view, show_managers_view, show_manufacturer_view, show_payments_view, \
  show_products_view, show_shipping_company_view


# Salvar estado do e-comerce.
# Mensagem de sucesso
def result_window(text) -> None:
  layout: list = [
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

# Janela principal.
def main_window(name, e_comerce):
  if int(platform.release()) >= 8:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
  # Instanciando os controllers.
  user_controller: object = UserController(client_list=[], manager_list=[])
  sale_controller: object = SaleController(sales_list=[], item_sale_list=[])
  product_controller: object = ProductController(product_list=[])
  payment_controller: object = PaymentController(payment_list=[])
  # Carregando as fontes de texto.
  pyglet.font.add_file(r"./fonts/Roboto-Regular.ttf")
  font1 = ("Roboto Regular", 12)
  sg.set_options(font=font1)
  sg.theme('SystemDefault')
  Col = [
    [
      sg.HSeparator()
    ],
    [
      sg.Text('Feito por:'),
    ],
    [
      sg.Text('Guilherme Luis Di Giorgi - 211250767', expand_x=True, expand_y=True),
    ],
    [
      sg.Text('Sara Albuquerque - 181254808', expand_x=True, expand_y=True)
    ],
    [
      sg.Text('Juan Cardoso da Silva - 171257138', expand_x=True, expand_y=True),
    ],
    [
      sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'), expand_x=True, expand_y=True)
    ]
  ]
  layout = []
  layout.append(
    [
      sg.Menu(
        [
          [
            '&Clientes',
            [
              'Criar Cliente',
              'Mostrar todos Clientes',
            ],
          ],
          [
            '&Gerentes',
            [
              'Criar Gerente',
              'Mostrar todos Gerentes',
            ],
          ],
          [
            '&Vendas',
            [
              'Criar Venda',
              'Mostrar Vendas',
            ]
          ],
          [
            '&Produtos',
            [
              'Adicionar Produto',
              'Mostrar todos Produtos',
            ]
          ],
          [
            '&Fabricantes',
            [
              'Adicionar Fabricante',
              'Mostrar todos Fabricantes',
            ]
          ],
          [
            '&Transportadoras',
            [
              'Adicionar Transportadora',
              'Mostrar todas Transportadoras',
            ]
          ],
          [
            '&Pagamento',
            [
              'Adicionar Pagamento por cartão',
              'Adicionar Pagamento por dinheiro',
              'Adicionar Pagamento por pix',
              'Mostrar todos pagamentos',
            ]
          ],
          [
            '&E-Comerce',
          [
            'Salvar arquivo do programa',
            'Carregar arquivo do programa'
          ]
        ],
      ],
      font=('Cascadia Code', 12),
      tearoff=False,
      pad=(200, 5)
      )
    ]
  )
  layout.append(
    [
      sg.Column(Col, justification="right", pad=(0, 0), size=(800, 200), expand_x=True, expand_y=True)
    ]
  )
  layout2 = []  # layout da janela
  # Configurações da página.
  window = sg.Window(name, layout, size=(680, 200), resizable=True, enable_close_attempted_event=True, finalize=True)
  # Objetos instanciados com Null para receberem os ponteiros depois.
  while True:
    result: object = None
    event, values = window.read()
    layout2.append([sg.Text('Resultado'), values])
    print(event)
    if event in [sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Sair']:
      break
    if event in ['Salvar arquivo do programa']:
      result_window(
        str(save_config(e_comerce, user_controller, sale_controller, product_controller, payment_controller))
      )
    if event in ['Carregar arquivo do programa']:
      data_array = load_config()
      if data_array is None:
        result_window("Erro ao ler todos os dados!")
      else:
        e_comerce, user_controller, sale_controller, product_controller, payment_controller = data_array
        if e_comerce is None:
          result_window("Erro ao ler o comercio digital")
        elif user_controller is None:
          result_window("Erro ao ler o dados usuário")
        elif sale_controller is None:
          result_window("Erro ao ler os dados de vendas")
        elif product_controller is None:
          result_window("Erro ao ler os dados de produtos")
        elif payment_controller is None:
          result_window("Erro ao ler os dados de pagamentos")
        else:
          result_window("Sucesso ao carregar os dados!")
    if event in ['Criar Cliente']:
      result = create_client_view(user_controller)
      if result is None:
        result_window('Operação Falhou!')
      else:
        e_comerce.client_list = result
        result_window('Operação feita com sucesso')
    if event in ['Criar Gerente']:
      result = create_manager_view(user_controller)
      if result is None:
        result_window('Operação Falhou!')
      else:
        e_comerce.manager_list = result
        result_window('Operação feita com sucesso')
    if event in ['Criar Venda']:
      result = create_sale_view(sale_controller, e_comerce, payment_controller)
      if result is None:
        result_window('Operação Falhou!')
      else:
        e_comerce.sales_list = result
        result_window('Operação feita com sucesso')
    if event in ['Adicionar Produto']:
      result = create_product_view(product_controller, e_comerce.manufacturer_list)
      if result is None:
        result_window('Operação Falhou!')
      else:
        e_comerce.product_list = result
        result_window('Operação feita com sucesso')
    if event in ['Adicionar Fabricante']:
      result = create_manufacturer_view(e_comerce.manufacturer_list)
      if result is None:
        result_window('Operação Falhou!')
      else:
        e_comerce.manufacturer_list = result
        result_window('Operação feita com sucesso')
    if event in ['Adicionar Transportadora']:
      result = create_shipping_company_view(e_comerce.shipping_company_list)
      if result is None:
        result_window('Operação Falhou!')
      else:
        e_comerce.shipping_company_list = result
        result_window('Operação feita com sucesso')
    if event in ['Adicionar Pagamento por cartão']: # Cartão.
      result = create_payment_credit_card_view(payment_controller)
      if result is None:
        result_window('Operação Falhou!')
      else:
        payment_controller.payment_list = result
        result_window('Operação feita com sucesso')
    if event in ['Adicionar Pagamento por dinheiro']: # Dinheiro.
      result = create_payment_money_view(payment_controller)
      if result is None:
        result_window('Operação Falhou!')
      else:
        payment_controller.payment_list = result
        result_window('Operação feita com sucesso')
    if event in ['Adicionar Pagamento por pix']:  # PIX.
      result = create_payment_pix_view(payment_controller)
      if result is None:
        result_window('Operação Falhou!')
      else:
        payment_controller.payment_list = result
        result_window('Operação feita com sucesso')
    # FIM CRIAR OBJETOS.
    # INICIO MOSTRAR INFORMAÇÕES NA GUI.
    if event in ['Mostrar todos Clientes']:
      show_clients_view(user_controller)
    if event in ['Mostrar todos Gerentes']:
      show_managers_view(user_controller)
    if event in ['Mostrar todos Produtos']:
      show_products_view(e_comerce.product_list)
    if event in ['Mostrar todos Fabricantes']:
      show_manufacturer_view(e_comerce.manufacturer_list)
    if event in ['Mostrar todas Transportadoras']:
      show_shipping_company_view(e_comerce.shipping_company_list)
    if event in ['Mostrar todos pagamentos']:
      show_payments_view(payment_controller)
    # Lógica de criação dos objetos.
    del result
  window.close()
