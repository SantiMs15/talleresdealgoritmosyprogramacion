Algoritmo Inicio_ventas
	Escribir "Sueldo base: "
	Leer sueldo
	Escribir "Valor primera venta: "
	Leer venta1
	Escribir "Valor segunda venta: "
	Leer venta2
	Escribir "Valor tercera venta: "
	Leer venta3
	comisiones<-(venta1+venta2+venta3)*10/100
	total<-comisiones+sueldo
	Escribir "Ganancias en comisiones: " comisiones
	Escribir "Ganancias totales del mes: " total
	
FinAlgoritmo