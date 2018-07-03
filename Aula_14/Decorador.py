# Feito com base no exemplo do material didático fornecido

class CarOptions:
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class Celula(CarOptions):
    cost = 60000

class Decorator(CarOptions):
    def __init__(self, caroptions):
        self.component = caroptions
    def getTotalCost(self):
        return self.component.getTotalCost() + CarOptions.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription() + ' ' +CarOptions.getDescription(self)

class ABS(Decorator):
    cost = 2000
    def __init__(self, caroptions):
        Decorator.__init__(self, caroptions)

class PinturaMetalica(Decorator):
    cost = 1200
    def __init__(self, caroptions):
        Decorator.__init__(self, caroptions)

class ArDigital(Decorator):
    cost = 1500
    def __init__(self, caroptions):
        Decorator.__init__(self, caroptions)

class MotorTurbo(Decorator):
    cost = 7000
    def __init__(self, caroptions):
        Decorator.__init__(self, caroptions)

entrada = ABS(Celula())
print(str(entrada.getDescription())+ ": $" + str(entrada.getTotalCost()))

confortline = PinturaMetalica(ArDigital(ABS(Celula())))
print(str(confortline.getDescription())+ ": $" + str(confortline.getTotalCost()))

hiline = MotorTurbo(PinturaMetalica(ArDigital(ABS(Celula()))))
print(str(hiline.getDescription())+ ": $" + str(hiline.getTotalCost()))
