from No import No
import numpy as np
class Trie:
    def __init__(self,texto = []):
        self.raiz = No(0,'', None)
        self.index = 1
        self.texto = texto
        self.no_atual = self.raiz
        #self.comprimido = ""
        self.tokens = np.array([],dtype=np.uint32)

    def comprimir(self):
        for caractere in self.texto:
            filho = self.no_atual.getFilhoPorCaractere(caractere)
            if not filho:
                self.no_atual.adiciona_filho(self.index,caractere)
                #self.comprimido += str(self.no_atual.index) + chr(caractere)
                binario = np.zeros(1, dtype=np.uint32)
                binario[0] |= (self.no_atual.index << 8)
                binario[0] |= (caractere)
                self.tokens = np.append(self.tokens,binario[0])
                self.index += 1
                self.no_atual = self.raiz
            else:
                self.no_atual = filho