class Chinela:
    def __init__(self):
        self.__tamanhox: int = 0
        self.__tamanhoy: int = 0
    def __str__(self):
        return f"sua Chinela é tamanho = {self.__tamanhox}/{self.__tamanhoy}"

    def getTamanho(self):
        return self.__tamanhoy

    def setTamanho(self, tamanhox: int, tamanhoy: int):
        if tamanhox >= 20 and tamanhox <= 50:
            self.__tamanhox = tamanhox
        else:
            print(f"Tamanho inválido: '{tamanhox}'. Por favor, digite um número entre 20 e 50.")

        if tamanhoy >= 20 and tamanhoy <= 50 and tamanhoy == tamanhox + 1:
            self.__tamanhoy = tamanhoy
        else:
            print(f"Tamanho inválido: '{tamanhoy}'. Por favor, digite um número entre 20 e 50.")

def main():
    chinela = Chinela()
    while chinela.getTamanho() == 0:
        n = input().split("/")
        tamanhox = int(n[0])
        tamanhoy = int(n[1])
        chinela.setTamanho(int(tamanhox), int(tamanhoy))
    print(chinela)

main()