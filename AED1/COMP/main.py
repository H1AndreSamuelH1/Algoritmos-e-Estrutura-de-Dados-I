from modelos import Torre, Apartamento
from lineare import Fila, Pilha, ListaDupla
from listar_vagas import ListaVagasOrdenada

def menu():
    fila_espera = Fila()
    lista_vagas = ListaVagasOrdenada()
    torre_padrao = Torre(1, "Torre Principal", "Rua Central, 100")

    while True:
        print("\n========================================")
        print("   SISTEMA DO CONDOMÍNIO (AED I)")
        print("========================================")
        print("1. Cadastrar apartamento (Fila / Vaga)")
        print("2. Liberar vaga de garagem")
        print("3. Imprimir fila de espera")
        print("4. Imprimir lista de vagas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                id_ap = int(input("ID: "))
                num_ap = input("Número do Apto: ")
                vaga_ap = int(input("Vaga (1 a 5, ou 0 se sem vaga): "))

                novo_apto = Apartamento(id_ap, num_ap, torre_padrao, vaga_ap)

                if vaga_ap == 0 or vaga_ap > 5:
                    print("Sem vaga. Indo para a Fila de Espera.")
                    fila_espera.enfileirar(novo_apto)
                else:
                    lista_vagas.inserir_ordenado(novo_apto)
            except ValueError:
                print("Valor inválido!")

        elif opcao == "2":
            try:
                vaga_lib = int(input("Qual vaga deseja liberar (1-5)? "))
                lista_vagas.liberar_vaga(vaga_lib, fila_espera)
            except ValueError:
                print("Valor inválido!")

        elif opcao == "3":
            print("\n--- FILA DE ESPERA ---")
            atual = fila_espera.inicio
            if not atual:
                print("Fila vazia.")
            while atual:
                print(f"Apto: {atual.numero}")
                atual = atual.proximo

        elif opcao == "4":
            lista_vagas.imprimir()

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()