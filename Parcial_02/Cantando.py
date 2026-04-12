palabra = "CANTANDO"
minusculas = palabra.lower()
sin_sufijo = minusculas.removesuffix("ando")
indice_t = sin_sufijo.find("t")
print(f"Resultado: {sin_sufijo}, Índice de 't': {indice_t}")
