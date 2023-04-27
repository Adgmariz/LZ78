#!/usr/bin/env python3
import sys
from Trie import Trie

def main():
    if(sys.argv[1] == "-c"):
        texto = open(sys.argv[2], "r").read()
    elif(sys.argv[1] == "-x"):
        print("Descomprimir")
    else:
        print("Parâmetros inválidos.")
    
    #Temp:
    trie = Trie()
    trie.adicionaCaractere('c')
main()