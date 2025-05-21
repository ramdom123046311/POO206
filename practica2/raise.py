# raise
def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    elif edad < 18:
        raise ValueError("Debes ser mayor de edad")
    else:
        print("Edad válida")

try:
    edad = int(input("Ingrese su edad: "))
    validar_edad(edad)
except ValueError as e:
    print(f"Error: {e}")
else:
    print("Edad aceptada")