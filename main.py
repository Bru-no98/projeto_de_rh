from contratacao import Funcionario
from folha_de_pagamento import FolhaPagamento

funcionario = Funcionario('bruno', 'salva vidas', 3000)
funcionario.gerar_olerite()
funcionario.gerar_olerite()
funcionario.gerar_olerite()

FolhaPagamento.criar_arquivo_com_olerite()