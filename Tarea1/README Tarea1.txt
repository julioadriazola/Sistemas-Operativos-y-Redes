================================================================
			TAREA 1 - IIC2333
			     GRUPO 7

1. El archivo de ejecución debe llamarse "example.txt"
2. La Memoria del celular está simulada por los siguientes
archivos:
	2.1. "Historial.txt" : historial de llamadas hechas y
	y recibidas.
	2.2. "SMS.txt" : Datos de de los mensajes de texto
	enviados y recibidos.
	2.3. "Procesos.txt" : Información con respecto a todos
	los procesos de prioridad 3.
3. Para ingresar un comando, simplemente se debe escribir
hasta terminar, y apretar enter. Los comandos que son 
aceptados por Consola son:
	3.1. "top" : simula la función top de Unix, muestra la
	lista de procesos en ejecución, ordenados por prioridad
	(primero las llamadas, luego los mensajes y por último
	todos los demás).
	Además separa entre el que está haciendo uso de la CPU
	en ese momento y el(los) que está(n) en modo "Waiting"
	(Debido a que un proceso con mayor prioridad, como una
	llamada, está siendo ejecutado).
	3.2. "agenda" : muestra todos los contactos 
	almacenados en la memoria, para que uno pueda ser
	elegido y llamado, por el comando "call i", con i:
	número de lista del contacto.
	3.3. "call i" : llamar al contacto número i ("i" 
	es un número en el rango que tiene la agenda de
	contactos). 
	3.4. "historial" : muestra el historial de llamadas
	efectuadas y recibidas hasta el momento, en Consola.
		3.4.1. "dhistorial" : se borra la información
		guardada tanto en "Historial.txt" como en 
		"SMS.txt". En caso de algún error en la
		eliminación, se	notifica al usuario.
	3.5. "salir" : se termina la ejecución del programa.
4. Además se puede agregar un comando, con el mismo formato
que el usado en "example.txt" (con los datos separados por
un punto y coma). 

================================================================

