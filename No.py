class No:
    def __init__(self, index, caractere, pai):
        self.index = index
        self.caractere = caractere
        self.filhos = []
        self.pai = pai
    def adiciona_filho(self, index, caractere, pai):
        filho = No(index,caractere,pai)
        self.filhos.append(filho)
    def getFilhoPorCaractere(self, caractere_):
        for filho in self.filhos:
            if filho.caractere == caractere_:
                return filho
        return False