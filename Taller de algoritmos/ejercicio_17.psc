Algoritmo Inicio_velocidades
	Escribir "Digite velocidad (km/h) del veh�culo que va detr�s: "
	Leer v1
	Escribir "Digite velocidad (km/h) del veh�culo que va delante: "
	Leer v2
	Escribir "Digite distancia (km) entre ambos veh�culos: "
	Leer distancia
	t1<-distancia/v1
	dist1<-t1*v2
	tiempo<-(dist1+distancia)/v1
	tiempof<-redon(tiempo*60)
	Escribir "Los minutos que transcurriran para que ambos veh�culos se encuentren son: " tiempof
	
FinAlgoritmo