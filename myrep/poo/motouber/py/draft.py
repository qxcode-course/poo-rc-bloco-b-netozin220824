class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def __str__(self):
        return f"{self.__nome}:{self.__dinheiro}"

    def getNome(self):
        return self.__nome

    def getDinheiro(self):
        return self.__dinheiro

    def setDinheiro(self, valor: int):
        self.__dinheiro = valor


class Moto:
    def __init__(self):
        self.__custo = 0
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None

    def setDriver(self, nome: str, dinheiro: int):
        self.__motorista = Pessoa(nome, dinheiro)

    def setPass(self, nome: str, dinheiro: int) -> bool:
        if self.__motorista is None:
            print("fail: no driver")
            return False
        self.__passageiro = Pessoa(nome, dinheiro)
        self.__custo = 0  # Reseta custo ao entrar passageiro
        return True

    def drive(self, km: int):
        if self.__passageiro is None:
            print("fail: no passenger")
            return
        self.__custo += km

    def leavePass(self):
        if self.__passageiro is None:
            print("fail: no passenger")
            return
        paga = min(self.__custo, self.__passageiro.getDinheiro())
        if paga < self.__custo:  # Imprime fail se não pagou o total
            print("fail: Passenger does not have enough money")
        self.__passageiro.setDinheiro(self.__passageiro.getDinheiro() - paga)
        self.__motorista.setDinheiro(self.__motorista.getDinheiro() + self.__custo)  # Motorista recebe o custo total
        print(f"{self.__passageiro.getNome()}:{self.__passageiro.getDinheiro()} left")  # Imprime dinheiro restante (após subtração)
        self.__passageiro = None
        self.__custo = 0

    def __str__(self):
        driver = "None" if self.__motorista is None else str(self.__motorista)
        passenger = "None" if self.__passageiro is None else str(self.__passageiro)
        return f"Cost: {self.__custo}, Driver: {driver}, Passenger: {passenger}"


def main():
    moto = Moto()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setDriver":
            nome = args[1]
            dinheiro = int(args[2])
            moto.setDriver(nome, dinheiro)
        elif args[0] == "setPass":
            nome = args[1]
            dinheiro = int(args[2])
            moto.setPass(nome, dinheiro)
        elif args[0] == "drive":
            km = int(args[1])
            moto.drive(km)
        elif args[0] == "leavePass":
            moto.leavePass()


main()
