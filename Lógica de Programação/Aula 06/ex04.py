numero_inicio = int(input('Digite o numero inicial: '))
numero_fim = int(input('Digite o numero final: '))

for n in range(numero_inicio, numero_fim + 1):
    if n % 2 == 1:
        print(n, end=' ')