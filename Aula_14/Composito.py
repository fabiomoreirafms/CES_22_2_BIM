import abc

class Component(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def operation(self):
        pass


class Setor(Component):

    def __init__(self):
        self._funcionarios = set()

    def operation(self):
        for funcionario in self._funcionarios:
            funcionario.operation()

    def add(self, funcionario):
        self._funcionarios.add(funcionario)

    def remove(self, funcionario):
        self._funcionarios.discard(funcionario)


class Funcionario(Component):

    def __init__(self, nome, prof):
        self.nome = nome
        self.prof = prof
        if prof == 'Computer Engineer':
            self.salario = 15000
        else:
            self.salario = 'valor desconhecido'

    def operation(self):
        print("{0} é {1} e recebe {2}".format(self.nome, self.prof, self.salario))


def main():
    fulano = Funcionario('Fulano', 'Computer Scientist')
    beltrano = Funcionario('Beltrano', 'Computer Engineer')
    computer_jobs = Setor()
    computer_jobs.add(fulano)
    computer_jobs.add(beltrano)
    computer_jobs.operation()

if __name__ == "__main__":
    main()
