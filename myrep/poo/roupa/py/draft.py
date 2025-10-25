class Roupa:
    def __init__(self):
        self.__tamanho = ""  
    def getTamanho(self):
        return self.__tamanho 
    def setTamanho(self, tamanho):
        tamanhos_validos = ["pp", "p", "m", "g", "gg", "xg"]
        if tamanho in tamanhos_validos:
            self.__tamanho = tamanho
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
def __str__(self):
        return f"sua roupa é tamanho = {self.__tamanho}"
def main():
    roupa: Roupa = Roupa()
    while roupa.getTamanho() == "":
        n: str = input()
        roupa.setTamanho(n)
    print(roupa)
main()