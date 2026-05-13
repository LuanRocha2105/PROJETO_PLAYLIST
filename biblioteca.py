from musica import Musica


class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Biblioteca:
    def __init__(self):
        self.inicio = None
        self.proximo_id = 1