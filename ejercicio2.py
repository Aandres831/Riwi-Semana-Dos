# Ejercicio 2: Aprobado o reprobado Crea un programa que reciba la calificación de un estudiante (0 a 100) 
# e indique si está aprobado (60 o más) o reprobado (menos de 60).


while True:
    try:
        calificacion = int(input("Ingresa la calificación:"))

        if calificacion >= 60 and calificacion <= 100:
            print(f"El estudiante aprueba el curso. ")
            break
        elif calificacion >= 0 and calificacion < 60:
            print(f"El estudiante reprueba el curso. ")
            break
        else:
            print("Ingresa un calificación entre 0 - 100")
    except ValueError:
        print("Ingresa una calificación válida. ")