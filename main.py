from contratacao import Funcionario
from datetime import datetime

funcionario = Funcionario('bruno', 'salva vidas', 3000)
funcionario.gerar_olerite(datetime.now())

funcionario.printar_olerites()

