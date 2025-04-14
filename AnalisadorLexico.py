from setup import SM, simbolos, token_type

class AnalisadorLexico:
    def __init__ (self):
        self.reset()

    def reset(self):
        self.STATE = SM.IDENTIFICAR
        self.data = ""
        self.pointer = 0
        self.char = ""
        self.lexema = ""
        self.expr = []
        self.expr_list = []
        self.EOF = False


    def valida_char(self, validacao):
        if validacao(self.char):
            self.lexema += self.char
            # if not self.EOF:
            self.pointer += 1
        else:
            if self.STATE in simbolos.keys():
                if self.lexema in simbolos[self.STATE]:
                    self.expr.append((self.lexema, token_type[self.STATE]))
                    self.STATE = SM.IDENTIFICAR
                else:
                    self.STATE = SM.SIMBOLOILEGAL
                    self.expr.append((self.lexema, token_type[self.STATE]))
            else:
                self.expr.append((self.lexema, token_type[self.STATE]))
                self.STATE = SM.IDENTIFICAR
            self.lexema = ""

    def valida_constante(self, char):
        return self.char.islower()

    def valida_proposicao(self, char):
        if self.lexema == "" and self.char.isnumeric():
            return 1
        else:
            return self.char.isalnum()

    def valida_operador(self, char):
        global STATE
        if self.lexema == "" and self.char == "\\":
            return 1
        elif self.char.islower():
            return 1
        else:
            if self.lexema in simbolos[SM.OPERATORUNARIO]:
                self.STATE = SM.OPERATORUNARIO
            else:
                self.STATE = SM.OPERATORBINARIO
            return 0

    def valida_paren(self, char):
        if self.lexema == "":
            return 1
        else:
            return 0


    def get_expr_num(self):
        string = ""

        while self.data[self.pointer] != "\n":
            string += self.char
            self.pointer += 1

        if string.isnumeric():
            self.expr_num = int(string)
            return 1
        else:
            return 0

    def identificacao(self):
        if self.char == " ":
            self.pointer += 1
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
        elif (self.char == "\n") or (self.char == "$"):
            self.STATE = SM.FIMEXPR



    def analise_lexicar(self, data):
        self.reset()
        self.data = data

        if self.get_expr_num():
            return 0

        while self.pointer <= len(self.data):
            if self.pointer < len(self.data):
                self.char = self.data[self.pointer]
            else:
                self.char = "\n"

            if (self.pointer == len(self.data)-1) and (self.EOF != True):
                self.EOF = True

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
                self.pointer += 1

            elif self.STATE == SM.SIMBOLOILEGAL:
                if self.char == "\n":
                    self.expr_list.append([("invalid", token_type[self.STATE])])
                    self.STATE = SM.IDENTIFICAR
                self.pointer += 1

        return self.expr_list