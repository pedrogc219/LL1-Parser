from setup import tabela_producao
from time import sleep

class LL1parser:
    def __init__(self):
        self.pilha = []
        self.buffer = []

    def fill_buffer(self, expr):
        self.buffer = []
        for token in expr:
            if token[1] == "PROPOSICAO":
                self.buffer.append("prop")
            else:
                self.buffer.append(token[0])
        self.buffer.append("$")
        
    def LL1_parse(self, expr):
        self.pilha = ["FORMULA", "$"]
        self.fill_buffer(expr)

        while (self.buffer[0] != "$") or (self.pilha[0] != "$"):
            topo_pilha = self.pilha[0]
            topo_buffer = self.buffer[0]
            if topo_pilha == topo_buffer:
                self.pilha.pop(0)
                self.buffer.pop(0)
            else:
                if topo_buffer in tabela_producao[topo_pilha].keys():
                    producao = tabela_producao[topo_pilha][topo_buffer]
                    self.pilha.pop(0)
                    for simbolo in producao[::-1]:
                        self.pilha.insert(0, simbolo)
                else:
                    return 0

        return 1

