class NodoFila:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.qtd = 0

    def enqueue(self, musica):
        novo = NodoFila(musica)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        self.qtd += 1

    def dequeue(self):
        if self.inicio is None:
            return None
        musica = self.inicio.musica
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.qtd -= 1
        return musica