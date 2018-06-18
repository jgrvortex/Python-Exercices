4

import random
from time import sleep

SECONDS = 3

while True:
    number = random.randint(1,10)
    print("Adivina el número secreto comprendido entre 1 y 10")
    sleep(SECONDS)
    print("El número oculto era {}".format(number))