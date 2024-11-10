pessoas = []

for p in range(1, 6):
    pessoa = {}

    pessoa['nome'] = input(f'Digite o nome da {p}º pessoa: ')
    pessoa['idade'] = int(input(f'Digite a idade da {p}º pessoa: '))
    pessoa['altura'] = float(input(f'Digite a altura da {p}º pessoa: '))

    pessoas.append(pessoa)

print(' Pessoas '.center(30, '-'))
for pessoa in pessoas:
    print(f'Nome: {pessoa.get("nome")}')
    print(f'Idade: {pessoa.get("idade")}')
    print(f'Altura: {pessoa.get("altura")}')
    print('-' * 30)