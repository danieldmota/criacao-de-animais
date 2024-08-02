from classes import *
from views import *
from funcoes import *

def fluxo_principal():
    while True:
        menu_principal()
        op_principal= int(input('Escolha uma opção: '))

        if op_principal == 1:
            criar_cachorro()

        elif op_principal == 2:
            criar_humano()

        elif op_principal == 3:
            while True:
                listar_cachorro()
                op= int (input('Escolha algum cachorro, ou feche este menu digitando 99: '))
                if op == 99:
                    break
                else:
                    while True:
                        menu_cao()
                        op_acao= int(input(f'Escolha uma ação para fazer com o cachorro selecionado: '))
                        if op_acao == 99:
                            break
                        elif op_acao == 1:
                            Cachorro.andar()
                        elif op_acao == 2:
                            Cachorro.dormir()
                        elif op_acao == 3:
                            Cachorro.comer()
                        elif op_acao == 4:
                            Cachorro.latir()
                        else:
                            print ('Opção INVÁLIDA')

        elif op_principal == 4:
            listar_humanos()

        elif op_principal == 99:
            break

        else:
            print ('Opção INVÁLIDA')

fluxo_principal()