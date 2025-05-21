try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print("El resultado es:", resultado)

except ValueError:
    print("Error: Debes introducir un número entero.")
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.")
