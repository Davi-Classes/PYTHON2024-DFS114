qtd_vendas = 0
faturamento = 0

while True:
    resposta = input('Deseja registrar uma venda? [S/N] -> ')

    if resposta.upper() not in ('S', 'N'):
        print('Opção Inválida, digite "S" ou "N".')
        continue

    if resposta.upper() == 'N':
        break
        
    venda = float(input('Qual foi o valor da venda? -> ').replace(',', '.'))

    qtd_vendas += 1
    faturamento += venda

faturamento_formatado = f'R${str(round(faturamento, 2)).replace('.', ',')}'
print(f'Faturamento de Hoje: {faturamento_formatado}')
print(f'Quantidade de Vendas: {qtd_vendas}')