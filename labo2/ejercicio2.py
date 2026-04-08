def mostrar_resultado(palabra, numero):
    if numero == 1:
        print(palabra.upper())
    elif numero == 2:
        print(palabra.lower())
    elif numero == 3:
        print(palabra.capitalize())
    else:
        print("Opción inválida")


mostrar_resultado("Hola", 1)
mostrar_resultado("Hola", 2)
mostrar_resultado("Hola", 3)
