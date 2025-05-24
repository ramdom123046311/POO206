def es_palindroma(cadena):
    
    cadena_limpia = cadena.lower().replace(" ", "")
    return cadena_limpia == cadena_limpia[::-1]

def verificar_palindromo():
    try:
        texto = input("Ingresa una cadena de texto: ")
        if not texto.strip():  
            raise ValueError("La cadena no puede estar vacía.")
        
        if es_palindroma(texto):
            print(f"La cadena \"{texto}\" es palíndroma.")
        else:
            print(f"La cadena \"{texto}\" no es palíndroma.")
    except ValueError as e:
        print("Error:", e)

verificar_palindromo()
