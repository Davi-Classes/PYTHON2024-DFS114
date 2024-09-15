vogais = 'AEIOUÃÁÀÉ'
qtd_vogais = 0
frase = input('Digite uma frase: ')

for letra in frase:
    if letra.upper() in vogais:
        qtd_vogais += 1
        
    # if letra == 'a' or letra == 'e' or letra == 'o' or letra == 'i' or letra == 'u':
    #     qtd_vogais += 1

print(f'A quantidade de vogais é: {qtd_vogais}')