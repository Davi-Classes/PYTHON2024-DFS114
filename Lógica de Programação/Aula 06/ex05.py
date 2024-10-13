print('Calculador de Rendimento da Turma')
qtd_alunos = int(input('Quantos alunos a turma têm? -> '))

soma_medias = 0
melhor_aluno = ''
media_melhor_aluno = None
pior_aluno = ''
media_pior_aluno = None

for n in range(qtd_alunos):
    nome = input(f'Digite o nome do {n + 1}º aluno: ')

    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    
    media = (nota1 + nota2) / 2

    soma_medias += media

    if media_melhor_aluno is None or media > media_melhor_aluno:
        melhor_aluno = nome
        media_melhor_aluno = media

    if media_pior_aluno is None or media < media_pior_aluno:
        pior_aluno = nome
        media_pior_aluno = media


media_turma = soma_medias / qtd_alunos


print(f'Média da Turma: {media_turma:.2f}')
print(f'Melhor Aluno: {melhor_aluno} ({media_melhor_aluno:.2f})')
print(f'Pior Aluno: {pior_aluno} ({media_pior_aluno:.2f})')