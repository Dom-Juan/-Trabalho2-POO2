import pickle
import os


# Salva os arquivos em um tipo pickle do python para salvar os objetos.
def save_e_comerce_config(e_comerce) -> bool:
  if e_comerce.client_list:
    if os.path.exists('./files/e_comerce_config.pickle'):
      with open('./files/e_comerce_config.pickle', 'wb') as save_file:
        try:
          pickle.dump(e_comerce, save_file, protocol=2)
        except EOFError:
          print('Erro ao salvar arquivo...')
          return False
        finally:
          return True
    else:
      with open('./files/e_comerce_config.pickle', 'ab') as save_file:
        try:
          pickle.dump(e_comerce, save_file, protocol=2)
        except EOFError:
          print('Erro ao salvar arquivo...')
          return False
        finally:
          return True
  return False


# Salva os arquivos em um tipo pickle do python para salvar os objetos.
def save_user_controller_config(user_controller) -> bool:
  if user_controller.get_all_managers() and user_controller.get_all_clients():
    if os.path.exists('./files/user_controller.pickle'):
      with open('./files/user_controller.pickle', 'wb') as save_file:
        try:
          pickle.dump(user_controller, save_file, protocol=2)
        except EOFError:
          print('Erro ao salvar arquivo...')
          return False
        finally:
          return True
    else:
      with open('./files/user_controller.pickle', 'ab') as save_file:
        try:
          pickle.dump(user_controller, save_file, protocol=2)
        except EOFError:
          print('Erro ao salvar arquivo...')
          return False
        finally:
          return True
  return False


# Salva os arquivos em um tipo pickle do python para salvar os objetos.
def save_sale_controller_config(sale_controller) -> bool:
  if sale_controller:
    if os.path.exists('./files/sale_controller.pickle'):
      with open('./files/sale_controller.pickle', 'wb') as save_file:
        try:
          pickle.dump(sale_controller, save_file, protocol=2)
        except EOFError:
          print('Erro ao salvar arquivo...')
          return False
        finally:
          return True
    else:
      with open('./files/sale_controller.pickle', 'ab') as save_file:
        try:
          pickle.dump(sale_controller, save_file, protocol=2)
        except EOFError:
          print('Erro ao salvar arquivo...')
          return False
        finally:
          return True
  return False


# Salva os arquivos em um tipo pickle do python para salvar os objetos.
def save_product_controller_config(product_controller) -> bool:
  if product_controller:
    if os.path.exists('./files/product_controller.pickle'):
      with open('./files/product_controller.pickle', 'wb') as save_file:
        try:
          pickle.dump(product_controller, save_file, protocol=2)
        except EOFError:
          print('Erro ao salvar arquivo...')
          return False
        finally:
          return True
    else:
      with open('./files/product_controller.pickle', 'ab') as save_file:
        try:
          pickle.dump(product_controller, save_file, protocol=2)
        except EOFError:
          print('Erro ao salvar arquivo...')
          return False
        finally:
          return True
  return False


# Salva os arquivos em um tipo pickle do python para salvar os objetos.
def save_payment_controller_config(payment_controller) -> bool:
  if payment_controller.payment_list:
    if os.path.exists('./files/payment_controller.pickle'):
      with open('./files/payment_controller.pickle', 'wb') as save_file:
        try:
          pickle.dump(payment_controller, save_file, protocol=2)
        except EOFError:
          print('Erro ao salvar arquivo...')
          return False
        finally:
          return True
    else:
      with open('./files/payment_controller.pickle', 'ab') as save_file:
        try:
          pickle.dump(payment_controller, save_file, protocol=2)
        except EOFError:
          print('Erro ao salvar arquivo...')
          return False
        finally:
          return True
  return False