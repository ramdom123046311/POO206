def es_bisiesto(año):
    # Regla de año bisiesto
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def verificar_año_bisiesto():
    try:
        año = int(input("Ingresa un año (número entero): "))
        if es_bisiesto(año):
            print(f"El año {año} es bisiesto.")
        else:
            print(f"El año {año} no es bisiesto.")
    except ValueError:
        print("Error: Debes ingresar un número entero válido para el año.")

verificar_año_bisiesto()
