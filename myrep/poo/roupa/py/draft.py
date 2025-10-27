from pyparsing import line


class Roupa:
    def __init__(self):
        self.__tamanho : str = ""
    def __str__(self):
        if self.__tamanho == "":
            return "size: ()"
        else:
            return f"size: ({self.__tamanho})"
    def getTamanho(self):
        return self.__tamanho
    def setTamanho(self,tamanho: str):
        tamanhos_disponiveis = ["PP","P","M","G","GG","XG"]
        if tamanho in tamanhos_disponiveis:
            self.__tamanho = tamanho
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
def main():
    roupa = Roupa()
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        if args[0] == "show":
            print(roupa)
        elif args[0] == "size":
            roupa.setTamanho(args[1])
main()