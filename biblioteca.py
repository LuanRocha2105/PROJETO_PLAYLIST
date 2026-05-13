from musica import Musica


class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Biblioteca:
    def __init__(self):
        self.inicio = None
        self.proximo_id = 1

    def adicionar(self, titulo, artista, genero, bpm):
        nova_musica = Musica(self.proximo_id, titulo, artista, genero, bpm)
        self.proximo_id += 1
        novo_nodo = NodoLista(nova_musica)

        if self.inicio is None:
            self.inicio = novo_nodo
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo
        return nova_musica
    
    def listar(self):
        if self.inicio is None:
            print("Biblioteca vazia.")
            return
        atual = self.inicio
        while atual is not None:
            atual.musica.mostrar()
            atual = atual.proximo

    def buscar_por_id(self, id):
        atual = self.inicio
        while atual is not None:
            if atual.musica.id == id:
                return atual.musica
            atual = atual.proximo
        return None