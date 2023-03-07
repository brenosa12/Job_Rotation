string = input('Digite uma frase: ')
strig_invertida = ''
for let in range(len(string) - 1, -1, -1):
    strig_invertida += string[let]
print(strig_invertida)
