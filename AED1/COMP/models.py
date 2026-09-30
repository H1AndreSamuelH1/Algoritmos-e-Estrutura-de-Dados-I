class Torre:
    def __init__(self, id_torre, nome, endereco):
        self.id = id_torre
        self.nome = nome
        self.endereco = endereco

    def cadastrar(self):
        pass

    def imprimir(self):
        print(f"Torre: {self.nome} | Endereço: {self.endereco}")


class Apartamento:
    def __init__(self, id_apto, numero, torre, vaga):
        self.id = id_apto
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None  # Usado em listas simples e filas
        self.anterior = None # Usado caso precise de lista duplamente encadeada

    def imprimir(self):
        print(f"Apto: {self.numero} | Vaga: {self.vaga} | Torre: {self.torre.nome}")