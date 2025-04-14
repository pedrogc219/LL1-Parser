from enum import Enum

class SM(Enum):
    IDENTIFICAR = 0
    CONSTANTE = 1
    PROPOSICAO = 2
    ABREPAREN = 3
    FECHAPAREN = 4
    OPERATOR = 5
    OPERATORUNARIO = 6
    OPERATORBINARIO = 7
    FIMEXPR = 8
    SIMBOLOILEGAL = 9

simbolos = {
    SM.CONSTANTE : ["true", "false"],
    SM.OPERATORUNARIO : "\\neg",
    SM.OPERATORBINARIO : ["\\wedge", "\\vee", "\\rightarrow", "\\leftrightarrow"]
}
token_type = {
    SM.CONSTANTE : "CONSTANTE",
    SM.PROPOSICAO : "PROPOSICAO",
    SM.OPERATORUNARIO : "OPERATORUNARIO",
    SM.OPERATORBINARIO : "OPERATORBINARIO",
    SM.ABREPAREN : "ABREPAREN",
    SM.FECHAPAREN : "FECHAPAREN",
    SM.SIMBOLOILEGAL : "SIMBOLOILEGAL"
}


tabela_producao = {
    "FORMULA" : {
        "true" : ["CONSTANTE"],
        "false" : ["CONSTANTE"],
        "prop" : ["PROPOSICAO"],
        "(" : ["ABREPAREN", "FORMULAINDEFINIDA", "FECHAPAREN"]
    },
    "CONSTANTE" : {
        "true" : ["true"],
        "false" : ["false"],
    },
    "PROPOSICAO" : {
        "prop" : ["prop"],
    },
    "FORMULAINDEFINIDA" : {
        "\\neg" : ["OPERATORUNARIO", "FORMULA"],
        "\\wedge" : ["OPERATORBINARIO", "FORMULA", "FORMULA"],
        "\\vee" : ["OPERATORBINARIO", "FORMULA", "FORMULA"],
        "\\rightarrow" : ["OPERATORBINARIO", "FORMULA", "FORMULA"],
        "\\leftrightarrow" : ["OPERATORBINARIO", "FORMULA", "FORMULA"],
    },
    "ABREPAREN" : {
        "(" : ["("]
    },
    "FECHAPAREN" : {
        ")" : [")"]
    },
    "OPERATORUNARIO" : {
        "\\neg" : ["\\neg"]
    },
    "OPERATORBINARIO" : {
        "\\wedge" : ["\\wedge"],
        "\\vee" : ["\\vee"],
        "\\rightarrow" : ["\\rightarrow"],
        "\\leftrightarrow" : ["\\leftrightarrow"],
    }
}