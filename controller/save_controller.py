import pickle
import os


# Função criada para evitar repetições grandes na função de código.
def save_logic(e_comerce, user_controller, sale_controller, product_controller, payment_controller, save_file):
  print('DEBUG: save_logic')
  pickle.dump(e_comerce, save_file, protocol=2)
  pickle.dump(user_controller, save_file, protocol=2)
  pickle.dump(sale_controller, save_file, protocol=2)
  pickle.dump(product_controller, save_file, protocol=2)
  pickle.dump(payment_controller, save_file, protocol=2)
  return True


# Salva os arquivos em um tipo pickle do python para salvar os objetos.
def save_config(e_comerce, user_controller, sale_controller, product_controller, payment_controller):
  if os.path.exists('./files/save_config.pickle'):
    with open('./files/save_config.pickle', 'wb') as save_file:
      try:
        save_logic(e_comerce, user_controller, sale_controller, product_controller, payment_controller, save_file)
      except EOFError:
        print('Erro ao salvar arquivo...')
      finally:
        return 'Sucesso ao salvar os dados.'
  else:
    with open('./files/save_config.pickle', 'ab') as save_file:
      try:
        save_logic(e_comerce, user_controller, sale_controller, product_controller, payment_controller, save_file)
      except EOFError:
        print('Erro ao salvar arquivo...')
      finally:
        return 'Sucesso ao salvar os dados.'
