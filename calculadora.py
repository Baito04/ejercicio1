class Calculadora:
    def __init__(self, n1=0, n2=0):
        self.n1 = n1
        self.n2 = n2

    def suma(self):
        sumar = (self.n1 + self.n2)
        return round(sumar, 2)

    def resta(self):
        res = (self.n1 - self.n2)
        return round(res, 2)

    def multiplicacion(self):
        mul = self.n1 * self.n2
        return mul

    def division(self):
        if self.numero2 == 0: return 0
        div = (self.n1 / self.n2)
        return round(div, 2)
