from AnalisadorLexico import AnalisadorLexico
from LL1parser import LL1parser
from setup import *

from sys import argv

# imprime cada expressao em uma linha
def print_expressoes_analisadas(expressoes_analisadas):
    for expr in expressoes_analisadas:
        string = ""
        for token in expr:
            string += token[0]+" "
        print(string)

# para cada expressao imprime um [{$lexema}, {$classe}] em cada linha
# expressões sao separadas por "-------------" 
def print_expressoes_analisadas_tokens(expressoes_analisadas):
    for expr in expressoes_analisadas:
        for token in expr:
            print(token)
        print("--------------------")


analisador_lexico = AnalisadorLexico()
expressoes_analisadas = analisador_lexico.analise_lexica(argv[1])

print_expressoes_analisadas(expressoes_analisadas)
print("---------------")


LL1_parser = LL1parser()
for expressao in expressoes_analisadas:
    if LL1_parser.LL1_parse(expressao):
        print("valido")
    else:
        print("invalido")


# python main.py .\test-files\test-1.txt