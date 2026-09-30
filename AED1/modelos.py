class Torre:
    def __init__(self, id_torre, nome, enedereco):
        self.id = id_torre
        self.nome = nome
        self.endereco = self.endereco

    def cadastro_torre(self):
        pass

    def imprimir(self):
        print(f"Torre: {self.nome} | Endereco: {self.endereco}")


class Apartamento: 
    def __init__(self, id_apartamento, numero, torre, vaga):
        self.id = id_apartamento
        self.numero = numero
        self.torre = torre #pertence a classe torre 
        self.vaga = vaga #aqui é o numero da vaga (0 (zerada) se não houver nenhuma)
        self.proximo = None #através dele aponta para o proximo apartamento

    def cadastro_apartamento(self):
        pass

    def imprimir(self):
        print(f"Apartamento {self.numero} | Vaga: {self.vaga} | Torre: {self.torre.nome}")
        
