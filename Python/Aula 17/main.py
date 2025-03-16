from professor import professor_repository

def menu():
    while True:
        print('[1] - Modulo de Materias')
        print('[2] - Modulo de Professores')
        print('[3] - Modulo de Alunos')
        print('[4] - Modulo de Turmas')
        print('[5] - Sair')

        opcao = input('Digite qual opção deseja: ')

        if opcao == '1':
            pass
        elif opcao == '2':
            pass
        elif opcao == '3':
            pass
        elif opcao == '4':
            menu_turmas()
        elif opcao == '5':
            break
        else:
            print('Opção Inválida.')

def menu_turmas():
    while True:
        print('[1] - Listar Turmas')
        print('[2] - Cadastrar Turmas')
        print('[3] - Voltar')

        opcao = input('Digite qual opção deseja: ')

        if opcao == '1':
            pass
        elif opcao == '2':
            print('Selecione um Professor: ')
            professores = professor_repository.listar()

            for id, nome, _, _, _ in professores:
                print(f'[{id}] - {nome}')

            professor_id = int(input('--> '))

            print('Selecione uma Matéria: ')
            materias = professor_repository.listar_materias(professor_id)

            for id, nome, sigla in materias:
                print(f'[{id}] - {nome} ({sigla})')
    
            materia_id = int(input('--> '))
            print(f'ProfessorId: {professor_id}')
            print(f'MateriaId: {materia_id}')
            print('Resto do Fluxo...')
        elif opcao == '3':
            break
        else:
            print('Opção Inválida.')

if __name__ == '__main__':
    menu()