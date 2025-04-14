from AnalisadorLexico import AnalisadorLexico
from setup import *

from sys import argv
from time import sleep

def print_expressoes_analisadas(expressoes_analisadas):
    for expr in expressoes_analisadas:
        string = ""
        for token in expr:
            string += token[0]+" "
        print(string)

def print_expressoes_analisadas_tokens(expressoes_analisadas):
    for expr in expressoes_analisadas:
        for token in expr:
            print(token)
        print("--------------------")

data = open(argv[1])
read_data = data.read()
data.close()

with open(argv[1]) as f:
    string = ""
    while char := f.read(1):
        if char != "\n":
            string += char
        else:
            print(string)
            string = ""

# analisador_lexico = AnalisadorLexico()
# expressoes_analisadas = analisador_lexico.analise_lexicar(read_data)

# python main.py .\test-files\test-1.txt