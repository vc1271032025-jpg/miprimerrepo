def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "⚠️ Error: La opción seleccionada no es válida."


# --- Inicio del programa interactivo ---
print("=== TRANSFORMADOR DE TEXTO ===")
# El usuario ingresa el texto
frase = input("Introduce el texto que deseas transformar: ")

# El usuario elige la opción
print("\nOpciones disponibles:")
print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")
print("3. Primera letra en Mayúscula")

try:
    seleccion = int(input("\nSelecciona un número (1, 2 o 3): "))

    # Llamamos a la función y mostramos el resultado
    resultado = transformar_texto(frase, seleccion)

    print("\n" + "=" * 30)
    print(f"RESULTADO: {resultado}")
    print("=" * 30)

except ValueError:
    print("⚠️ Error: Por favor, introduce un número válido.")
