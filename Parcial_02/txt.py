archivo = "Cristian.txt"
# Se asume que el ejercicio pide limpiar prefijos/sufijos y pasar a minúsculas
nombre_limpio = archivo.removesuffix(".txt").removeprefix("ING. ")
resultado = nombre_limpio.lower()
print(resultado)
