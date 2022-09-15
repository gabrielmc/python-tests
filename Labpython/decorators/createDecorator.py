
# Decorator a nivel de functions 
class customUppercase(object):
    def __ini__(self, function):
        self.function = function

    def __call__(self, *args):
        self.function(args[0].upper())


@customUppercase
def nome(nome):
    print(f'Nome: {nome}')

nome("gabriel")



# --------------------------------------------------------
# Api publica para conversão do Real => Dolar
# https://economia.awesomeapi.com.br/last/USD-BRL/bid

# obs:
# Decorator são comumente usados em interfaces e
# modificações a nível de functions.