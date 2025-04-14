pilha = ["FORMULA", "$"]
buffer = []

for expr in expressoes_analisadas:
    buffer_expr = ["prop" if token[1] == "PROPOSICAO" else token[0] for token in expr]
    buffer.append(buffer_expr)

for x in buffer:
    print(x)