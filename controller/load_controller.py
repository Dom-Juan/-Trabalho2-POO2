import pickle


# Salva os arquivos em um tipo pickle do python para salvar os objetos.
def load_config():
    try:
      e_comerce: object = pickle.load(open('./files/e_comerce_config.pickle', 'rb'))
      user_controller: object = pickle.load(open('./files/user_controller.pickle', 'rb'))
      sale_controller: object = pickle.load(open('./files/sale_controller.pickle', 'rb'))
      product_controller: object = pickle.load(open('./files/product_controller.pickle', 'rb'))
      payment_controller: object = pickle.load(open('./files/payment_controller.pickle', 'rb'))
      print(e_comerce.name)
      if e_comerce is None:
        return [None, None, None, None, None]
      elif user_controller is None:
        return [None, None, None, None, None]
      elif sale_controller is None:
        return [e_comerce, user_controller, None, product_controller, payment_controller]
      elif product_controller is None:
        return [None, None, None, None, None]
      elif payment_controller is None:
        return [None, None, None, None, None]
      else:
        return [e_comerce, user_controller, sale_controller, product_controller, payment_controller]
    except EOFError:
      print('Erro ao salvar arquivo')