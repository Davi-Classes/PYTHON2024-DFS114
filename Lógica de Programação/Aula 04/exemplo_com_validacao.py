soma = 0
for i in range(1, 6):
    while True:
        numero = input(f'Digite o {i}º numero: ')

        comparacao = numero.replace('.', '').replace('-', '')
        if comparacao.isnumeric():
            numero = float(numero)
            break

        print('Entrada inválida!')

    soma += numero
    print(soma)

print(f'A soma dos numeros digitados é: {soma}')