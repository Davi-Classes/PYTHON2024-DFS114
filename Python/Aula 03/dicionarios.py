# Dicionários
# Os dicionários são estruturas compostas por items, 
# e cada item é composto por chave e valor

# Uma chave é como se fosse uma variavel dentro 
# do dicionário, onde você pode armazenar valores

aluno = {
    'nome': 'Gabriel',
    'notas': [8, 9, 6],
}

# Acessar um valor de uma chave
print(aluno.get('nome')) # 'Gabriel'
print(aluno.get('notas')) # [8, 9, 6]
print(aluno.get('nao_existe')) # None

print(aluno['nome']) # 'Gabriel'
print(aluno['nao_existe']) # KeyError

# Criar ou Atualizar uma chave.
# Cria a chave 'media'
aluno['media'] = sum(aluno.get('notas')) / len(aluno.get('notas')) 

# Atualiza a chave nome.
aluno['nome'] = 'Gabriel Souto'