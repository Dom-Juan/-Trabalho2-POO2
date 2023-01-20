
# ############################################################### #
# Classe para operações lógicas não específicas de modelo,        #
# ajudando em lógicas de negócio e derivados.                     #
# ############################################################### #

import PySimpleGUI as sg  # Interface.


# Converte STR para boolean
def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")


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