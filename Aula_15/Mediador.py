class Comandante:

    def __init__(self):
        self._pessoal = Pessoal(self)
        self._operacoes = Operacoes(self)
        self._material = Material(self)

    def addanv(self, anv):
        self._material.addanv(anv)
        self._material.adddisp(anv)
    def disp(self):
        return self._material.disp()
    def addmilitar(self, militar):
        self._pessoal.add(militar)
    def equipagens(self):
        return self._pessoal.equipagens()
    def missao(self):
        print("Missoes: " + str(self._operacoes.missao(self.equipagens(), self.disp())))


class Pessoal:

    def __init__(self, mediator):
        self._mediator = mediator
        self.militares =[]

    def add(self, nome):
        self.militares.append(nome)

    def remove(self, nome):
        self.militares.remove(nome)

    def equipagens(self):
        return self.militares

class Operacoes:

    def __init__(self, mediator):
        self._mediator = mediator
    def missao(self, equipagens, disp):
        i = 0
        mission = []
        for anv in disp:
            if i<len(equipagens):
                mission.append((anv, equipagens[i]))
                i = i + 1
        return mission

class Material:

    def __init__(self, mediator):
        self._mediator = mediator
        self.aeronaves = []
        self.inspecao = []
        self.disponiveis = []

    def disp(self):
        return self.disponiveis

    def addanv(self, anv):
        self.aeronaves.append(anv)

    def removeanv(self, anv):
        self.aeronaves.remove(anv)

    def addinsp(self, anv):
        self.inspecao.append(anv)

    def adddisp(self, anv):
        self.disponiveis.append(anv)


def main():
    comandante = Comandante()
    comandante.addmilitar('fulano')
    comandante.addmilitar('ciclano')
    comandante.addanv('8512')
    comandante.addanv('8510')
    comandante.missao()


if __name__ == "__main__":
    main()
