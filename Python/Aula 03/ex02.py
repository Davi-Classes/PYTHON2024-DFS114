frutas = []

for f in range(3):
    fruta = input(f'Digite a {f + 1}ª fruta: ').capitalize()
    frutas.append(fruta)

frutas.sort()

print('Frutas: ')
for fruta in frutas:
    print(f'- {fruta}')