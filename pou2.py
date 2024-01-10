import random

def minmax(value):
    return max(0, min(value, 100))

state = {
    "nombre": "Pou",
    "edad": 0,
    "hambre": random.randint(25, 50),
    "energia": random.randint(50, 75),
    "felicidad": random.randint(60, 80),
    "vida": 100,
    "vivo": True
}

def status():
    print("Nombre:", state["nombre"])
    print("Edad:", state["edad"])
    print("Hambre:", state["hambre"])
    print("Energia:", state["energia"])
    print("Felicidad:", state["felicidad"])
    print("Vida:", state["vida"])

def fin_partida():
    if state["hambre"] == 0 or state["energia"] == 0 or state["felicidad"] == 0:
        state["vivo"] = False
        print(f"{state['nombre']} No ha sido bien cuidado. Se acabó la partida.")

def jugar(state):
    new_state = dict(state)
    new_state["hambre"] = minmax(state["hambre"] - random.randint(5, 15))
    new_state["energia"] = minmax(state["energia"] - random.randint(15, 25))
    new_state["felicidad"] = minmax(state["felicidad"] + random.randint(20, 25))
    new_state["vida"] = minmax(state["vida"] - random.randint(15, 20))
    new_state["edad"] = minmax(state["edad"] + random.randint(0, 1))
    return new_state

def comer(state):
    new_state = dict(state)
    new_state["hambre"] = minmax(state["hambre"] + random.randint(15, 25))
    new_state["energia"] = minmax(state["energia"] + random.randint(20, 30))
    new_state["felicidad"] = minmax(state["felicidad"] - random.randint(10, 20))
    new_state["vida"] = minmax(state["vida"] + random.randint(10, 20))
    new_state["edad"] = minmax(state["edad"] + random.randint(0, 1))
    return new_state

def dormir(state):
    new_state = dict(state)
    new_state["hambre"] = minmax(state["hambre"] - random.randint(20, 25))
    new_state["energia"] = minmax(state["energia"] + random.randint(25, 30))
    new_state["felicidad"] = minmax(state["felicidad"] - random.randint(10, 20))
    new_state["vida"] = minmax(state["vida"] + random.randint(10, 15))
    new_state["edad"] = minmax(state["edad"] + random.randint(0, 1))
    return new_state

while state["vivo"]:
    status()
    option = input("¿Qué te apetece hacer? (jugar, dormir, comer, salir): ")

    if option == "jugar":
        state = jugar(state)
    elif option == "comer":
        state = comer(state)
    elif option == "dormir":
        state = dormir(state)
    elif option == "salir":
        break
    else:
        print("Opción no válida. Vuelve a intentarlo.")

    fin_partida()
