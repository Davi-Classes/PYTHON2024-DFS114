# Solução 1
def verificar_primo(numero: int) -> bool:
    qtd_divisores = 0

    for n in range(1, numero + 1):
        if numero % n == 0:
            qtd_divisores += 1

    return qtd_divisores == 2

# Solução 2
# def verificar_primo(numero: int) -> bool:
#     for n in range(2, numero):
#         if numero % n == 0:
#             return False
    
#     return True


numero = int(input('Digite um numero: '))

if verificar_primo(numero):
    print('O numero é primo.')
else:
    print('O numero não é primo.')