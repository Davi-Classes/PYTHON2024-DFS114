from dataclasses import dataclass


# Metódo Tradicional
# class Endereco:
#     # Construtor
#     def __init__(self, cep, estado, bairro, cidade, rua, numero, complemento = None):
#         self.cep = cep
#         self.estado = estado
#         self.cidade = cidade
#         self.bairro = bairro
#         self.rua = rua 
#         self.numero = numero 
#         self.complemento = complemento 


# Com DataClasses
@dataclass
class Endereco:
    cep: str
    estado: str
    cidade: str
    bairro: str
    rua: str
    numero: str
    complemento: str | None = None

endereco1 = Endereco(
    cep='41720000',
    estado='BA',
    cidade='Salvador',
    bairro='Imbuí',
    rua='João José Rescala',
    numero='160'
)
print(endereco1)