Algoritmo Inicio_calificaciones
	Escribir "Digite primera calificación parcial: "
	Leer parcial1
	Escribir "Digite su segunda calificación parcial: "
	Leer parcial2 
	Escribir "Digite su tercera calificación parcial: " 
	Leer parcial3
	Escribir"Digite su calificación del examen final: "
	Leer examen
	Escribir "Digite su calificación del trabajo final: "
	Leer trabajo
	parciales<-(parcial1+parcial2+parcial3)/3*0.55
	exam<-examen*0.30
	proyecto<-trabajo*0.15
	final<-parciales+exam+proyecto
	Escribir "Nota final en la materia es de: " final
	
FinAlgoritmo