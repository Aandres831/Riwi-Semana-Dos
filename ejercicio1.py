# Estructuras Condicionales Ejercicio 1: 
# Clasificador de números Escribe un programa que
# pida al usuario un número entero y determine si es positivo, negativo o cero.
while True:
    try:
        num = int(input("Ingresa el número:"))
        if num > 0:
            print(f"El número {num} es positivo. ")
            break
        elif num < 0:
            print(f"El número {num} es negativo. ")
            break
        else:
            print(f"El número es cero. ")
            break
    except ValueError:
        print("Ingresa un número válido por favor. ") 