#!/usr/bin/env python3
import sys
from Trie import Trie
from No import No

def main():
    if(sys.argv[1] == "-c"):
        texto = open(sys.argv[2], "r").read()
    elif(sys.argv[1] == "-x"):
        print("Descomprimir")
    else:
        print("Parâmetros inválidos.")
    
    #Temp:

    trie = Trie(texto)
    trie.comprimir()
    #print(trie.comprimido)
    #with open('saida.txt', 'w') as saida:
        #saida.write(trie.comprimido)
    trie.descomprimir()
main()