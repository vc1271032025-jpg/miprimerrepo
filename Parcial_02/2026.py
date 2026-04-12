cadena = "Python2026"
if cadena.isalnum():
    minusculas = cadena.lower()
    solo_texto = minusculas.replace("2026", "")
    print(f"Resultado: {solo_texto}")
