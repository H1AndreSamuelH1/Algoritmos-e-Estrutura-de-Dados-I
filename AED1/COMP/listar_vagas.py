# lista_vagas.py

class ListaVagasOrdenada:
    def __init__(self):
        self.cabeca = None

    def inserir_ordenado(self, apto):
        apto.proximo = None
        if self.cabeca is None or self.cabeca.vaga > apto.vaga:
            apto.proximo = self.cabeca
            self.cabeca = apto
        else:
            atual = self.cabeca
            while atual.proximo is not None and atual.proximo.vaga < apto.vaga:
                atual = atual.proximo
            apto.proximo = atual.proximo
            atual.proximo = apto

    def liberar_vaga(self, numero_vaga, fila_espera):
        atual = self.cabeca
        anterior = None

        while atual is not None and atual.vaga != numero_vaga:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            print(f"Vaga {numero_vaga} não encontrada.")
            return

        if anterior is None:
            self.cabeca = atual.proximo
        else:
            anterior.proximo = atual.proximo

        print(f"Vaga {numero_vaga} liberada pelo apto {atual.numero}.")
        
        # O apto perde a vaga e vai para a fila de espera
        atual.vaga = 0
        fila_espera.enfileirar(atual)

        # Se houver alguém na fila, o primeiro ganha a vaga
        if not fila_espera.esta_vazia():
            sortudo = fila_espera.desenfileirar()
            sortudo.vaga = numero_vaga
            self.inserir_ordenado(sortudo)

    def imprimir(self):
        print("\n--- LISTA DE APARTAMENTOS COM VAGA ---")
        atual = self.cabeca
        if not atual:
            print("Vazio.")
            return
        while atual:
            print(f"Vaga: {atual.vaga} | Apto: {atual.numero}")
            atual = atual.proximo