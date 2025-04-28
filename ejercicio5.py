# Ejercicio Combinado Ejercicio 5: Adivina el número Crea un programa que genere un número aleatorio entre 1 y 10, 
# y le pida al usuario que lo adivine. 
# El programa debe indicar si el número ingresado es mayor, menor o correcto. El usuario tiene hasta 3 intentos.

import random


num_random = random.randint(1, 10)
intentos = 3

while True:
    try:
        while intentos <= 3 and intentos > 0:
            #intentos -= 1
            num_usuario = int(input("Ingresa el número: ", ))
            #i += 1
            if num_random == num_usuario:
                print (f"Felicidades Adivinate el número {num_random}")
                break

            if num_random < num_usuario:
                print(f"El número {num_usuario} es mayor. ")
            elif num_random > num_usuario:
                print(f"El número {num_usuario} es menor. ")

                intentos -= 1
            if intentos == 0:
                print(f"No lograste adivinar el {num_random}")
        break
    except ValueError:
        print("Ingresa un número válido. ")
