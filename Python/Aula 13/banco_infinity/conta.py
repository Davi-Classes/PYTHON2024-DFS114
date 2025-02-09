# Ex03. Crie uma classe "Conta" que deve conter as propriedades:

# - titular
# - numero
# - saldo (Será opcional e não pode ser negativo, se não for passado receberá 0)

# A conta terá os seguintes metódos:
# "depositar(valor)"
# "sacar(valor)"
# "transferir(valor, conta_destino)"

# Lembre-se que ao sacar, o valor de saque não pode ser maior que o saldo atual da conta.
from uuid import uuid4


class Conta:
    def __init__(self, titular: str, saldo: float = 0):
        self.numero = str(uuid4())[:6]
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de depósito deve ser positivo.')
        
        self.saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser positivo.')
        
        if valor > self.saldo:
            raise ValueError('O valor de saque não pode ser maior que o saldo da conta.')

        self.saldo -= valor

    def transferir(self, valor: float, conta: 'Conta'):
        self.sacar(valor)
        conta.depositar(valor)

    def info(self):
        print('========= INFOS =========')
        print(f'Titular: {self.titular}')
        print(f'Numero: {self.numero}')
        print(f'Saldo: R$ {self.saldo}')

    def __str__(self):
        return f'<Conta - {self.titular} (R${self.saldo})>'
