class Carga:
    def __init__(self, nome, carga, data):
        self.nome = nome
        self.carga = carga
        self.data = data

    def __str__(self):
        return self.nome + " - " + self.carga
