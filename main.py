# -*- coding: utf-8 -*-
# import de interface
from views.main_view import main_window
from models.comerce.e_comerce import EComerce

def main():
  e_comerce_obj = EComerce()
  main_window('Trabalho 2 de POO 2', e_comerce_obj)

if __name__ == '__main__':
  main()
