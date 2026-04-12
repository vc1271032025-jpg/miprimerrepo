poema = """No pude convertirme en nada: Ni en bueno ni en malo,
ni en un sinvergüenza ni en un hombre honesto,
ni en héroe ni en insecto. Y ahora estoy alargando mis días
 en mi esquina, torturándome con el amargo e inútil consuelo 
 que un hombre inteligente no puede convertirse seriamente en nada; 
 de que tan solo un idiota puede convertirse en algo"""
conteo_a = poema.count("a")
lista_oraciones = poema.splitlines()
print(f"Letras 'a': {conteo_a}, Lista: {lista_oraciones}")
