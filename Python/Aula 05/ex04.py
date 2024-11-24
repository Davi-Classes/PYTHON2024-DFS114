def menu():
    print('=== Calculadora ===')
    print('[1] - Somar')
    print('[2] - Subtrair')
    print('[3] - Multiplicar')
    print('[4] - Dividir')
    print('===================')

    while True:
        opcao = input('Digite uma opção: ')

        if opcao in ('1', '2', '3', '4'):
            break
        
        print('Opção Inválida! Digite novamente!')

    return opcao


def calculadora(n1: float, n2: float, operacao: str) -> float | None:
    if operacao == '1':
        return n1 + n2
    elif operacao == '2':
        return n1 - n2
    elif operacao == '3':
        return n1 * n2
    elif operacao == '4':
        if n2 == 0:
            return None
        
        return n1 / n2


opcao = menu()

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

resultado = calculadora(num1, num2, opcao)

if resultado is not None:
    print(f'Resultado: {resultado}')
else:
    print('Operação Inválida. Não é possivel dividir um numero por 0.')
