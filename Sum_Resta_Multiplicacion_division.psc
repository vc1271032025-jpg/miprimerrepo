Algoritmo Sum_Resta_Multiplicacion_division
	// Solicitar al usuario
	// que ingrese dos números enteros
	// y mostrar la suma de ambos.
	Definir NumeroEntrada1, NumeroEntrada2, NumeroTotal, NumeroTotal2, NumeroTotal3, NumeroTotal4 Como Entero
	Escribir 'Ingrese un numero entro '
	Leer NumeroEntrada1
	Escribir 'Ingrese un numero para restar '
	Leer NumeroEntrada2
	// Las condicones logicas son las que nos va a decir si es verdadero o falso
	// and
	// or
	// not >
	Si NumeroEntrada1>0 Entonces
		total <- NumeroEntrada1+NumeroEntrada2
		total2 <- NumeroEntrada1-NumeroEntrada2
		total3 <- NumeroEntrada1*NumeroEntrada2
		total4 <- NumeroEntrada1/NumeroEntrada2
	FinSi
	Escribir ' El total de la suma es ', total
	Escribir ' El total de la resta es ', total2
	Escribir ' El total de la multiplicacion es ', total3
	Escribir ' El total de la division es ', total4
FinAlgoritmo
