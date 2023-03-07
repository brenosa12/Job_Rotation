def seq(numero):
    if numero < 2:
        return numero
    else:
        return seq(numero-1) + seq(numero-2)


buscar = int(input('Digite um numero inteiro para ser buscado: '))
numeros = []
i = 0
while True:
    numeros.append(seq(i))
    if seq(i) >= buscar:
        break
    else:
        i += 1
        continue
if buscar in numeros:
    print(f'O número: {buscar} PERTENCE a sequência de Fibonacci.')
else:
    print(f'O número: {buscar} NÃO PERTENCE a sequência de Fibonacci.')
