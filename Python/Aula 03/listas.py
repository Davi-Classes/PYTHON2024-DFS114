# Lista  
# Uma variavel que pode armazenar muitiplos valores de forma ORDENADA e INDEXADA (Começando de Zero)

#                 0         1          2          3
perifericos = ['Monitor', 'Mouse', 'Teclado', 'Headset']

print(perifericos[2]) # 'Teclado'
print(perifericos[1]) # 'Mouse'

# Adiciona um elemento na lista.
perifericos.append('Microfone') # Será adicionado ao final da lista
perifericos.insert(0, 'Mesa Digitalizadora') # Será adicionado ao indice informado (0 nesse caso), e os outros elementos serão empurrados para a direita

# Excluir um elemento de uma lista
perifericos.pop() # Remover o ultimo elemento ('Microfone')
perifericos.pop(0) # Remove o elemento do indice informado ('Mesa Digitalizadora')
