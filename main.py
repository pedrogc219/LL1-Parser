import requests
from time import sleep
from io import StringIO
from AnalisadorLexico import AnalisadorLexico
from setup import *


data = open("test_file_2.txt")
read_data = data.read()
data.close()

analisador_lexico = AnalisadorLexico()
expressoes_analisadas = analisador_lexico.analise_lexicar(read_data)



# expressions from data
for expr in read_data.split("\n"):
    print(expr)

# expressions resulted from lexical analyzer
for expr in expressoes_analisadas:
    string = ""
    for token in expr:
        string += token[0]+" "
    print(string)

# tokens from lexical analyzer
for expr in expressoes_analisadas:
    for token in expr:
        print(token)
    print("--------------------")


pilha = ["FORMULA", "$"]
buffer = []

for expr in expressoes_analisadas:
    buffer_expr = ["prop" if token[1] == "PROPOSICAO" else token[0] for token in expr]
    buffer.append(buffer_expr)

for x in buffer:
    print(x)