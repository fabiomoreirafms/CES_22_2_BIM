import abc

class AbstractSequence(metaclass=abc.ABCMeta):
    """
    Declare an interface for operations that create abstract product
    objects.
    """

    @abc.abstractmethod
    def fibonacci(self):
        pass


class Sequence1(AbstractSequence):
    """
    Implement the operations to create concrete product objects.
    """

    def fibonacci(self):
        return ConcreteFibonacci1()


class Sequence2(AbstractSequence):
    """
    Implement the operations to create concrete product objects.
    """

    def fibonacci(self):
        return ConcreteFibonacci2()


class AbstractFibonacci(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface(self):
        pass


class ConcreteFibonacci1(AbstractFibonacci):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface(self, n):
        def fib(n):
            if n <= 2:
                return 1
            return fib(n - 2) + fib(n - 1)
        sequence = []
        for i in range(1,n+1):
            sequence.append(fib(i))
        return sequence


class ConcreteFibonacci2(AbstractFibonacci):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface(self, n):
        def fib(n):
            if n == 1:
                sequence = [1]
            f1 = 1
            f2 = 1
            sequence = [1, 1]
            for i in range(n-1):
                aux = f2
                f2 = f2 + f1
                f1 = aux
                sequence.append(f2)
            return sequence
        return fib(n)


def main():
    for factory in (Sequence1(), Sequence2()):
        produto = factory.fibonacci()
        sequencia = produto.interface(10)
        for i in range(10):
            print("{0} ".format(sequencia[i]))

if __name__ == "__main__":
    main()
