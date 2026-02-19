Algoritmo Compra
	// Solicitar al usuario
	// que ingrese dos números enteros
	// y mostrar la suma de ambos.
	Definir Presio, Cantidad, total Como Real
	Escribir 'Ingrese el presio del producto '
	Leer Presio
	Escribir 'Ingrese la cantidad '
	Leer Cantidad
	// Las condicones logicas son las que nos va a decir si es verdadero o falso
	// and
	// or
	// not >
	Si Presio>0 Entonces
		total <- Presio*Cantidad
	FinSi
	Escribir ' El total a pagar es ', total
FinAlgoritmo
