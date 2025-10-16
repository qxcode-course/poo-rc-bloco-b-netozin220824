class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria| None = None
    def __str__(self)-> str:
        return f"ligar: {self.__ligado} bateria: {self.bateria}"
    def ligar(self):
        if self.__ligado:
            print(f"notebook ligado")
        else:
            print(f"notebook desligado")
    def usar(self,tempo: int):
        if tempo

class Bateria: