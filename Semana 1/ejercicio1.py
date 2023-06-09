while True:
    numero = int(input("Ingrese un número impar: "))
    if numero % 2 == 0:
        print("El numero es par, ingrese nuevamente un numero que sea impar")
    else:
        print("El numero es impar")
        break