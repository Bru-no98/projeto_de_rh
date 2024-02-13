from folha_de_pagamento import FolhaPagamento

class Funcionario:

    funcionarios = []
    def __init__(self, nome, cargo, salario):
        self._nome = nome
        self._cargo = cargo
        self._salario = salario
        self._ativo = True
        self._olerites = []
    
    def __str__(self):
        return f'{self._nome.ljust(25)} | {self._cargo.ljust(25)} | {str(self._salario).ljust(25)}'
    
    def gerar_olerite(self):
        olerite = FolhaPagamento(self._nome, self._cargo, self._salario)
        self._olerites.append(olerite)

    def printar_olerites(self):
        for item in self._olerites:
            print(item)

    
    

    
