def obtener_numero():
    while True:
        try:
            numero = int(input("Introduce un número entero positivo mayor de 10: "))
            if numero <= 10:
                print(" El número debe ser mayor de 10. Intenta de nuevo.")
            else:
                return numero
        except ValueError:
            print(" Error: Debes introducir un número entero válido.")

def mostrar_impares_hasta(n):
    impares = [str(i) for i in range(3, n + 1, 2)]  # empezamos en 3 porque 2 no es impar
    print("Números impares desde 2 hasta", n, ":")
    print(", ".join(impares))

def main():
    numero = obtener_numero()
    mostrar_impares_hasta(numero)

if __name__ == "__main__":
    main()