inicio = int(input('Digite o começo da contagem: '))
final = int(input('Digite o final da contagem: '))
passo = int(input('Digite o passo da contagem: '))

ajuste = +1 if inicio < final else -1

if (passo > 0 and inicio > final) or (passo < 0 and inicio < final):
    passo = -passo

for numero in range(inicio, final + ajuste, passo):
    print(numero, end=' ')

# \n quebra a linha
print('\nFim da Contagem.')