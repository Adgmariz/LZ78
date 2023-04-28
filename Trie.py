from No import No
class Trie:
    def __init__(self,texto = ""):
        self.raiz = No(0,'', None)
        self.index = 1
        self.texto = texto
        self.no_atual = self.raiz
        self.dicionario = {0:"0"}

    def comprimir(self):
        for caractere in self.texto:
            filho = self.no_atual.getFilhoPorCaractere(caractere)
            if not filho:
                self.no_atual.adiciona_filho(self.index,caractere)
                self.dicionario[self.index] = str(self.no_atual.index) + caractere
                self.index += 1
                self.no_atual = self.raiz
            else:
                self.no_atual = filho