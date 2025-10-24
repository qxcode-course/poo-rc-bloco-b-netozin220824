class Roupa:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
    def __str__(self):
        return f"sua camisa e tamanho = {self.__tamanho}"
    def getTamanho(self):
        return self.__tamanho
    def setTamanho(self,tamanho: str) -> bool:
        if tamanho == "pp" or tamanho == "p" or tamanho == "m" or tamanho == "g" or tamanho == "gg":
            self.__tamanho = tamanho
            return True
        else:
            print(f"Valor inválido: '{tamanho}'. Por favor, digite pp, p, m, g ou gg.")
            return False
def main():
    roupa: Roupa = Roupa()
    while True:
        n: str = input()
        if roupa.setTamanho(n):
            break
    print(roupa)
main()
