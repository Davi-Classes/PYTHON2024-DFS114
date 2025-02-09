from banco_infinity.banco import Banco
from banco_infinity.view import BancoView


my_bank = Banco()
bank_view = BancoView(my_bank)
bank_view.run()