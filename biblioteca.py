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
        if self.existe(titulo, artista):
            return None

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
    
    #op 4
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
    
    def buscar_por_titulo(self, titulo):
        atual = self.inicio
        while atual is not None:
            if atual.musica.titulo.lower() == titulo.lower():
                return atual.musica
            atual = atual.proximo
        return None
    
    def existe(self, titulo, artista):
        atual = self.inicio
        while atual is not None:
            if (atual.musica.titulo.lower() == titulo.lower() and
                atual.musica.artista.lower() == artista.lower()):
                return True
            atual = atual.proximo
        return False
    
    def remover(self, id):
        if self.inicio is None:
            return False

        if self.inicio.musica.id == id:
            self.inicio = self.inicio.proximo
            return True

        anterior = self.inicio
        atual = self.inicio.proximo
        while atual is not None:
            if atual.musica.id == id:
                anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False
    
    def tamanho(self):
        cont = 0
        atual = self.inicio
        while atual is not None:
            cont += 1
            atual = atual.proximo
        return cont