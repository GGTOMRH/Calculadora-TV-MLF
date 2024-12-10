import random
import time

cartass = {
    "A": "Copas",
    "A": "Espadas"
}


naipes = ["Copas", "Espadas", "Paus", "Ouros"]

cartas = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2","A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2","A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2","A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

random.shuffle(cartas)
for carta in cartas:
    print(carta)
