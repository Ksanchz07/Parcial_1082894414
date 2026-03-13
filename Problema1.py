import re

def longitud_valida(contraseña):
    return 8 <= len(contraseña) <= 20

def tiene_mayuscula(contraseña):
    return any(c.isupper() for c in contraseña)

def tiene_minuscula(contraseña):
    return any(c.islower() for c in contraseña)

def tiene_numero(contraseña):
    return any(c.isdigit() for c in contraseña)

def tiene_especial(contraseña):
    especiales = "!@#$%^&*"
    return any(c in especiales for c in contraseña)

def validar_contraseña(contraseña):
    return (longitud_valida(contraseña) and
            tiene_mayuscula(contraseña) and
            tiene_minuscula(contraseña) and
            tiene_numero(contraseña) and
            tiene_especial(contraseña))

def obtener_errores(contraseña):
    errores = []
    if not longitud_valida(contraseña):
        errores.append("La contraseña debe tener entre 8 y 20 caracteres.")
    if not tiene_mayuscula(contraseña):
        errores.append("La contraseña debe tener al menos una mayúscula.")
    if not tiene_minuscula(contraseña):
        errores.append("La contraseña debe tener al menos una minúscula.")
    if not tiene_numero(contraseña):
        errores.append("La contraseña debe tener al menos un número.")
    if not tiene_especial(contraseña):
        errores.append("La contraseña debe tener al menos un carácter especial (!@#$%^&*).")
    return errores

def main():
    while True:
        contraseña = input("Ingresa una contraseña: ")
        if validar_contraseña(contraseña):
            print("Contraseña válida.")
            break
        else:
            errores = obtener_errores(contraseña)
            print("Contraseña inválida. Razones:")
            for error in errores:
                print(f"- {error}")

if __name__ == "__main__":
    main()