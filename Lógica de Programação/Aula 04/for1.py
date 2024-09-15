# For
# O for funciona percorrendo sequencias, e para cada valor daquela sequencia ele executa um bloco de código

# O range gera uma sequencia numerica dado que você passa: Inicio, Fim e Passo (respectivamente)
for variavel in range(0, 10, 2):
    print(variavel, end=' ')

print('\nFim da contagem')

# Somente a Repetição
# Quando o começo é 0, o valor do final é a quantidade de repetições
for _ in range(3):
    print('Olá')


# Percorrer uma Palavra
palavra = 'Spring Boot'
for caractere in palavra:
    print(caractere)