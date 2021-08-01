from .calculadora import Calculadora


class calEstandar(Calculadora):
    def __init__(self, n1=0, n2=0):
        super().__init__(n1=n1, n2=n2)

    def multiplicacion(self):
        mul = (self.n1 * self.n2)
        return round(mul, 2)

    def exponente(self):
        expo = (self.n1 ** self.n2)
        return round(expo, 2)

    def valorAbsoluto(self, numero):
        return abs(numero)
