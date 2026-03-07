Algoritmo SolicitarNumeros
	Definir num Como Real
	
	Escribir "Ingrese un número entre 1 y 10 para continuar:"
	Leer num
	
	Mientras num >= 1 Y num <= 10 Hacer
		Escribir "Número correcto. Ingrese otro (o uno fuera de rango para salir):"
		Leer num
	FinMientras
	
	Escribir "Número inválido detectado. Programa finalizado."
FinAlgoritmo
