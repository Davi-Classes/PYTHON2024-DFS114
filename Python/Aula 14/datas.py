from datetime import date

# posicional
data_nascimento = date(1980, 2, 15)
# ou nomeado
# data_nascimento2 = date(year=1980, month=2, day=15)

# Hoje
hoje = date.today()
delta = hoje - data_nascimento
idade = delta.days // 365