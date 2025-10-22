class Camisa:
    def __init__(self):
        self.__tamanho : str = ""
    def __str__(self):
        return f"sua camisa e tamanho = {self.__tamanho}"
    def getTamanho(self):
        return self.__tamanho
    def setTamanho(self,tamanho: str) -> bool:
        if tamanho == "pp" or tamanho == "p" or tamanho == "m" or tamanho == "g" or tamanho == "gg":
            self.__tamanho = tamanho
            return True
        else:
            print(f"Tamanho inválido: '{tamanho}'. Por favor, digite pp, p, m, g ou gg.")
            return False
def main():
    camisa: Camisa = Camisa()
    while True:
        n: str = input()
        if camisa.setTamanho(n):
            break
    print(camisa)
main()
