
from logging import Logger
from logging import getLogger


class TestClass:
    def __init__(self):
        self.logger: Logger = getLogger(__name__)

    def sayHello(self):
        print('Hola!')


if __name__ == "__main__":

    TestClass().sayHello()
