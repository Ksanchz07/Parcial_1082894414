import re

def total_caracteres(texto):
    # Cuenta el número total de caracteres en el texto
    return len(texto)

def total_palabras(texto):
    # Cuenta el número de palabras separadas por espacios
    if not texto:
        return 0
    palabras = 0
    en_palabra = False
    for c in texto:
        if c != ' ' and not en_palabra:
            palabras += 1
            en_palabra = True
        elif c == ' ':
            en_palabra = False
    return palabras

def total_oraciones(texto):
    # Cuenta el número de oraciones separadas por . ! ?
    oraciones = re.split(r'[.!?]', texto)
    oraciones = [o.strip() for o in oraciones if o.strip()]
    return len(oraciones)

def palabra_mas_larga(texto):
    # Encuentra la palabra más larga en el texto
    palabras = texto.split()
    if not palabras:
        return ""
    mas_larga = palabras[0]
    for palabra in palabras:
        if len(palabra) > len(mas_larga):
            mas_larga = palabra
    return mas_larga

def palabra_mas_corta(texto):
    # Encuentra la palabra más corta en el texto
    palabras = texto.split()
    if not palabras:
        return ""
    mas_corta = palabras[0]
    for palabra in palabras:
        if len(palabra) < len(mas_corta):
            mas_corta = palabra
    return mas_corta

def numero_vocales(texto):
    # Cuenta el número de vocales (a, e, i, o, u, mayúsculas y minúsculas)
    vocales = "aeiouAEIOU"
    contador = 0
    for c in texto:
        if c in vocales:
            contador += 1
    return contador

def numero_consonantes(texto):
    # Cuenta el número de consonantes (letras que no son vocales)
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    contador = 0
    for c in texto:
        if c in consonantes:
            contador += 1
    return contador

def main():
    # Bucle principal para pedir el texto hasta que sea válido
    while True:
        texto = input("Ingresa un texto para analizar (no vacío): ").strip()
        if not texto:
            print("El texto no puede estar vacío. Intenta de nuevo.")
            continue
        break

    # Mostrar las estadísticas calculadas
    print("\nEstadísticas del texto:")
    print(f"Total de caracteres: {total_caracteres(texto)}")
    print(f"Total de palabras: {total_palabras(texto)}")
    print(f"Total de oraciones: {total_oraciones(texto)}")
    print(f"Palabra más larga: '{palabra_mas_larga(texto)}'")
    print(f"Palabra más corta: '{palabra_mas_corta(texto)}'")
    print(f"Número de vocales: {numero_vocales(texto)}")
    print(f"Número de consonantes: {numero_consonantes(texto)}")

if __name__ == "__main__":
    main()
