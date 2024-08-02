class Animal:
    nome: str
    cor= str
    tamanho: float
    peso: float
    sexo: str

    def __init__(self, nome= None, cor= None, tamanho= None, peso= None, sexo= None):
        self.nome= nome
        self.cor= cor
        self.tamanho= tamanho
        self.peso= peso
        self.sexo= sexo

    def andar():
        print ('AÇÃO CONCLUÍDA: andando...')

    def dormir():
        print ('AÇÃO CONCLUÍDA: zzz...(Dormindo)')

    def comer():
        print ('AÇÃO CONCLUÍDA: comendo...')


class Cachorro(Animal):
    def __init__(self, raca= None):
        super().__init__(nome= None, cor= None, tamanho= None, peso= None, sexo= None)
        self.raca= raca

    def latir():
        print ('AÇÃO CONCLUÍDA: au-au')


class Humano(Animal):
    autoconhecimento: bool
    def __init__(self, autoconhecimento= None):
        super().__init__(nome= None, cor= None, tamanho= None, peso= None, sexo= None)
        self.autoconhecimento= autoconhecimento

    def pensar():
        print ('Pensando...')