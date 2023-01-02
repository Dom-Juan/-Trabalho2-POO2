# -*- coding: utf-8 -*-
# import de interface
from models.comerce.e_comerce import EComerce
from views.main_view import main_window


def main():
  e_comerce_obj = EComerce(
    name='Atacado da Tristeza UNESP',
    sales_list=[],
    product_list=[],
    manufacturer_list=[],
    shipping_company_list=[],
    client_list=[],
    manager_list=[],
    config=None
  )
  main_window('Trabalho 2 de POO 2', e_comerce_obj)

if __name__ == '__main__':
  main()
