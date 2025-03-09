from datetime import date, datetime
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    cpf: str
    data_nascimento: date

    def calcular_idade(self) -> int:
        hoje = date.today()
        delta = hoje - self.data_nascimento
        idade = delta.days // 365
        return idade


nome = input('Digite um nome para a pessoa: ')
cpf = input('Digite o cpf para a pessoa: ')

# data_nascimento = date(1294, 10, 15)
data_nascimento = input('Digite a data de nascimento (dd/MM/YYYY)')
data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()

pessoa = Pessoa(nome, cpf, data_nascimento)
print(f'A {pessoa.nome} tem {pessoa.calcular_idade()} anos.')
