# Bucles Ejercicio 3: Tabla de multiplicar Escribe un programa que muestre la tabla de multiplicar 
# de un número ingresado por el usuario (del 1 al 10) usando un bucle for.

while True:
    try:
        num = int(input("Ingresa el número de la tabla que deseas: "))

        for i in range (10):
            print(num," X ",i+1," = ", num * (i + 1) )
        break
    except ValueError:
        print("Ingresa un número de verdad. ")