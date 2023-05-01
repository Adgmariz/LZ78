#!/usr/bin/env python3
import sys
import numpy as np
from Trie import Trie
from No import No

def main():
    if(sys.argv[1] == "-c"):
        texto = open(sys.argv[2], "r").read()
        trie = Trie(texto)
        trie.comprimir()
        nome_saida = ""
        if len(sys.argv) == 5:
            if sys.arg[3] == "-o":
                nome_saida = sys.argv[4].rstrip(".txt") + ".z78"
            else:
                print("Parâmetros inválidos")
        else:
            nome_saida = sys.argv[2].rstrip(".txt") + ".z78"
        with open(nome_saida, "wb") as arquivo:
            for token in trie.tokens:
                arquivo.write(token)
                print(token)

    elif(sys.argv[1] == "-x"):
        trie = Trie()
        with open(sys.argv[2], "rb") as arquivo:
            while True:
                token = arquivo.read(3)
                if len(token) == 0:
                    break
                if len(token) < 3:
                    print("ERRO BINÁRIO, len:"+str(len(token)))
                    print(token)
                    print("-")
                trie.tokens = np.append(trie.tokens,token)
        descomprimido = trie.descomprimir()
        print(descomprimido)
    else:
        print("Parâmetros inválidos.")
    
    #Temp:

    #trie = Trie(texto)
    #trie.comprimir()
    #trie.descomprimir()
main()