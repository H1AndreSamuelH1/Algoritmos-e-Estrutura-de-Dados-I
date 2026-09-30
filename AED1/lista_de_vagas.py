class ListaVagas: 
    def __init__(self):
        self.cabeca = None
    
    def inserir_ordenado(self, Apartamento):
        Apartamento.proximo = None
        if self.cabeca is None or self.cabeca.vaga > Apartamento.vaga:
            Apartamento.proximo = self.cabeca
            self.cabeca = Apartamento

        else:
            atual = self.cabeca
            while atual.proximo is not None and atual.proximo.vaga < Apartamento.vaga:
                atual = atual.proximo
            Apartamento.proximo = atual.proximo
            atual.proximo = Apartamento
        print(f"Apartamento {Apartamento.numero} alocado na vaga {Apartamento.vaga} (com lista ordenada).")

    def excluir_por_numero(self, numero_Apartamento):
        atual = self.cabeca
        anterior = None

        while atual is not None and atual.numero != numero_Apartamento:
            anterior = atual
            atual = None

        if atual is None:
            return False
        
        if anterior is None:
            self.cabeca = atual.proximo 
        else: 
            anterior.proximo = atual.proximo

        print(f"Apartamento {numero_Apartamento} com vaga {atual.vaga} foi excluído da lista/sistema.")
        return True

    def liberar_vaga(self, numero_vaga, fila_espera):
        atual = self.cabeca
        anterior = None

        while atual is not None and atual.vaga != numero_vaga:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            print(f"Nenhum apartamento foi encontrado ocupando a vaga {numero_vaga}.")
            return
        
        if anterior is None:
            self.cabeca = atual.proximo
        else:
            anterior.proximo = atual.proximo

        print(f"Vaga {numero_vaga} liberada pelo apartamento {atual.numero}.")

        #O apartamento que liberou perde a vaga e vai para a fila de espera
        atual.vaga = 0
        fila_espera.adicionar(atual)

        #Se houver alguém na fila, o primeiro ganha a vaga recém liberada 
        if not fila_espera.esta_vazia():
            sortudo = fila_espera.retirar_inicio()
            sortudo.vaga = numero_vaga
            self.inserir_ordenado(sortudo)

    def imprimir(self):
        print("/n--- Lista de apartamentos com vaga (ordenada) ---")
        atual = self.cabeca
        if not atual:
            print("Nenhum apartamento está disponível no momento.")
            return
        while atual:
            print(f"Vaga: {atual.vaga} | Apartamento: {atual.numero} | Torre {atual.torre.nome}")
            atual = atual.proximo