class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.__calibre = calibre
        self.__dureza = dureza
        self.__tamanho = tamanho

    def usoPorFolha(self) -> int:
        if self.__dureza == "HB":
            return 1
        elif self.__dureza == "2B":
            return 2
        elif self.__dureza == "4B":
            return 4
        elif self.__dureza == "6B":
            return 6
        else:
            return 0  

    def getCalibre(self) -> float:
        return self.__calibre

    def getDureza(self) -> str:
        return self.__dureza

    def getTamanho(self) -> int:
        return self.__tamanho

    def setTamanho(self, tamanho: int):
        self.__tamanho = tamanho

    def __str__(self):
        return f"[{self.__calibre}:{self.__dureza}:{self.__tamanho}]"


class Lapiseira:
    def __init__(self, calibre: float):
        self.__calibre = calibre
        self.__ponta: Grafite | None = None

    def inserir(self, grafite: Grafite) -> bool:
        if self.__ponta is not None:
            print("fail: ja existe grafite")
            return False
        if grafite.getCalibre() != self.__calibre:
            print("fail: calibre incompativel")
            return False
        self.__ponta = grafite
        return True

    def remover(self) -> Grafite | None:
        if self.__ponta is None:
            print("fail: nao existe grafite")
            return None
        removido = self.__ponta
        self.__ponta = None 
        return removido

    def escrever(self):
        if self.__ponta is None:
            print("fail: nao existe grafite")
            return
        if self.__ponta.getTamanho() <= 10:
            print("fail: tamanho insuficiente")
            return
        uso = self.__ponta.usoPorFolha()
        if self.__ponta.getTamanho() - uso < 10:
            gasto = self.__ponta.getTamanho() - 10
            self.__ponta.setTamanho(10)
            print("fail: folha incompleta")
        else:
            self.__ponta.setTamanho(self.__ponta.getTamanho() - uso)

    def __str__(self):
        ponta_str = "null" if self.__ponta is None else str(self.__ponta)
        return f"calibre: {self.__calibre}, grafite: {ponta_str}"


def main():
    lapiseira = None

    while True:
        linha = input()
        print("$" + linha)
        args = linha.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            calibre = float(args[1])
            lapiseira = Lapiseira(calibre)
        elif args[0] == "show":
            if lapiseira is not None:
                print(lapiseira)
        elif args[0] == "insert":
            if lapiseira is not None:
                calibre = float(args[1])
                dureza = args[2]
                tamanho = int(args[3])
                grafite = Grafite(calibre, dureza, tamanho)
                lapiseira.inserir(grafite)
        elif args[0] == "remove":
            if lapiseira is not None:
                lapiseira.remover()
        elif args[0] == "write":
            if lapiseira is not None:
                lapiseira.escrever()


main()
