Algoritmo Cuadrado
	// Solicitar al usuario
	// que ingrese dos números enteros
	// y mostrar la suma de ambos.
	Definir NumeroEntrada, numeroTotal Como Entero
	Escribir 'Ingrese un numero entro '
	Leer NumeroEntrada
	// Las condicones logicas son las que nos va a decir si es verdadero o falso
	// and
	// or
	// not >
	Si NumeroEntrada>0 Entonces
		numeroTotal <- NumeroEntrada*NumeroEntrada
	FinSi
	Escribir ' El total del cuadrado es ', numeroTotal
FinAlgoritmo
