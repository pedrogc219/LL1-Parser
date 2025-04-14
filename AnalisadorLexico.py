from setup import SM, simbolos, token_type

class AnalisadorLexico:
    def __init__ (self):
        self.STATE = SM.IDENTIFICAR
        self.data = ""
        self.pointer = 0
        self.char = ""
        self.lexema = ""
        self.expr = []
        self.expr_list = []
        self.expr_num = []
        self.EOF = False


    def valida_char(self, validacao):
        if validacao():
            self.lexema += self.char
            self.char = self.f.read(1)
        else:
            self.valida_lexema()
            

    def valida_lexema(self):
        if self.STATE == SM.OPERATOR:
            if self.lexema in simbolos[SM.OPERATORUNARIO]:
                self.STATE = SM.OPERATORUNARIO
            else:
                self.STATE = SM.OPERATORBINARIO

        if self.STATE in simbolos.keys():
            if self.lexema not in simbolos[self.STATE]:
                self.STATE = SM.SIMBOLOILEGAL

        self.expr.append((self.lexema, token_type[self.STATE]))
        self.lexema = ""
        if self.STATE != SM.SIMBOLOILEGAL:
            self.STATE = SM.IDENTIFICAR


    def valida_constante(self):
        return self.char.islower()

    def valida_proposicao(self):
        if self.lexema == "" and self.char.isnumeric():
            return 1
        else:
            return self.char.isalnum()

    def valida_operador(self):
        if self.lexema == "" and self.char == "\\":
            return 1
        elif self.char.islower():
            return 1
        else:
            return 0

    def valida_paren(self):
        return self.lexema == ""


    def get_expr_num(self):
        string = ""
        while (char := self.f.read(1)) != "\n":
            string += char

        if string.isnumeric():
            self.expr_num = int(string)
            self.char = self.f.read(1) # para não começar o loop em "\n"
            return 1
        else:
            return 0

    def identificacao(self):
        if self.char == " ":
            self.char = self.f.read(1)
        elif self.char.islower():
            self.STATE = SM.CONSTANTE
        elif self.char.isnumeric():
            self.STATE = SM.PROPOSICAO
        elif self.char == "\\":
            self.STATE = SM.OPERATOR
        elif self.char == "(":
            self.STATE = SM.ABREPAREN
        elif self.char == ")":
            self.STATE = SM.FECHAPAREN
        elif (self.char == "\n") or (self.char == ""):
            self.STATE = SM.FIMEXPR



    def analise_lexica(self, file):
        with open(file) as self.f:

            # termina se primeira linha for invalida
            if not self.get_expr_num():
                return "Primeira linha não é invalida"

            while len(self.expr_list) < self.expr_num:

                if self.STATE == SM.IDENTIFICAR:
                    self.identificacao()

                if self.STATE == SM.CONSTANTE:
                    self.valida_char(self.valida_constante)
                elif self.STATE == SM.PROPOSICAO:
                    self.valida_char(self.valida_proposicao)
                elif self.STATE == SM.OPERATOR:
                    self.valida_char(self.valida_operador)
                elif (self.STATE == SM.ABREPAREN) or (self.STATE == SM.FECHAPAREN):
                    self.valida_char(self.valida_paren)

                elif self.STATE == SM.FIMEXPR:
                    self.STATE = SM.IDENTIFICAR
                    self.expr_list.append(self.expr)
                    self.expr = []
                    self.char = self.f.read(1)

                elif self.STATE == SM.SIMBOLOILEGAL:
                    if (self.char == "\n") or (self.char == ""):
                        self.expr_list.append([("invalido", token_type[self.STATE])])
                        self.expr = []
                        self.STATE = SM.IDENTIFICAR
                    self.char = self.f.read(1)

            return self.expr_list