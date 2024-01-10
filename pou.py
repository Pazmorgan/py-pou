import random

def minmax(value):
    return max(0, min(value, 100))

class Pou:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = random.randint(25, 50)
        self.energy = random.randint(50, 100)
        self.happiness = 70
        self.health = 100
        self.alive = True

    def status(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Hunger:", self.hunger)
        print("Energy:", self.energy)
        print("Happiness:", self.happiness)
        print("Health:", self.health)

    def play(self):
        self.hunger = minmax(self.hunger + random.randint(0, 10))
        self.energy = minmax(self.energy + random.randint(0, 10))
        self.happiness = minmax(self.happiness + random.randint(0, 10))
        self.health = minmax(self.health + random.randint(0, 10))
        self.age += 1       
        """self.status()"""

    def eat(self):
        self.hunger = minmax(self.hunger + random.randint(10, 20))
        self.energy = minmax(self.energy + random.randint(10, 20))
        self.happiness = minmax(self.happiness - random.randint(0, 10))
        self.age += 1       

        """self.status()"""
        

    def sleep(self):
        self.hunger = minmax(self.hunger - random.randint(10, 20))
        self.energy = minmax(self.energy + random.randint(10, 20))
        self.happiness = minmax(self.happiness - random.randint(10, 30))
        self.health = minmax(self.health + random.randint(10, 20))
        self.age += 1
        """self.status()"""
        

    def check_status(self):
        if self.hunger == 0 or self.energy == 0 or self.happiness == 0:
            self.alive = False
            print(f"{self.name} no ha sido bien cuidado. Se acabó la partida.")

def game_loop(pou):
    while pou.alive:
        pou.status()
        option = input("¿Qué quieres hacer? (play, eat, sleep, exit): ")

        if option == "play":
            pou.play()
        elif option == "eat":
            pou.eat()
        elif option == "sleep":
            pou.sleep()
        elif option == "exit":
            break
        else:
            print("Opción no válida. Vuelve a intentarlo.")

        pou.check_status()

# Instancia de Pou
toto = Pou("Toto")

# Bucle del juego
game_loop(toto)
