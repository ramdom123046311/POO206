def obtener_numero_positivo():
    while True:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero < 0:
                print(" El número debe ser positivo. otra vez.")
            else:
                return numero
        except ValueError:
            print(" Error: Debes introducir un número entero no seas wey.")

# mi cuenta va desde n que es el numero ingresado hasta 0 que tambien va incluido

def cuenta_atras(n):
    cuenta = [str(i) for i in range(n, -1, -1)]  
    print("Cuenta atrás:")
    print(", ".join(cuenta))

def main():
    numero = obtener_numero_positivo()
    cuenta_atras(numero)

if __name__ == "__main__":
    main()
