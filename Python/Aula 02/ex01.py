frutas = []

for _ in range(5):
    fruta = input('Digite uma fruta: ')
    frutas.append(fruta.capitalize())

frutas = list(set(frutas))

print('Frutas Inseridas: ')
for fruta in frutas:
    print(f'- {fruta}')