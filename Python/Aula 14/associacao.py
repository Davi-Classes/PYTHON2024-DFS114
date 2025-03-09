from dataclasses import dataclass


@dataclass
class Endereco:
    cep: str
    estado: str
    cidade: str
    bairro: str
    rua: str
    numero: str
    complemento: str | None = None


@dataclass
class Pessoa:
    nome: str
    cpf: str
    endereco: Endereco


endereco1 = Endereco(
    cep='41720000',
    estado='BA',
    cidade='Salvador',
    bairro='Imbuí',
    rua='João José Rescala',
    numero='160'
)
pessoa = Pessoa('Millena', cpf='12343465700', endereco=endereco1)

print(pessoa.nome)
print(pessoa.cpf)
print(pessoa.endereco.rua)
print(pessoa.endereco.numero)
print(pessoa.endereco.cidade)
print(pessoa.endereco.estado)