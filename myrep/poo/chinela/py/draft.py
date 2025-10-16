class Chinela:
    def __init__(self):
        self.__tamanho: int = 0
    def __str__(self):
        return f"sua Chinela é tamanho= {self.__tamanho}"

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, tamanho: int):
        if tamanho >=20 and tamanho <=50 and tamanho % 2 == 0:
            self.__tamanho = tamanho
        else:
            print(f"Tamanho inválido: '{tamanho}'. Por favor, digite um número par entre 20 e 50.")

def main():
    chinela = Chinela()
    while chinela.getTamanho() == 0:
        n = int(input())
        chinela.setTamanho(n)
    print(chinela)

main()