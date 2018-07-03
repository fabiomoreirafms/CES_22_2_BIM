import abc


class Aeronave:

    def __init__(self, state):
        self._state = state

    def setstate(self, state):
        self._state = state

    def request(self):
        n = self._state.handle()
        if n == 0:
            if isinstance(self._state, Disp):
                self._state = Indisp()
            else:
                self._state = Disp()


class Situacao(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def handle(self):
        pass


class Disp(Situacao):

    def __init__(self):
        self.situacao = "Disponivel"
        self.horas = 100


    def handle(self):
        self.horas = self.horas - 20
        print (self.situacao +" " + str(self.horas) + " disponiveis")
        return self.horas


class Indisp(Situacao):

    def __init__(self):
        self.situacao = "Manutencao"
        self.horas = -30

    def handle(self):
        self.horas = self.horas + 10
        print(self.situacao + " faltam " + str(-self.horas) + " horas para ficar disponível")
        return self.horas


def main():
    caracal = Aeronave(Disp())
    caracal.request()
    caracal.request()
    caracal.request()
    caracal.request()
    caracal.request()
    caracal.request()
    caracal.request()
    caracal.request()
    caracal.request()
    caracal.request()
    caracal.request()
    caracal.request()


if __name__ == "__main__":
    main()
