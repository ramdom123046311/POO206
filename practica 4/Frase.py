def obtener_frase():
    while True:
        frase = input("Introduce una frase: ").strip()
        if frase == "":
            print(" La frase no puede estar vacía. Inténtalo de nuevo.")
        else:
            return frase

def obtener_letra():
    while True:
        letra = input("Introduce una letra: ").strip()
        if len(letra) != 1:
            print(" Error: Debes introducir solo una letra.")
        elif not letra.isalpha():
            print(" Solo se permiten letras del alfabeto.")
        else:
            return letra

def contar_letra(frase, letra):
    cantidad = frase.lower().count(letra.lower())  # Cuenta ignorando mayúsculas
    print(f"La letra '{letra}' aparece {cantidad} veces en la frase.")

def main():
    try:
        frase = obtener_frase()
        letra = obtener_letra()
        contar_letra(frase, letra)
    except Exception as e:
        print(" Ocurrió un error inesperado:", e)

if __name__ == "__main__":
    main()
