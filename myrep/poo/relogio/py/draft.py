class Relogio:
    def __init__(self):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0
    
    def get_hora(self):
        return self.__hora
    def get_minuto(self):
        return self.__minuto
    def get_segundo(self):
        return self.__segundo
    def __str__(self) -> str:
        return f"{self.get_hora():02}:{self.get_minuto():02}:{self.get_segundo():02}"
    
    def set_hora(self, hora: int):
        if hora < 0 or hora > 23:
            print("fail: hora invalida")
            return
        self.__hora = hora

    def set_minuto(self, minuto: int):
        if minuto < 0 or minuto > 59:
            print("fail: minuto invalido")
            return
        self.__minuto = minuto
    
    def set_segundo(self, segundo: int):
        if segundo < 0 or segundo > 59:
            print("fail: segundo invalido")
            return
        self.__segundo = segundo

    def qtd_hora(self, hora: int):
        if hora < 0 or hora > 23:
            print("fail: hora invalida")
            self.__hora = 0   
            return
        self.__hora = hora

    def qtd_minuto(self, minuto: int):
        if minuto < 0 or minuto > 59:
            print("fail: minuto invalido")
            self.__minuto = 0
            return
        self.__minuto = minuto
        
    def qtd_segundo(self, segundo: int):
        if segundo < 0 or segundo > 59:
            print("fail: segundo invalido")
            self.__segundo = 0
            return
        self.__segundo = segundo

    def NextSecond(self):
        if self.get_segundo() == 59:
            self.set_segundo(0)
            if self.get_minuto() == 59:
                self.set_minuto(0)
                if self.get_hora() == 23:
                    self.set_hora(0)
                else:
                    self.set_hora(self.get_hora() + 1)
            else:
                self.set_minuto(self.get_minuto() + 1)
        else:
            self.set_segundo(self.get_segundo() + 1)
def main():
    relogio = Relogio()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "set":
            if len(args) >= 4:  
                relogio.set_hora(int(args[1]))
                relogio.set_minuto(int(args[2]))
                relogio.set_segundo(int(args[3]))
        elif args[0] == "init":
            if len(args) >= 4:
                relogio.qtd_hora(int(args[1]))
                relogio.qtd_minuto(int(args[2]))
                relogio.qtd_segundo(int(args[3]))
        elif args[0] == "next":
            relogio.NextSecond()
    
main()
