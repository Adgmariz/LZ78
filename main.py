#!/usr/bin/env python3
import sys
import numpy as np
from Trie import Trie
from No import No

def main():
    if(sys.argv[1] == "-c"):
        entrada = open(sys.argv[2], "rb").read()
        trie = Trie(entrada)
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

    elif(sys.argv[1] == "-x"):
        nome_saida = ""
        if len(sys.argv) == 5:
            if sys.arg[3] == "-o":
                nome_saida = sys.argv[4].rstrip(".z78") + ".txt"
            else:
                print("Parâmetros inválidos")
        else:
            nome_saida = sys.argv[2].rstrip(".z78") + ".txt"
        indices = []
        caracteres = []
        indices.append(0)
        caracteres.append(0)
        with open(sys.argv[2], "rb") as arquivo:
            while True:
                token = arquivo.read(4)
                if len(token) == 0:
                    break
                if len(token) < 4:
                    print("ERRO BINÁRIO, len:"+str(len(token)))
                    print(token)
                    print("-")
                caractere = token[0]
                index = (token[3] << 16) | (token[2] << 8) | (token[1])
                indices.append(index)
                caracteres.append(caractere)
        nome_saida = "saida.txt"
        with open(nome_saida, "wb") as arquivo:
            for i in range(1,len(indices)):
                if indices[i] == 0:
                    arquivo.write(caracteres[i].to_bytes(1))
                else:
                    pilha_sequencia = []
                    aux = i
                    while indices[aux] != 0:
                        pilha_sequencia.append(aux)
                        aux = indices[aux]
                    pilha_sequencia.append(aux)
                    while len(pilha_sequencia) > 0:
                        j = pilha_sequencia.pop()
                        arquivo.write(caracteres[j].to_bytes(1))

    else:
        print("Parâmetros inválidos.")
    
    #Temp:

    #trie = Trie(texto)
    #trie.comprimir()
    #trie.descomprimir()
main()