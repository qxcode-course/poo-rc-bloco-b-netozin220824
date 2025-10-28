class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

    def getCapacidade(self) -> int:
        return self.__capacidade

    def getCarga(self) -> int:
        return self.__carga

    def setCarga(self, carga: int):
        self.__carga = max(0, min(carga, self.__capacidade))

    def __str__(self):
        return f"{self.__carga}/{self.__capacidade}"

class Carregador:
    def __init__(self, potencia: int):
        self.__potencia: int = potencia

    def getPotencia(self) -> int:
        return self.__potencia

    def __str__(self):
        return f"{self.__potencia}W"

class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__tempo_uso: int = 0
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def turn_on(self):
        if self.__ligado:
            return
        if (self.__bateria is None or self.__bateria.getCarga() <= 0) and self.__carregador is None:
            print("fail: não foi possível ligar")
            return
        self.__ligado = True

    def turn_off(self):
        if not self.__ligado:
            return
        self.__ligado = False

    def use(self, tempo: int):
        if not self.__ligado:
            print("fail: desligado")
            return
        if self.__bateria is not None and self.__carregador is not None:
            carga_adicionada = tempo * self.__carregador.getPotencia()
            self.__bateria.setCarga(self.__bateria.getCarga() + carga_adicionada)
        elif self.__bateria is not None:
            carga_atual = self.__bateria.getCarga()
            if carga_atual <= 0:
                print("fail: desligado")
                self.turn_off()
                return
            tempo_usado = min(tempo, carga_atual)
            self.__bateria.setCarga(carga_atual - tempo_usado)
            if self.__bateria.getCarga() == 0:
                print("fail: descarregou")
                self.turn_off()
                return
            if tempo_usado < tempo:
                print("fail: descarregou")
                self.turn_off()
                return
        self.__tempo_uso += tempo

    def set_charger(self, potencia: int):
        if self.__carregador is not None:
            print("fail: carregador já conectado")
            return
        self.__carregador = Carregador(potencia)

    def rm_charger(self):
        if self.__carregador is None:
            print("fail: Sem carregador")
            return
        removido = self.__carregador
        self.__carregador = None
        print(f"Removido {removido}")
        if self.__ligado and (self.__bateria is None or self.__bateria.getCarga() <= 0):
            self.turn_off()

    def set_battery(self, capacidade: int):
        if self.__bateria is not None:
            print("fail: bateria já instalada")
            return
        self.__bateria = Bateria(capacidade)

    def rm_battery(self):
        if self.__bateria is None:
            print("fail: Sem bateria")
            return
        removido = self.__bateria
        self.__bateria = None
        print(f"Removido {removido}")
        # Verifica se o notebook deve ser desligado após remover a bateria
        if self.__ligado and self.__carregador is None:
            self.turn_off()

    def show(self):
        status = "ligado" if self.__ligado else "desligado"
        if self.__ligado:
            partes = [f"Notebook: {status} por {self.__tempo_uso} min"]
        else:
            partes = [f"Notebook: {status}"]
        if self.__carregador is not None:
            partes.append(f"Carregador {self.__carregador}")
        if self.__bateria is not None:
            partes.append(f"Bateria {self.__bateria}")
        print(", ".join(partes))

def main():
    notebook = Notebook()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            notebook.show()
        elif args[0] == "turn_on":
            notebook.turn_on()
        elif args[0] == "turn_off":
            notebook.turn_off()
        elif args[0] == "use":
            tempo = int(args[1])
            notebook.use(tempo)
        elif args[0] == "set_charger":
            potencia = int(args[1])
            notebook.set_charger(potencia)
        elif args[0] == "rm_charger":
            notebook.rm_charger()
        elif args[0] == "set_battery":
            capacidade = int(args[1])
            notebook.set_battery(capacidade)
        elif args[0] == "rm_battery":
            notebook.rm_battery()

main()

