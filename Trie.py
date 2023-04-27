from No import No
class Trie:
    def __init__(self):
        self.raiz = No(0,'', None)
        self.index = 1

    def adicionaCaractere(self,caractere):
        #Procurar local de inserção(pai do nó a ser inserido):
        no_atual = self.raiz
        while no_atual:
            local = no_atual
            no_atual = no_atual.getFilhoPorCaractere(caractere)
        local.adiciona_filho(self.index, caractere, local)
        self.index += 1