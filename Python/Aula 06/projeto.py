import os # Importar o Modulo
import random as rd # Importar o Modulo com um Apelido
from tabulate import tabulate


clientes = []


def menu():
    print('========= Loja de Doces =========')
    print('[1] - Listar Vendas')
    print('[2] - Registrar Nova Venda')
    print('[3] - Encerrar')
    print('=================================')

    while True:
        option = input('Selecione uma opção -> ')

        if option in ('1', '2', '3'):
            break

        print('Opção inválida, digite novamente.')
    
    return option

def listar_clientes():
    if len(clientes) == 0:
        print('Não há clientes cadatrados')
    else:
        columns = clientes[0].keys()
        data = []
        for cliente in clientes:
            data.append(cliente.values())
        
        tabela = tabulate(data, headers=columns)
        print(tabela)

def registrar_cliente():
    cliente = {}

    cliente['nome'] = input('Digite o nome do cliente: ')
    cliente['telefone'] = input('Digite o telefone do cliente: ')
    cliente['endereco'] = input('Digite o endereco do cliente: ')

    return cliente

def sortear() -> dict | None:
    if len(clientes) == 0:
        return None

    return rd.choice(clientes)

# Código principal.
def main():
    while True:
        os.system('cls')
        opcao = menu()

        match opcao:
            case '1':
                listar_clientes()
            case '2':
                cliente = registrar_cliente()
                clientes.append(cliente)
            case '3':
                cliente = sortear()

                if cliente is not None:
                    print(f'O cliente sorteado foi {cliente.get("nome")}')
                    print(f'Telefone: {cliente.get("telefone")}')
                    print(f'Endereço: {cliente.get("")}')
                else:
                    print('Não foram realizadas vendas hoje.')

                break
        
        print()
        input('Aperte <ENTER> para continuar...')

    print('Fim do Programa')


if __name__ == '__main__':
    main()
