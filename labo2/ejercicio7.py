def transformaciones_secuenciales(texto, lista_numeros):
    for num in lista_numeros:
        if num == 1:
            texto = texto.upper()
        elif num == 2:
            texto = texto.lower()
        elif num == 3:
            texto = texto.capitalize()
    return texto
