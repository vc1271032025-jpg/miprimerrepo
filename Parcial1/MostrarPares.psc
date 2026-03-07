Algoritmo MostrarPares
	Definir N, i, par Como Entero
	
	Escribir "Ingrese la cantidad de números pares a mostrar:"
	Leer N
	
	Si N <= 0 Entonces
		Escribir "Por favor, ingrese un número mayor a cero."
	Sino
		Escribir "Los primeros ", N, " números pares son:"
		
		Para i <- 1 Hasta N Con Paso 1 Hacer
			par <- i * 2
			Escribir par
		FinPara
	FinSi
FinAlgoritmo
