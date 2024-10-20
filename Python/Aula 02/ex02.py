animal = {} 

animal['nome'] = input('Digite o nome do animal: ')
animal['raca'] = input('Digite a raça do animal: ')
animal['cor'] = input('Digite a cor do animal: ')

print('Dados do Animal: ')
print(f'- Nome: {animal.get('nome')}')
print(f'- Raça: {animal.get('raca')} ({animal['cor']})')