class FolhaPagamento():

    def __init__(self, nome, cargo, salario, data):
        self._nome = nome
        self._cargo = cargo
        self._salario = salario
        self._data = data
        self._desconto_inss = FolhaPagamento.calcular_inss(self._salario)
        self._desconto_irrf = FolhaPagamento.calcular_irrf(self._salario, self._desconto_inss)
        self._calculo_fgts = FolhaPagamento.calcular_fgts(self._salario)
        
    def __str__(self):
        return f'Folha de Pagamento de {self._nome}: \n SALÁRIO: {self._salario} | INSS: {self._desconto_inss} | IR: {self.desconto_irrf} | FGTS: {self._calculo_fgts}'
    
    @property
    def desconto_irrf(self):
        irrf_formatado = format(self._desconto_irrf, f".{2}f")
        return irrf_formatado
    
    
    @classmethod
    def calcular_inss(cls, salario):
        if salario <= 1412:
            desconto_inss = salario * 0.075
        elif salario > 1412 and salario <= 2666.68:
            desconto_inss =  salario * 0.09 - 21.18
        elif salario > 2666.68 and salario <= 4000.03:
            desconto_inss =  salario * 0.12 - 101.18
        elif salario > 4000.03 and salario <= 7786.02:
            desconto_inss =  salario * 0.14 - 101.18
        else:
            desconto_inss =  salario * 0.14 - 101.18
        return desconto_inss
    
    @classmethod
    def calcular_irrf(cls, salario, inss):
        salario_irrf = salario - inss
        if salario_irrf <= 2112:
            desconto_irrf = 0
        elif salario_irrf > 2112 and salario_irrf <= 2826.65:
            desconto_irrf = salario_irrf * 0.075 - 158.40
        elif salario_irrf > 2826.65 and salario_irrf <= 3751.05:
            desconto_irrf = salario_irrf * 0.15 - 370.40
        elif salario_irrf > 3751.05 and salario_irrf <= 4664.68:
            desconto_irrf = salario_irrf * 0.225 - 651.73
        else:
            desconto_irrf = salario_irrf * 0.275 - 884.96
        return desconto_irrf
    
    @classmethod
    def calcular_fgts(cls, salario):
        return salario * 0.08
        

