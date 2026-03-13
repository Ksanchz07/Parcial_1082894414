# Programa para validar contraseñas según criterios específicos

# Función auxiliar: verificar longitud mínima
def tiene_longitud_minima(contraseña):
    return len(contraseña) >= 8

# Función auxiliar: verificar longitud máxima
def tiene_longitud_maxima(contraseña):
    return len(contraseña) <= 20

# Función auxiliar: verificar al menos una mayúscula
def tiene_mayuscula(contraseña):
    for caracter in contraseña:
        if caracter.isupper():
            return True
    return False

# Función auxiliar: verificar al menos una minúscula
def tiene_minuscula(contraseña):
    for caracter in contraseña:
        if caracter.islower():
            return True
    return False

# Función auxiliar: verificar al menos un número
def tiene_numero(contraseña):
    for caracter in contraseña:
        if caracter.isdigit():
            return True
    return False

# Función auxiliar: verificar al menos un carácter especial
def tiene_caracter_especial(contraseña):
    especiales = "!@#$%^&*"
    for caracter in contraseña:
        if caracter in especiales:
            return True
    return False

# Función principal: validar contraseña
def validar_contraseña(contraseña):
    # Se verifican todos los criterios
    if (tiene_longitud_minima(contraseña) and
        tiene_longitud_maxima(contraseña) and
        tiene_mayuscula(contraseña) and
        tiene_minuscula(contraseña) and
        tiene_numero(contraseña) and
        tiene_caracter_especial(contraseña)):
        return True
    else:
        return False

# Programa principal: pedir contraseñas hasta que sean válidas
while True:
    contraseña = input("Ingrese una contraseña: ")
    
    if validar_contraseña(contraseña):
        print("¡Contraseña válida!")
        break
    else:
        print("La contraseña no cumple con los siguientes requisitos:")
        if not tiene_longitud_minima(contraseña):
            print("- Debe tener al menos 8 caracteres")
        if not tiene_longitud_maxima(contraseña):
            print("- No debe superar los 20 caracteres")
        if not tiene_mayuscula(contraseña):
            print("- Debe tener al menos una letra mayúscula")
        if not tiene_minuscula(contraseña):
            print("- Debe tener al menos una letra minúscula")
        if not tiene_numero(contraseña):
            print("- Debe tener al menos un número")
        if not tiene_caracter_especial(contraseña):
            print("- Debe tener al menos un carácter especial (!@#$%^&*)")