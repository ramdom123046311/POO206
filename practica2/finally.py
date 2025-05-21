# finally
def manejar_archivo():
    try:
        archivo = open("datos.txt", "r")
        contenido = archivo.read()
        print(contenido)
    except FileNotFoundError:
        print("El archivo no existe")
    finally:
        print("Cerrando recursos...")
        # Este bloque siempre se ejecuta, haya o no excepciones
        if 'archivo' in locals():
            archivo.close()

manejar_archivo()