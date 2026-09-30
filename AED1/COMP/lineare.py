# estruturas_lineares.py

# ==========================================
# 1. FILA (FIFO - First In, First Out)
# ==========================================
class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def enfileirar(self, item):
        item.proximo = None
        if self.esta_vazia():
            self.inicio = item
            self.fim = item
        else:
            self.fim.proximo = item
            self.fim = item

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        removido = self.inicio
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        removido.proximo = None
        return removido


# ==========================================
# 2. PILHA (LIFO - Last In, First Out)
# ==========================================
class Pilha:
    def __init__(self):
        self.topo = None

    def esta_vazia(self):
        return self.topo is None

    def empilhar(self, item):
        item.proximo = self.topo
        self.topo = item

    def desempilhar(self):
        if self.esta_vazia():
            return None
        removido = self.topo
        self.topo = self.topo.proximo
        removido.proximo = None
        return removido


# ==========================================
# 3. LISTA DUPLAMENTE ENCADEADA
# ==========================================
class ListaDupla:
    def __init__(self):
        self.cabeca = None

    def inserir_inicio(self, item):
        item.proximo = self.cabeca
        item.anterior = None
        if self.cabeca is not None:
            self.cabeca.anterior = item
        self.cabeca = item

    def remover(self, numero):
        atual = self.cabeca
        while atual is not None and atual.numero != numero:
            atual = atual.proximo

        if atual is None:
            return False

        if atual.anterior is not None:
            atual.anterior.proximo = atual.proximo
        else:
            self.cabeca = atual.proximo  # Era o primeiro

        if atual.proximo is not None:
            atual.proximo.anterior = atual.anterior

        return True