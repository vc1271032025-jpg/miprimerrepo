def transformar_lista(lista, opcion):
    resultado = []
    for palabra in lista:
        if opcion == 1:
            resultado.append(palabra.upper())
        elif opcion == 2:
            resultado.append(palabra.lower())
        elif opcion == 3:
            resultado.append(palabra.capitalize())
    return resultado
