from random import randint
from modulos.style_mdls import *
from modulos.int_mdls import *

def cpf_print(self):
    while True:
        try:
            texto = str(input(self)).strip().replace('.', '').replace('-', '')
            if texto.isnumeric():
                if len(texto) != 11:
                    print(f'{vermelho('Erro!')} {italico(texto)} ← Não corresponde ao CPF!')
                else:
                    return texto
            else:
                print(f'{vermelho('Erro!')} {italico(texto)} ← Não corresponde ao CPF!')
        except:
            print(f'{vermelho('Erro!')} {italico(texto)} ← Não corresponde ao CPF!')

def ValidarCPF(self):
    while True:
        cpf_digitado = cpf_print(self)

        nove_dg = cpf_digitado[:9]
        m1 = 10
        s1 = dg1 = 0
        for i in nove_dg:
            s1 += int(i) * m1
            m1 -= 1
        dg1 = (s1 * 10) % 11
        dg1 if dg1 <= 9 else 0

        dez_dg = nove_dg + str(dg1)
        m2 = 11
        s2 = dg2 = 0
        for i in dez_dg:
            s2 += int(i) * m2
            m2 -= 1
        dg2 = (s2 * 10) % 11
        dg2 if dg2 <=9  else 0

        c1 = str(dg1) + str(dg2)
        c2 = cpf_digitado[9:]
        VouF = True if c1 == c2 else False
        if VouF:
            return f"{cpf_digitado[0]}{cpf_digitado[1]}{cpf_digitado[2]}.{cpf_digitado[3]}{cpf_digitado[4]}{cpf_digitado[5]}.{cpf_digitado[6]}{cpf_digitado[7]}{cpf_digitado[8]}-{cpf_digitado[9]}{cpf_digitado[10]}"
        else:
            print(vermelho(italico('CPF Inválido')))


def GerarCPF():
    # Gera os primeiros nove dígitos do CPF
    cpf = [randint(0, 9) for _ in range(9)]
    
    # Calcula o primeiro dígito verificador
    sum_digit = sum([cpf[i] * (10 - i) for i in range(9)])
    first_digit = (sum_digit * 10) % 11
    first_digit = 0 if first_digit == 10 else first_digit
    
    # Adiciona o primeiro dígito verificador ao CPF
    cpf.append(first_digit)
    
    # Calcula o segundo dígito verificador
    sum_digit = sum([cpf[i] * (11 - i) for i in range(10)])
    second_digit = (sum_digit * 10) % 11
    second_digit = 0 if second_digit == 10 else second_digit
    
    # Adiciona o segundo dígito verificador ao CPF
    cpf.append(second_digit)
    
    return ''.join(map(str, cpf))

def GerarVariosCPFs():
    num = int_print('Quantos CPFs deseja gerar?: ')
    cpfs = [GerarCPF() for _ in range(num)]
    return print(*cpfs, sep='\n')

