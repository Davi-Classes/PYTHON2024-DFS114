from datetime import datetime, UTC
from dataclasses import dataclass


@dataclass
class Item:
    nome: str
    categoria: str
    preco_unitario: float
    quantidade: int = 1


class Pedido:
    def __init__(self, numero: str, itens: list[Item] = [], data_hora: datetime = datetime.now()):
        self.numero = numero
        self.itens = itens
        self.data_hora = data_hora
        self.calcular_total()
    
    def calcular_total(self):
        total = 0

        for item in self.itens:
            total += item.quantidade * item.preco_unitario
        
        self.total = total
    
    def adicionar_item(self, item: Item):
        adicionado = False

        for item_adicionado in self.itens:
            if item.nome == item_adicionado.nome:
                item_adicionado.quantidade += item.quantidade
                adicionado = True
                break
        
        if not adicionado:
            self.itens.append(item)
        
        self.calcular_total()

itens = [
    Item('Batata', 'Vegetais', 0.5, 10),
    Item('Celular', 'Eletrônico', 900, 1),
]

pedido = Pedido('123543', itens)

print('Adicionando Batata...')
pedido.adicionar_item(Item('Batata', 'Vegetal', 0.5, 1000))
print(pedido.total)
print(pedido.itens)

print('Adicionando Notebook...')
pedido.adicionar_item(Item('Notebook', 'Eletrônico', 2000, 1))
print(pedido.total)
print(pedido.itens)