from modulos.style_mdls import *


def int_print(self):
    while True:
        try:
            num = str(input(self)).strip()
            if num.isnumeric():
                num = int(num)
                return num
            else:
                print(f'{vermelho('Erro!')} {italico(num)} ← Valor inválido!')    
        except ValueError:
            print(f'{vermelho('Erro!')} {italico(num)} ← Valor inválido!')


def float_print(self):
    while True:
        try:
            num = str(input(self)).strip()
            if num.isnumeric():
                num = float(num)
                return num
            else:
                print(f'{vermelho('Erro!')} {italico(num)} ← Valor inválido!')    
        except ValueError:
            print(f'{vermelho('Erro!')} {italico(num)} ← Valor inválido!')
