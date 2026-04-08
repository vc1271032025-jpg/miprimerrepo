def transformar_y_contar(texto, numero):
    resultado = ""
    if numero == 1:
        resultado = texto.upper()
    elif numero == 2:
        resultado = texto.lower()
    elif numero == 3:
        resultado = texto.capitalize()

    return len(resultado)
