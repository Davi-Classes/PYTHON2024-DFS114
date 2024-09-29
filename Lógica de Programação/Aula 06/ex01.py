import math

raio = float(input('Digite o raio da circuferência: ').replace(',', '.'))

area = math.pi * (raio ** 2)
perimetro = 2 * math.pi * raio

print(f'A area da circuferência é: {area:.2f}')
print(f'O perimetro da circuferência é: {perimetro:.2f}')