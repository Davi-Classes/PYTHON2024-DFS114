class Conta:
    # Construtor
    def __init__(self, titular: str, saldo: float = 0):
        # Atributos
        self.titular = titular
        self.saldo = saldo

    # Metódos
    def sacar(self, valor: float):
        if valor > self.saldo:
            raise Exception('Não é possivel sacar mais do que há na conta.')
        
        self.saldo -= valor

    def render(self) -> float:
        return 0


# Herança: Conta Investimento irá herdar os metódos e atributos de conta
class ContaInvestimento(Conta):
    # Polimorfismo no metódo render, para modificar o seu comportamento em relação ao seu pai.
    def render(self):
        total = self.saldo * 0.03
        self.saldo += total
        return total
    

c1 = Conta('Fernanda', 600)
c2 = ContaInvestimento('Fernanda', 600)

# A conta não rende nada
c1.render()
print(c1.saldo)

# Já a conta investimento teve um rendimento de 3% definido no seu proprio metódo
print(c2.saldo)
c2.render()
print(c2.saldo)