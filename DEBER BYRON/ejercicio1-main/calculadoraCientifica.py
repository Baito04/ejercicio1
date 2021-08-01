from .calculadora import Calculadora


class calCienti(Calculadora):
    PI = 3.1416

    def __init__(self, n1=0, n2=0):
        super().__init__()
    
    def circunferencia(self, radio):
        circu = (2 * self.PI) * radio
        return round(circu, 2)

    def areaCirculo(self, radio):
        a_cir = (self.PI * (radio**2))
        return round(a_cir, 2)

    def areaCuadrado(self, lado):
        a_cuad = (lado * lado)
        return round(a_cuad, 2)
