import PySimpleGUI as sg
import sys

# import de classes
sys.path.append('../')

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

# Mostrar Objetos
# Função helper para printa as info dos obj.
def print_info(obj_type, obj_array):
  for obj in obj_array[:]:
    if type(obj) == obj_type:
      obj.print_obj()
  pass
# Monstrando os Clientes
def show_clients_view(user_controller)->None:
  user_list = user_controller.get_all_clients()
  print(user_list)
  layout = []
  Col = []
  if None in user_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for client in user_list:
    if client is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
        sg.Text(str(client.user_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Nome: ', pad=(5, 5), size=(20, 1)),
          sg.Text(str(client.name), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('CPF:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(client.cpf), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('RG:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(client.rg), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Ano de nascimento:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(client.anniversary_date), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Endereço:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(client.address), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('CEP:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(client.cep), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Email:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(client.email), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Cliente de Ouro:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(client.golden_client), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Data de registro:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(client.register_date), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
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
def show_managers_view(user_controller)->None:
  manager_list = user_controller.get_all_clients()
  print(manager_list)
  layout = []
  Col = []
  if None in manager_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for manager in manager_list:
    if manager is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
        sg.Text(str(manager.user_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Nome: ', pad=(5, 5), size=(20, 1)),
          sg.Text(str(manager.name), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('CPF:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(manager.cpf), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('RG:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(manager.rg), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Ano de nascimento:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(manager.anniversary_date), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Endereço:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(manager.address), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('CEP:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(manager.cep), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Email:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(manager.email), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Salário:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(manager.wage), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('pis:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(manager.pis), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Data de adimissão:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(manager.register_date), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Gerentes", layout, element_justification='c', resizable=True, finalize=True,
                      modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()
# FIM Mostrar Objetos
