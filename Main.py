from biblioteca import Biblioteca


def menu():
    print("\n===== Sistema de Playlist =====")
    print("1 - Adicionar musica na biblioteca")
    print("2 - Remover musica da biblioteca")
    print("3 - Buscar musica")
    print("4 - Listar biblioteca completa")
    print("5 - Montar fila de reproducao por humor")
    print("6 - Reproduzir proxima")
    print("7 - Exibir fila de humor")
    print("8 - Exibir historico")
    print("9 - Estatisticas")
    print("10 - Sair")


def main():
    biblioteca = Biblioteca()

    while True:
        menu()
        op = input("Escolha: ")
        if op == "10":
            print("Saindo...")
            break
        else:
            print("Opcao ainda nao implementada.")


if __name__ == "__main__":
    main()