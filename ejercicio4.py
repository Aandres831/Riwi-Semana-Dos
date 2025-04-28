# Ejercicio 4: Contador regresivo Crea un programa que pida un número positivo al usuario y 
# haga una cuenta regresiva desde ese número hasta 0 usando un bucle while.

while True:    
    try:
        num = int(input("Ingresa el número: "))

        while num >=  0:
            print(f" {num}... ")
            num -= 1
            if num < 0:
                print("Se destruyó ")
        break
    except ValueError:
        print("Ingresa un número válido. ")