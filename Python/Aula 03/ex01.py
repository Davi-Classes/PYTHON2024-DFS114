numeros = []

for n in range(5):
    numero = int(input('Digite um numero: '))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)

print(f'Soma: {soma}')
print(f'Média: {media}')
