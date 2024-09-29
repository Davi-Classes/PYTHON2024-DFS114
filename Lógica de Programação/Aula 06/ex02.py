print('Calculadora')
print('[1] - Somar')
print('[2] - Subtrair')
print('[3] - Multiplicar')
print('[4] - Dividir')

opcao = input('Insira uma opção: ')

if opcao == '1':
    n1 = float(input('Digite o 1º numero: '))
    n2 = float(input('Digite o 2º numero: '))

    resultado = n1 + n2
    print(f'{n1} + {n2} = {resultado}')
elif opcao == '2':
    n1 = float(input('Digite o 1º numero: '))
    n2 = float(input('Digite o 2º numero: '))

    resultado = n1 - n2
    print(f'{n1} - {n2} = {resultado}')
elif opcao == '3':
    n1 = float(input('Digite o 1º numero: '))
    n2 = float(input('Digite o 2º numero: '))

    resultado = n1 * n2
    print(f'{n1} x {n2} = {resultado}')
elif opcao == '4':
    n1 = float(input('Digite o 1º numero: '))
    n2 = float(input('Digite o 2º numero: '))

    if n2 != 0:
        resultado = n1 / n2
        print(f'{n1} / {n2} = {resultado}')
    else:
        print('Você não pode dividir por 0.')
else:
    print('Opção Inválida!')