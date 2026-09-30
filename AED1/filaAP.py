class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None
    
    def adicionar(self, Apartamento):
        Apartamento.proximo = None
        if self.esta_vazia():
            self.inicio = Apartamento
            self.fim = Apartamento
        
        else:
            self.fim.proximo = Apartamento
            self.fim = Apartamento
        print(f"Apartamento {Apartamento.numero} foi adicionado á fila de espera.")

    def retirar_inicio(self):
        if self.esta_vazia():
            return None
        
        Apartamento_removido = self.inicio
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        Apartamento_removido.proximo = None
        return Apartamento_removido
    
    def remover_pelo_numero(self, numero_apartamento):
        atual = self.inicio
        anterior = None

        while atual is not None and atual.numero != numero_apartamento:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            return False 
        
        if anterior is None:
            self.inicio = atual.proximo
            if self.inicio is None: 
                self.fim = None 

        else: 
            anterior.proximo = atual.proximo
            if atual == self.fim:
                self.fim = anterior 

        print(f"Apartamento {numero_apartamento} retirado da fila de espera.")
        return True
    
    def imprimir (self):
        print("\n--- Fila de espera de vagas ---")
        atual = self.inicio 
        if not atual: 
            print("Fila de espera vazia.")
            return 
        while atual:
            print(f"Apartamento {atual.numero} | Torre: {atual.torre.nome}")
            atual = atual.proximo
