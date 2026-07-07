class carteira:
    def __init__(self, moeda, valor):
        self.moeda = moeda # 'USD', 'BRL', 'CNY'
        self.valor = valor

    def __add__(self, valor_yuan):
        if self.moeda == 'USD':
            valor_yuan = valor_yuan * 0.15
        elif self.moeda == 'BRL':
            valor_yuan = valor_yuan * 0.29
        soma_moeda = self.valor + valor_yuan
        return soma_moeda
    

    def __sub__(self, valor_yuan):
        if self.moeda == 'USD':
            valor_yuan = valor_yuan * 0.15
        elif self.moeda == 'BRL':
            valor_yuan = valor_yuan * 0.29
        sub_moeda = self.valor - valor_yuan
        return sub_moeda
    
    def __add__ (self, valor_dolar):
        if self.moeda == 'CNY':
            valor_dolar = valor_dolar * 6.45
        soma_moeda = self.valor + valor_dolar
        return soma_moeda
    
    def __sub__ (self, valor_dolar):
        if self.moeda == 'CNY':
            valor_dolar = valor_dolar * 6.45
        sub_moeda = self.valor - valor_dolar
        return sub_moeda
    
    def __add__(self, valor_real):
        if self.moeda == 'CNY':
            valor_real = valor_real * 5.25
        soma_moeda = self.valor + valor_real
        return soma_moeda
    
    def __sub__(self, valor_real):
        if self.moeda == 'CNY':
            valor_real = valor_real * 5.25
        sub_moeda = self.valor - valor_real
        return sub_moeda
    
dolar = carteira('USD', 10)
novo_valor = dolar + 10
print("valor do dolar:", novo_valor)

real = carteira('BRL', 50)
novo_valor_real = real - 50
print("valor do real:", novo_valor_real)

yuan = carteira('CNY', 67)
valor_novo = yuan + 67
print("valor do yuan:", valor_novo)
