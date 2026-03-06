Algoritmo Promedio
	// Solicitar al usuario
	// que ingrese dos números enteros
	// y mostrar la suma de ambos.
	Definir NumeroEntrada1, NumeroEntrada2, NumeroEntrada3, totalSuma, totalPromedio, numeroTotal Como Entero
	Escribir 'Ingrese un numero entro '
	Leer NumeroEntrada1
	Escribir 'Ingrese un numero para restar '
	Leer NumeroEntrada2
	Escribir 'Ingresar un numero para sumar '
	Leer NumeroEntrada3
	// Las condicones logicas son las que nos va a decir si es verdadero o falso
	// and
	// or
	// not >
	Si NumeroEntrada1>0 Entonces
		totalSuma <- NumeroEntrada1+NumeroEntrada2+NumeroEntrada3
	FinSi
	Si totalSuma>0 Entonces
		totalPromedio <- totalSuma/3
	FinSi
	Escribir ' El total de el promedio es ', totalPromedio
FinAlgoritmo
