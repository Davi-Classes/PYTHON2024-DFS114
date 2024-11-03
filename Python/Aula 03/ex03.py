faixas_etarias = {
    "criança": "Você é uma criança!", # Menor que 14
    "adolescente": "Você é um adolescente!", # Entre 14 e 18
    "adulto": "Você é um adulto!",  # Maior que 18
    "idoso": "Você é um idoso!" # Maior que 65
}

# Entrada
idade = int(input('Digite a sua idade: '))

# Processamento
if idade < 14:
    faixa = 'criança'
elif idade >= 14 and idade < 18:
    faixa = 'adolescente'
elif idade >= 18 and idade < 65:
    faixa = 'adulto'
else:
    faixa = 'idoso'

# Saída
mensagem = faixas_etarias.get(faixa)
print(mensagem)
