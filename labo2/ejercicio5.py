def transformar_validado(texto, numero):
    if numero not in [1, 2, 3]:
        print("opción inválida")
        return

    if numero == 1:
        return texto.upper()
    elif numero == 2:
        return texto.lower()
    elif numero == 3:
        return texto.capitalize()
