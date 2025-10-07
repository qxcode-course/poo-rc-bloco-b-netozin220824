class Chinela:
    def __init__(self, tamanho: int = 0):
        self.__tamanho = tamanho

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: int):
        self.__tamanho = valor

def main():
    chinela1 = Chinela(38)
    print(chinela1.getTamanho())
    chinela1.setTamanho(40)
    print(chinela1.getTamanho())