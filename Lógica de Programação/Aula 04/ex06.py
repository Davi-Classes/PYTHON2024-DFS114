soma_notas = 0

aluno = input('Digite o nome do aluno: ')
qtd_notas = int(input('Quantas notas deseja inserir? '))

for n in range(1, qtd_notas + 1):
    nota = float(input(f'Digite a {n}ª nota: ').replace(',', '.'))
    soma_notas += nota

media = soma_notas / qtd_notas

print(f'A média do aluno {aluno} é {media:.2f}')