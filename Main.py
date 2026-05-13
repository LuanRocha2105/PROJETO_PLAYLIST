from biblioteca import Biblioteca
from fila import Fila

import os


def limpar_tela():
    input("Pressione qualquer tecla para continuar")
    os.system('cls' if os.name == 'nt' else 'clear')

# garantir que o bpm seja inteiro e maior que 0 
def ler_bpm():
    entrada = input("BPM: ")
    try:
        bpm = int(entrada)
    except ValueError:
        print("\nBPM invalido, precisa ser um numero inteiro.")
        return None
    if bpm <= 0:
        print("\nBPM precisa ser maior que zero.")
        return None
    return bpm

# garantir que o usuario digite um numero inteiro
def ler_int(mensagem):
    entrada = input(mensagem)
    try:
        return int(entrada)
    except ValueError:
        print("\nValor invalido! Precisa ser um numero inteiro.")
        return None

#op 1
def adicionar_musica(biblioteca):
    titulo = input("Titulo: ")
    artista = input("Artista: ")
    genero = input("Genero: ")
    bpm = ler_bpm()
    if bpm is None:
        return
    musica = biblioteca.adicionar(titulo, artista, genero, bpm)
    print(f"\nMusica adicionada com id {musica.id}.")
    limpar_tela()

#op 2 
def remover_musica(biblioteca):
    id = ler_int("\nId da musica para remover: ")
    if id is None:
        return
    if biblioteca.remover(id):
        print("\nMusica removida.")
    else:
        print("\nId nao encontrado.")
    limpar_tela()

#op 3
def buscar_musica(biblioteca):
    print("\n1 - Buscar por id")
    print("2 - Buscar por titulo")
    op = input("Escolha: ")
    if op == "1":
        id = ler_int("Id: ")
        if id is None:
            return
        musica = biblioteca.buscar_por_id(id)
    elif op == "2":
        titulo = input("Titulo: ")
        musica = biblioteca.buscar_por_titulo(titulo)
    else:
        print("\nOpcao invalida.")
        return

    if musica is None:
        print("\nMusica nao encontrada.")
    else:
        musica.mostrar()
    limpar_tela()

#op 5 
def montar_filas(biblioteca, filas):
    # limpa todas as filas antes de remontar
    for nome in filas:
        filas[nome].limpar()

    atual = biblioteca.inicio
    while atual is not None:
        m = atual.musica
        if m.bpm <= 80:
            filas["Relaxar"].enqueue(m)
        elif m.bpm <= 120:
            filas["Focar"].enqueue(m)
        elif m.bpm <= 160:
            filas["Animar"].enqueue(m)
        else:
            filas["Treinar"].enqueue(m)
        atual = atual.proximo
    print("\nFilas de humor montadas com sucesso!")
    limpar_tela()


def escolher_fila(filas):
    print("\n1 - Relaxar (ate 80 BPM)")
    print("2 - Focar (81 a 120 BPM)")
    print("3 - Animar (121 a 160 BPM)")
    print("4 - Treinar (acima de 160 BPM)")
    op = input("Escolha a fila: ")
    if op == "1":
        return "Relaxar"
    elif op == "2":
        return "Focar"
    elif op == "3":
        return "Animar"
    elif op == "4":
        return "Treinar"
    else:
        print("\nOpcao invalida.")
        limpar_tela()
        return None

#op 6
def reproduzir_proxima(filas, historico):
    nome = escolher_fila(filas)
    if nome is None:
        return
    fila = filas[nome]
    if fila.vazia():
        print(f"A fila {nome} esta vazia.")
        return
    musica = fila.dequeue()
    print(f"\nReproduzindo da fila {nome}:")
    musica.mostrar()
    historico.enqueue(musica)
    limpar_tela()

#op 7
def exibir_fila_humor(filas):
    nome = escolher_fila(filas)
    if nome is None:
        return
    print(f"\n--- Fila {nome} ---")
    filas[nome].exibir()
    limpar_tela()

#op 8
def exibir_historico(historico):
    print("\n--- Historico de reproducoes ---")
    historico.exibir()
    limpar_tela()

#op 9
def estatisticas(biblioteca, filas, historico):
    print("\n--- Estatisticas ---")
    print(f"Total na biblioteca: {biblioteca.tamanho()}")
    for nome in filas:
        print(f"Fila {nome}: {filas[nome].tamanho()}")
    print(f"Total reproduzidas: {historico.tamanho()}")
    limpar_tela()


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
    filas = {
        "Relaxar": Fila(),
        "Focar": Fila(),
        "Animar": Fila(),
        "Treinar": Fila(),
    }
    historico = Fila()

    while True:
        menu()
        op = input("Escolha: ")
        if op == "1":
            adicionar_musica(biblioteca)
        elif op == "2":
            remover_musica(biblioteca)
        elif op == "3":
            buscar_musica(biblioteca)
        elif op == "4":
            biblioteca.listar()
        elif op == "5":
            montar_filas(biblioteca, filas)
        elif op == "6":
            reproduzir_proxima(filas, historico)
        elif op == "7":
            exibir_fila_humor(filas)
        elif op == "8":
            exibir_historico(historico)
        elif op == "9":
            estatisticas(biblioteca, filas, historico)
        elif op == "10":
            print("Saindo...")
            break
        else:
            print("Opcao ainda nao implementada.")


if __name__ == "__main__":
    main()