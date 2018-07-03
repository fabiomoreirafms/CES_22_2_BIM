
class AbstractInterface:
# Target interface.
# This is the target interface, that clients use.

    def someFunctionality(self):
        raise NotImplemented()

class Bridge(AbstractInterface):

    """ Bridge class.
     
    This class forms a bridge between the target
    interface and background implementation.
    """

    def __init__(self):
        self.__implementation = None

class ComputerScientist(Bridge):

    """ Variant of the target interface.
 
    This is a variant of the target Abstract interface.
    It can do something little differently and it can
    also use various background implementations through
    the bridge.
    """

    def __init__(self, implementation, a, b):
        super(Bridge, self).__init__()
        self.__implementation = implementation
        self.a = a
        self.b = b

    def someFunctionality(self):
        print ("Computer Scientist: ")
        self.__implementation.anotherFunctionality(self.a, self.b)

class ComputerEngineer(Bridge):

    def __init__(self, implementation, a, b):
        super(Bridge, self).__init__()
        self.__implementation = implementation
        self.a = a
        self.b = b

    def someFunctionality(self):
        print ("Computer Engineer: ")
        self.__implementation.anotherFunctionality(self.a, self.b)

class ImplementationInterface:

    """ Interface for the background implementation.
 
    This class defines how the Bridge communicates
    with various background implementations.
    """

    def anotherFunctionality(self, a, b):
        raise NotImplemented

class Som(ImplementationInterface):

    """ Concrete background implementation.
 
    A variant of background implementation, in this
    case for Linux!
    """

    def anotherFunctionality(self, a, b):
        resp = 0
        for i in range (a):
            resp = resp + b
        print ("Resposta por múltiplas somas de a * b é: {0}".format(resp))

class Prod(ImplementationInterface):
    def anotherFunctionality(self, a, b):
        resp = a * b
        print("Resposta por produto de a * b é: {0}".format(resp))


if __name__=='__main__':
    ComputerScientist(Prod(), 17, 12).someFunctionality()
    ComputerEngineer(Prod(), 17, 12).someFunctionality()
    ComputerScientist(Som(), 17, 12).someFunctionality()
    ComputerEngineer(Som(), 17, 12).someFunctionality()