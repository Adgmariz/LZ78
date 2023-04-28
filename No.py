class No:
    def __init__(self, index, caractere, pai):
        self.index = index
        self.caractere = caractere
        self.filhos = []
        self.pai = pai
    def adiciona_filho(self, index, caractere):
        filho = No(index,caractere,self)
        self.filhos.append(filho)
    def getFilhoPorCaractere(self, caractere):
        for filho in self.filhos:
            if filho.caractere == caractere:
                return filho
        return False