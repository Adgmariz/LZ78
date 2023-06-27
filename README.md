# Instruções de execução:
- Abra um terminal e navegue até o diretório onde o arquivo main.py está localizado.
- Torne o arquivo executável com o seguinte comando: 'chmod +x main.py' (Linux ou macOS)
- Execute o programa de acordo com a especificação:
    - Compressão:
	./main.py -c <arquivo_entrada> [-o <arquivo_saida>]
    - Descompressão:
    ./main.py -x <arquivo_entrada> [-o <arquivo_saida>]

*Uma alternativa para executar o programa no Windows é utilizando o comando 'py main.py', usando os parâmetros no formato acima.



# Especificação:
UNIVERSIDADE FEDERAL DE MINAS GERAIS
Instituto de Ciências Exatas
Departamento de Ciência da Computação

DCC207 -- Algoritmos 2
Prof. Renato Vimieiro

Trabalho Prático 1 -- Manipulação de sequências

Objetivos
---------

Nesse trabalho serão abordados os aspectos práticos de manipulação de
sequências. Especificamente, serão explorados aspectos de implementação
de árvores de prefixo aplicada ao problema de compressão de arquivos.

O objetivo secundário é fixar o conteúdo. Entende-se que ao implementar a 
estrutura o aluno conseguirá compreender melhor os conceitos explorados.
Dessa forma, o conteúdo teórico será melhor absorvido e fixado. Além disso,
os alunos terão a oportunidade de ver conceitos não abordados na disciplina,
no caso específico, um método de compressão de arquivos.

Tarefas
-------

Os alunos deverão implementar um algoritmo para resolver o problema
de comprimir arquivos texto através do método LZ78. Esse método é baseado
em dicionários e, basicamente, substitui strings que se repetem no texto por
códigos. Como o algoritmo executa muitas buscas e inserções nesse dicionário,
é comum utilizar árvores de prefixo na sua implementação. O LZ78, apesar de simples,
é a base de vários algoritmos implementados nas ferramentas de compressão utilizadas
atualmente. A seguir é apresentada uma breve descrição do algoritmo.

O LZ78 foi proposto por Lempel e Ziv em 1978. Como dito, a ideia do algoritmo
é substituir strings que se repetem no texto por um código, diminuindo assim o
número de bytes gravados na saída. O dicionário é inicializado com a string vazia
associada ao código 0. Então, o texto é processado da esquerda para a direita,
caracter a caracter. Uma string 'padrão' é mantida para verificar se essa substring
já ocorreu anteriormente no texto. Se o padrão acrescido do próximo caracter lido
ocorrer no dicionário, então mais um símbolo é lido e o ciclo se repete. Caso contrário,
o par (código_padrão; caracter) deve ser emitido na saída, e a sequência padrão + caracter
deve ser inserida no dicionário com um novo código. O ciclo se repete até que todo
o arquivo tenha sido processado. A descompressão do arquivo segue o mesmo algoritmo.
O dicionário é inicializado com a string vazia associada ao código 0. Sempre que um
par (código_padrão, caracter) for lido, o padrão associado ao código deve ser emitido
na saída, e um novo código deve ser associado à sequência padrão + caracter. O ciclo
se repete até que todo o arquivo tenha sido processado. Veja um exemplo na Wikipedia
https://pt.wikipedia.org/wiki/LZ78#Exemplo. Como forma de melhorar a compressão, o número
de bytes usados na representação dos códigos pode ser ajustada conforme a necessidade.
Em outras palavras, pode-se realizar uma primeira passada no arquivo, executando o processo
de compressão como acima, calcula-se a quantidade de códigos gerados, e, então, realiza-se
a segunda passada emitindo códigos com o número de bytes ajustados. Nesse caso, é necessário
gravar também o número de códigos no início do arquivo comprimido para garantir que a
leitura dos bytes referentes aos códigos seja conforme a representação usada.

Deve-se construir um programa que implemente a compressão e descompressão de
arquivos, usando o algoritmo LZ78. O dicionário deve ser implementado através de
uma árvore trie compacta. As implementações deverão ser feitas em Python 3.6+, 
podendo usar NumPy como biblioteca de suporte para estrutura de dados básicas e tipos de dados. 
Alternativamente, serão admitidas implementações em C/C++ compiláveis com GCC. 
Nesse caso, o aluno também deverá incluir um arquivo Makefile para geração do executável.

O programa deve funcionar na linha de comando, tendo a seguinte sintaxe:

- Compressão
	
	./<programa> -c <arquivo_entrada> [-o <arquivo_saida>]

- Descompressão

	./<programa> -x <arquivo_entrada> [-o <arquivo_saida>]

A especificação do arquivo de saída é opcional. Caso ela não seja dada, o nome
do arquivo de saída para compressão deve ser o nome original do arquivo acrescido
da extensão z78. No caso da descompressão, será o nome do arquivo original, suprimida
a extensão atual e acrescentada a extensão .txt. Por exemplo:

- Compressão
	./<programa> -c teste.txt >>>>> resulta em >>>>> teste.z78 

- Descompressão
	./<programa> -c teste.z78 >>>>> resulta em >>>>> teste.txt
	
O uso de bibliotecas adicionais deve ser discutido com o professor.

O que entregar?
---------------

Devem ser entregues todos os arquivos fonte usados na implementação. Deve ser
entregue também um relatório explicando sua implementação, assim como a taxa
de compressão para, no mínimo, 10 exemplos. Os casos de teste devem ser arquivos
texto reais, com tamanho mínimo de 1KB e máximo de 2MB. Os exemplos também devem
ser entregues. OS ARQUIVOS NAO DEVEM SER COMPRIMIDOS EM HIPOTESE ALGUMA. Cada arquivo
deve ser anexado individualmente. Na entrega, um repositório no GitHub deverá ser
criado e o todos os arquivos da entrega deverão ser depositados lá. Dessa forma,
a entrega no Teams deverá ser somente o link de acesso ao repositório.

Política de Plágio
------------------

Os alunos podem, e devem, discutir soluções sempre que necessário. Dito isso,
há uma diferença bem grande entre implementação de soluções similares e cópia
integral de ideias. Trabalhos copiados na íntegra ou em partes de outros alunos
e/ou da internet serão prontamente anulados. Caso hajam dois trabalhos copiados
por alunos diferentes, ambos serão anulados.

AVISO ESPECIAL PARA CODIGOS COPIADOS/ALTERADOS DE SITES DA INTERNET. A maior parte
desses sites é de conhecimento do professor/monitores. Os trabalhos que contenham
trechos ou cópias integrais dos algoritmos propostos para serem implementados nessa
atividade SERÃO TOTALMENTE ANULADOS.

Datas
-----

Entrega Teams: 09/05/2023 às 23h59


Política de atraso
------------------

Haverá tolerância de 30min na entrega dos trabalhos. Submissões feitas depois
do intervalo de tolerância serão penalizados. 
- Atraso de 1 dia: 30%
- Atraso de 2 dias: 70%
- Atraso de 3+ dias: não aceito

Serão considerados atrasos de 1 dia aqueles feitos após as 0h30 do dia de entrega.
A partir daí serão contados o número de dias passados da data de entrega.


Referências
------------------

- https://pt.wikipedia.org/wiki/LZ78
- David Salomon. Data Compression: The complete reference. 4th edition. Springer
