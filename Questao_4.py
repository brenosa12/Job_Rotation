sp = 6783643
rj = 3667866
mg = 2922988
es = 2716548
outros = 1984953

total = sp+rj + mg + es + outros


def percentual(estado, total=total):
    return round((estado/total) * 100, 1)


final = 100 / (total)
sp_novo = final
print(f'O Percentual de Representação do estado:  SP = {percentual(sp)}%.')
print(f'O Percentual de Representação do estado: RJ = {percentual(rj)}%.')
print(f'O Percentual de Representação do estado: MG = {percentual(mg)}%.')
print(f'O Percentual de Representação do estado: ES = {percentual(es)}%.')
print(
    f'O Percentual de Representação do estado: Outros = {percentual(outros)}%.')
