from modulos.int_mdls import *
from modulos.str_mdls import *
from modulos.style_mdls import *


def menu_principal():
    menu = [
        "Novo Cadastro",
        "Exibir Cadastros",
        "Encerrar Sistema",
    ]
    titulo("MENU PRINCIPAL")
    for i, v in enumerate(menu):
        print(f"{i + 1} → {verde(v.upper())}")
