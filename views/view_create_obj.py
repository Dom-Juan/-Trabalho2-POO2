import PySimpleGUI as sg
import sys

sys.path.append('..\\')

from datetime import datetime

# import de controllers
from controller.user_controller import UserController


# Converte STR para boolean
def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")


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
        return user_controller.new_user_manager(
          name = values[0],
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


# Criar Cartão de crédito
def create_payment_money_view(payment_controller):
  pass


def create_payment_pix_view(payment_controller):
  pass


def create_payment_credit_card_view(payment_controller):
  pass
# FIM DA LÓGICA DE CRIAÇÃO DE OBJETOS.