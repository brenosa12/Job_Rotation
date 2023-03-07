import json

with open('f:\Projetos_Git\Job_Rotation\dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

total = 0
valores = []
for dado in dados:
    total += dado['valor']
    if dado['valor'] == 0:
        continue

    valores.append(int(dado['valor']))
valores.sort()
media = total / 21
dias = 0
for valor in valores:
    if valor > media:
        dias += 1

print(
    f'O menor valor de faturamento ocorrido em um dia do mês: R$ {valores[0]}.')
print(
    f'O maior valor de faturamento ocorrido em um dia do mês: R$ {valores[20]}.')
print(
    f'Em {dias} dias se obteve umvalor de faturamento diário foi superior à média mensal.')
