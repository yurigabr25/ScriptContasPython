# Programa para fins de aprendizado e ainda em processo de construção.
# Ainda é necessário implementar o mecânismo de registro e de cálculo de das contas adicionadas no programa.
# Sendo desenvolvido por Yuri Gabriel.

# Área de importação de bibliotécas:
from asyncio import to_thread
from glob import glob
from random import random
from tkinter import N
from unittest.mock import mock_open

# Área de declaração de variáveis:
global todas_as_contas

# Área de funções:
def adicionar_contas():
    conta = input(str("Qual conta você quer adicionar? "))
    conta_valor = float(input(f"Qual o valor de {conta}? R$ "))
    mconta = input("Quer adicionar mais contas? ")
    for m in mconta:
        if mconta == 'n':
            print("O total das suas contas é de ...")
        else:
            while mconta == 's':
                outra_conta_nome = input("Qual conta?")
                outra_conta_valor = float(input(f"Qual o valor de {outra_conta_nome}? R$ "))
                str(outra_conta_valor)
                contas_total = float(conta_valor + outra_conta_valor)
                print(f"{outra_conta_nome} foi adicionado(a) a lista.")
                mconta = input("Quer adicionar mais contas? ")
                if mconta == 's':
                    adicionar_contas()
                    return
                else:
                    print(f"O total das suas contas é de R$ {contas_total}.")
                    break

# Fluxo do código:
adicionar_contas()

input("Tecle ENTER para sair...")