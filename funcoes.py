from classes import *

cachorros= []
humanos=[]

def criar_cachorro():
    nome= input('Digite um nome: ')
    cor= input('Digite uma cor: ')
    tamanho= input('Digite um tamanho em cm: ')
    peso= input('Digite um peso em kg: ')
    sexo= input('Digite um sexo: ')
    raca= input ('Digite a raça: ')
    animal= Animal (nome,cor,tamanho,peso,sexo)
    cachorro= Cachorro(raca)
    cachorro_list= (f'nome: {animal.nome}\ncor: {animal.cor}\ntamanho: {animal.tamanho}cm\npeso: {animal.peso}kg\nsexo: {animal.sexo}\nraça: {cachorro.raca}\n')
    cachorros.append(cachorro_list)

def listar_cachorro():
    print ('LISTA DE CACHORROS JÁ CRIADOS JÁ CRIADOS:')
    for cachorro in cachorros:
            print (cachorro)

def criar_humano():
    nome= input('Digite um nome: ')
    cor= input('Digite uma cor: ')
    tamanho= input('Digite um tamanho: ')
    peso= input('Digite um peso: ')
    sexo= input('Digite um sexo: ')
    autoconhecimento= True
    animal= Animal (nome,cor,tamanho,peso,sexo)
    humano= Humano (autoconhecimento)
    humano_list= (f'nome: {animal.nome}\ncor: {animal.cor}\ntamanho: {animal.tamanho}cm\npeso: {animal.peso}kg\nsexo: {animal.sexo}\nraça: {humano.autoconhecimento}\n')
    humanos.append(humano_list)

def listar_humanos():
    print ('LISTA DE HUMANOS JÁ CRIADOS:')
    for humano in humanos:
        print (humano)