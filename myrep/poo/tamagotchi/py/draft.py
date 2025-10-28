class Tamagotchi:
    def __init__(self, energyMax: int, cleanMax: int):
        self.energyMax = energyMax
        self.cleanMax = cleanMax
        self.energy = energyMax
        self.clean = cleanMax
        self.age = 0
        self.alive = True

    def setEnergy(self, value: int):
        self.energy = max(0, min(value, self.energyMax))
        if self.energy == 0:
            self.alive = False

    def setClean(self, value: int):
        self.clean = max(0, min(value, self.cleanMax))
        if self.clean == 0:
            self.alive = False

    def getEnergy(self) -> int:
        return self.energy

    def getClean(self) -> int:
        return self.clean

    def getAge(self) -> int:
        return self.age

    def isAlive(self) -> bool:
        return self.alive

    def __str__(self):
        return f"E:{self.energy}/{self.energyMax}, L:{self.clean}/{self.cleanMax}, I:{self.age}"

class Game:
    def __init__(self):
        self.pet = None

    def init(self, energyMax: int, cleanMax: int):
        self.pet = Tamagotchi(energyMax, cleanMax)

    def show(self):
        if self.pet:
            print(self.pet)

    def play(self):
        if not self.pet or not self.pet.isAlive():
            print("fail: pet esta morto")
            return
        self.pet.setEnergy(self.pet.getEnergy() - 2)
        self.pet.setClean(self.pet.getClean() - 3)
        self.pet.age += 1
        if not self.pet.isAlive():
            if self.pet.getEnergy() == 0:
                print("fail: pet morreu de fraqueza")
            else:
                print("fail: pet morreu de sujeira")

    def shower(self):
        if not self.pet or not self.pet.isAlive():
            print("fail: pet esta morto")
            return
        self.pet.setEnergy(self.pet.getEnergy() - 3)
        self.pet.setClean(self.pet.cleanMax)
        self.pet.age += 2
        if not self.pet.isAlive():
            print("fail: pet morreu de fraqueza")

    def sleep(self):
        if not self.pet or not self.pet.isAlive():
            print("fail: pet esta morto")
            return
        if self.pet.getEnergy() > self.pet.energyMax - 5:
            print("fail: nao esta com sono")
            return
        turnos = self.pet.energyMax - self.pet.getEnergy()
        self.pet.setEnergy(self.pet.energyMax)
        self.pet.age += turnos

def main():
    game = Game()
    while True:
        line = input().strip()
        print("$" + line)
        args = line.split()
        if not args:
            continue
        cmd = args[0]
        if cmd == "end":
            break
        elif cmd == "init":
            energyMax = int(args[1])
            cleanMax = int(args[2])
            game.init(energyMax, cleanMax)
        elif cmd == "show":
            game.show()
        elif cmd == "play":
            game.play()
        elif cmd == "shower":
            game.shower()
        elif cmd == "sleep":
            game.sleep()

if __name__ == "__main__":
    main()
