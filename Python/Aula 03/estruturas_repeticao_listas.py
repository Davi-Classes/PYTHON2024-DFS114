alunos = []
medias = []

# While
resp = '' # Variavel de Controle
while resp != 'N':
    aluno = input('Digite o nome do aluno: ')

    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))

    media = (nota1 + nota2 + nota3) / 3

    alunos.append(aluno)
    medias.append(media)

    resp = input('Deseja continuar? [S/N] -> ')

# For
print(' Alunos '.center(30, '='))
for i in range(len(alunos)):
    print(f'Nome: {alunos[i]}')
    print(f'Média: {medias[i]}')
    print('=' * 30)

# print(' Alunos '.center(30, '='))
# for aluno, media in zip(alunos, medias):
#     print(f'Nome: {aluno}')
#     print(f'Média: {media}')
#     print('=' * 30)