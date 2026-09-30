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
        self.torre = torre      # Objeto da classe Torre
        self.vaga = vaga        # Número da vaga (0 se não tiver vaga)
        self.proximo = None     # Ponteiro para o próximo Apartamento (Nó)

    def cadastrar(self):
        pass

    def imprimir(self):
        print(f"Apto: {self.numero} | Vaga: {self.vaga} | Torre: {self.torre.nome}")


# =====================================================================
# FILA DE ESPERA (Passo 2 - FIFO)
# =====================================================================

class FilaEspera:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def adicionar(self, apto):
        apto.proximo = None
        if self.esta_vazia():
            self.inicio = apto
            self.fim = apto
        else:
            self.fim.proximo = apto
            self.fim = apto
        print(f"Apartamento {apto.numero} adicionado à fila de espera de vagas.")

    def retirar_inicio(self):
        if self.esta_vazia():
            return None
        
        apto_removido = self.inicio
        self.inicio = self.inicio.proximo
        
        if self.inicio is None:
            self.fim = None
            
        apto_removido.proximo = None
        return apto_removido

    def remover_por_numero(self, numero_apto):
        atual = self.inicio
        anterior = None

        while atual is not None and atual.numero != numero_apto:
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

        print(f"Apartamento {numero_apto} excluído da fila de espera.")
        return True

    def imprimir(self):
        print("\n--- FILA DE ESPERA DE VAGAS ---")
        atual = self.inicio
        if not atual:
            print("Fila de espera vazia.")
            return
        while atual:
            print(f"Apto: {atual.numero} | Torre: {atual.torre.nome}")
            atual = atual.proximo


# =====================================================================
# LISTA ENCADEADA ORDENADA (Passo 3 - Com Vaga)
# =====================================================================

class ListaVagas:
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
        print(f"Apartamento {apto.numero} alocado na vaga {apto.vaga} (Lista Ordenada).")

    def excluir_por_numero(self, numero_apto):
        atual = self.cabeca
        anterior = None

        while atual is not None and atual.numero != numero_apto:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            return False

        if anterior is None:
            self.cabeca = atual.proximo
        else:
            anterior.proximo = atual.proximo

        print(f"Apartamento {numero_apto} com vaga {atual.vaga} foi excluído do sistema.")
        return True

    def liberar_vaga(self, numero_vaga, fila_espera):
        atual = self.cabeca
        anterior = None

        while atual is not None and atual.vaga != numero_vaga:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            print(f"Nenhum apartamento encontrado ocupando a vaga {numero_vaga}.")
            return

        if anterior is None:
            self.cabeca = atual.proximo
        else:
            anterior.proximo = atual.proximo

        print(f"Vaga {numero_vaga} liberada pelo apto {atual.numero}.")

        atual.vaga = 0
        fila_espera.adicionar(atual)

        if not fila_espera.esta_vazia():
            sortudo = fila_espera.retirar_inicio()
            sortudo.vaga = numero_vaga
            self.inserir_ordenado(sortudo)

    def imprimir(self):
        print("\n--- LISTA DE APARTAMENTOS COM VAGA (ORDENADA) ---")
        atual = self.cabeca
        if not atual:
            print("Nenhum apartamento com vaga no momento.")
            return
        while atual:
            print(f"Vaga: {atual.vaga} | Apto: {atual.numero} | Torre: {atual.torre.nome}")
            atual = atual.proximo


# =====================================================================
# MENU DE OPÇÕES (Passo 4)  MAIN
# =====================================================================

def menu():
    fila_espera = FilaEspera()
    lista_vagas = ListaVagas()
    
    torre_padrao = Torre(1, "Torre Principal", "Rua das Flores, 123")

    while True:
        print("\n==============================================")
        print("   SISTEMA DE GERENCIAMENTO DE CONDOMÍNIO")
        print("==============================================")
        print("1. Cadastrar apartamento")
        print("2. Exclusão de apartamento")
        print("3. Liberar vaga")
        print("4. Imprimir fila de apartamentos sem vaga")
        print("5. Imprimir lista de apartamentos com vaga")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                id_ap = int(input("ID do apartamento: "))
                num_ap = input("Número do apartamento (ex: 204): ")
                vaga_ap = int(input("Número da vaga (1 a 5, ou 0 se não tiver): "))

                novo_apto = Apartamento(id_ap, num_ap, torre_padrao, vaga_ap)

                if vaga_ap == 0 or vaga_ap > 5:
                    print("Sem vaga disponível ou vaga inválida. Indo para a fila de espera.")
                    fila_espera.adicionar(novo_apto)
                else:
                    lista_vagas.inserir_ordenado(novo_apto)
            except ValueError:
                print("Erro: Digite apenas números válidos.")

        elif opcao == "2":
            num_excluir = input("Digite o número do apartamento que deseja excluir: ")
            encontrou = lista_vagas.excluir_por_numero(num_excluir)
            if not encontrou:
                encontrou_fila = fila_espera.remover_por_numero(num_excluir)
                if not encontrou_fila:
                    print("Apartamento não encontrado em nenhuma das listas.")

        elif opcao == "3":
            try:
                vaga_lib = int(input("Qual o número da vaga que deseja liberar (1-5)? "))
                lista_vagas.liberar_vaga(vaga_lib, fila_espera)
            except ValueError:
                print("Erro: Digite um número de vaga válido.")

        elif opcao == "4":
            fila_espera.imprimir()

        elif opcao == "5":
            lista_vagas.imprimir()

        elif opcao == "0":
            print("Saindo do sistema... Boa prova na quarta-feira!")
            break
        else:
            print("Opção inválida! Escolha entre 0 e 5.")

if __name__ == "__main__":
    menu()