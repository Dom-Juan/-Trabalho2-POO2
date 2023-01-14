import PySimpleGUI as sg  # Interface.
import sys  # Sistema.
import pyglet  # Helper para ajudar nos arquivos.
import ctypes  # Tipos da linguagem C.
import platform  # Biblioteca de paltaforma.

from controller.product_controller import ProductController

# import de classes
sys.path.append('../')

# Controllers
from controller.user_controller import UserController

# Views
# Criação de obj.
from views.view_create_obj import create_client_view, create_manager_view, create_manufacturer_view, \
  create_payment_money_view, \
  create_payment_pix_view, create_payment_credit_card_view, create_product_view
# Mostrar os obj.
from views.view_show_obj import show_clients_view, show_managers_view
# Salvar estado do e-comerce.
# Mensagem de sucesso

def result_window(text) -> None:
  layout = [
    [sg.Text(text, key="new")],
    [sg.Button('Ok', pad=(5, 5), size=(20, 1))]
  ]
  window = sg.Window("Alerta!", layout, size=(320, 120), element_justification='c', resizable=True, modal=True)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Ok"]:
      break
    window.close()

# Janela principal.
def main_window(name, e_comerce):
  if int(platform.release()) >= 8:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
  # Instanciando a imobiliária
  user_controller = UserController(client_list=[], manager_list=[])
  product_controller = ProductController(product_list=[])
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
      sg.Text('Guilherme Luis Di Giorgi - 211250767'),
    ],
    [
      sg.Text('Sara Albuquerque - 181254808')
    ],
    [
      sg.Text('Juan Cardoso da Silva - 171257138'),
    ],
    [
      sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))
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
              'Adicionar Eletrônicos',
              'Adicionar Eletrodomésticos',
              'Adicionar Vestuário',
              'Adicionar Móveis',
              'Mostrar todos os Produtos',
            ]
          ],
          [
            '&Fabricantes',
            [
              'Adicionar Fabricante',
              'Mostrar Fabricante',
            ]
          ],
          [
            '&Transportadoras',
            [
              'Adicionar Transportadoras',
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
            'Salvar Estado do programa'
          ]
        ],
      ],
      font=('Cascadia Code', 12),
      tearoff=False,
      pad=(200, 5),
      )
    ]
  )
  layout.append(
    [
      sg.Column(Col, scrollable=True, justification="right", pad=(0, 0), size=(1280, 720))
    ]
  )
  layout2 = []  # layout da janela
  # Configurações da página.
  window = sg.Window(name, layout, size=(1280, 720), resizable=True, enable_close_attempted_event=True, finalize=True)
  # Objetos instanciados com Null para receberem os ponteiros depois.
  while True:
    result: object = None
    event, values = window.read()
    layout2.append([sg.Text('Resultado'), values])
    print(event)
    if event in [sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Sair']:
      break
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
    if event in ['Adicionar Pagamento por cartão']:
      pass
    if event in ['Adicionar Pagamento por dinheiro']:
      pass
    if event in ['Adicionar Pagamento por pix']:
      pass
    # FIM CRIAR OBJETOS.
    # INICIO MOSTRAR INFORMAÇÕES NA GUI.
    if event in ['Mostrar todos Clientes']:
      show_clients_view(user_controller)
    if event in ['Mostrar todos Gerentes']:
      show_managers_view(user_controller)
    # Lógica de criação dos objetos.
    del result
  window.close()
