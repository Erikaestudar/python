entrada = input().split()

transacoes_unicas = []

for transacao in entrada:
    if transacao not in transacoes_unicas:
        transacoes_unicas.append(transacao)

print(" ".join(transacoes_unicas))