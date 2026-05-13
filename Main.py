from biblioteca import Biblioteca


def adicionar_musica(biblioteca):
    titulo = input("Titulo: ")
    artista = input("Artista: ")
    genero = input("Genero: ")
    bpm = int(input("BPM: "))
    musica = biblioteca.adicionar(titulo, artista, genero, bpm)
    print(f"Musica adicionada com id {musica.id}.")

def buscar_musica(biblioteca):
    print("1 - Buscar por id")
    print("2 - Buscar por titulo")
    op = input("Escolha: ")
    if op == "1":
        id = int(input("Id: "))
        musica = biblioteca.buscar_por_id(id)
    elif op == "2":
        titulo = input("Titulo: ")
        musica = biblioteca.buscar_por_titulo(titulo)
    else:
        print("Opcao invalida.")
        return

    if musica is None:
        print("Musica nao encontrada.")
    else:
        musica.mostrar()


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
        if op == "1":
            adicionar_musica(biblioteca)
        elif op == "4":
            biblioteca.listar()
        elif op == "10":
            print("Saindo...")
            break
        else:
            print("Opcao ainda nao implementada.")


if __name__ == "__main__":
    main()