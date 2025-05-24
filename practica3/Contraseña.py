import string

def validar_contraseña(contraseña):
    # Verifica si la longitud es menor a 10
    if len(contraseña) < 10:
        return "Contraseña demasiado corta"

    # Verifica si contiene al menos un número
    if not any(char.isdigit() for char in contraseña):
        return "Debe contener al menos un número"

    # Verifica si contiene al menos un carácter especial
    caracteres_especiales = string.punctuation  
    if not any(char in caracteres_especiales for char in contraseña):
        return "Debe contener al menos un carácter especial"

    # Si pasa todas las validaciones
    return "Contraseña válida"

def pedir_contraseña():
    try:
        contraseña = input("Ingresa una contraseña: ")
        if not contraseña.strip():
            raise ValueError("No se ingresó ninguna contraseña.")
        resultado = validar_contraseña(contraseña)
        print(resultado)
    except ValueError as e:
        print("Error:", e)

pedir_contraseña()
