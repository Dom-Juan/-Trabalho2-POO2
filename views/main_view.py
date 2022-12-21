import PySimpleGUI as sg  # Interface.
import sys  # Sistema.
import pyglet  # Helper para ajudar nos arquivos.
import ctypes  # Tipos da linguagem C.
import platform  # Biblioteca de paltaforma.

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


# Janela principal.
def main_window(name, real_state_company_name):
    if int(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    # Instanciando a imobiliária
    user_list: list = list()
    property_list: list = list()
    insurance_list: list = list()
    payment_list: list = list()
    rental_list: list = list()
    sale_list: list = list()
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
                        '&Usuários',
                        [
                            'Criar Cliente',
                            'Criar Corretor',
                            'Mostrar todos Clientes',
                            'Mostrar todos Corretores',
                            'Salvar arquivo usuários',
                            'Carregar arquivo usuários'
                        ],
                    ],
                    [
                        '&Imóveis',
                        [
                            'Criar Apartamento',
                            'Criar Casa',
                            'Criar Comercio',
                            'Mostrar todos as Casas',
                            'Mostrar todos os Apartamentos',
                            'Mostrar todos os Comércios',
                            'Salvar arquivo imoveis',
                            'Carregar arquivo imoveis'
                        ]
                    ],
                    [
                        '&Seguro',
                        [
                            'Criar Seguro',
                            'Mostrar Seguros',
                            'Salvar arquivo do seguro',
                            'Carregar arquivo do seguro'
                        ]
                    ],
                    [
                        '&Métodos de Pagamentos',
                        [
                            'Criar Pagamento Dinheiro',
                            'Criar Pagamento Cartão',
                            'Mostrar todos pagamentos',
                            'Mostrar todos pagamentos com Dinheiro',
                            'Mostrar todos pagamentos com Cartão',
                            'Salvar arquivo pagamento',
                            'Carregar arquivo pagamento'
                        ]
                    ],
                    [
                        '&Alugéis',
                        [
                            'Criar Aluguel',
                            'Mostrar Alugueis',
                            'Mostrar imóveis alugados por cliente',
                            'Mostrar imóveis alugados',
                            'Salvar arquivo aluguel',
                            'Carregar arquivo aluguel'
                        ]
                    ],
                    [
                        '&Vendas',
                        [
                            'Criar Venda',
                            'Mostrar Vendas',
                            'Mostrar as vendas em um mês e seu lucro',
                            'Mostrar imóveis vendidos',
                            'Mostrar imóveis não vendidos',
                            'Mostrar todas as vendas realizadas e o lucro total',
                            'Salvar arquivo de vendas',
                            'Carregar arquivo de vendas'
                        ]
                    ],
                    [
                        '&Imobiliária',
                        [
                            'Salvar arquivo da imobiliaria'
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
    obj: object = None
    while True:
        event, values = window.read()
        layout2.append([sg.Text('Resultado'), values])

        print(event)

        if event in [sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Sair']:
            break
        # Lógica de criação dos objetos.
        obj = None
    window.close()
