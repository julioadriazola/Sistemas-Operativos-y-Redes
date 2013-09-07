from multiprocessing import Process
import time


class Proceso(object):

	def __init__(self,nombre_proceso,fecha_ejecucion,tipo_proceso,prioridad_base,opciones):
		self.nombre_proceso = nombre_proceso
		self.fecha_ejecucion = fecha_ejecucion
		self.tipo_proceso = tipo_proceso
		self.prioridad_base = prioridad_base
		self.opciones = opciones

	def getNombre(self):
		return self.nombre_proceso
	def getFecha(self):
		return self.fecha_ejecucion
	def getTipo(self):
		return self.tipo_proceso
	def getPrioridad(self):
		return self.prioridad_base
	# def getTiempo(self):
	# 	return self.tiempo
	# def getTiempoTotal(self):
	# 	return self.tiempoTotal


	def writeInfo(self):
		print self.nombre_proceso + " " + str(self.fecha_ejecucion) + " " + str(self.tipo_proceso) + " " + str(self.prioridad_base),
		for op in self.opciones:
			print op,
		print ""
		
		
	def callData(self):
		if self.tipo_proceso == 1:
			llamada = 'Llamada hecha: '
		else:
			llamada = 'Llamada recibida: '

		data = self.opciones[0] + ' Fecha: ' + self.fecha_ejecucion + ' Duracion: ' + self.opciones[1],

		try:
			f = open("Historial.txt", "a")
			f.write(llamada)
		finally:
			f.close()

	def smsData(self):
		tiempo = self.opciones[1].count() * 0.020

		if self.tipo_proceso == 3:
			sms = 'Mensaje enviado a: ' + self.opciones[0],
		else:
			sms = 'Mensaje recibido de: ' + self.opciones[0],

		try:
			f = open("SMS.txt", "a")
			f.write(sms)
			if self.tipo_proceso == 4:
				f.write(self.opciones[1])
		finally:
			f.close()
	
	
def ProcessFile():
	#Leer el archivo y guardar sus lineas en la lista "lines"
	f = open("example.txt","r")
	lines = f.readlines()
	f.close()

	procesos = []
	#Procesar cada linea para crear un proceso
	for l in range(0,len(lines)):
		lines[l] = lines[l].strip()
	#	print lines[l]
		partes = lines[l].split(';')
	#	for s in range(0,len(partes)):
	#		print "   " + partes[s]
		opciones = []
		for x in range(4,len(partes)):
			opciones.append(partes[x])
		#Crear un proceso a partir de las componentes de la linea
		p = Proceso(partes[0], int(partes[1]), int(partes[2]), int(partes[3]), opciones)
		procesos.append(p)

	return procesos


# Lista con los procesos del archivo

global tiempoMaquina
tiempoMaquina=0


def funcion(num,p):
	# for x in range (0, rango[num].getFecha()):
	# 	print str(1)+ " "+str(x)
	# 	time.sleep(0.1)
	global tiempoMaquina
	ejecutandose = []
	while(not(not p and not ejecutandose)):
		print "holi"
		print str(tiempoMaquina)
		time.sleep(0.1)
	# if(p[0].getFecha() >= tiempoMaquina):
	# 	ejecutandose.append(p[0])
	# 	p.pop[0]



procesos = ProcessFile()
procesos = sorted(procesos, key=lambda Proceso: Proceso.fecha_ejecucion) 

p1 = Process(target=funcion , args=(1,procesos))
p1.start()


while(True):
	tiempoMaquina+=1
	print str(tiempoMaquina)
	time.sleep(1)

# for p in procesos:
# 	p.writeInfo()
