# Múltiples excepciones en una línea
def dividir_numeros():
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1 / num2
        print(f"El resultado es: {resultado}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
    else:
        print("División realizada con éxito")
        
dividir_numeros()