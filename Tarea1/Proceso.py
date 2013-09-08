from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
import time
import math

# Falta:
# 2 - Arreglar ejecutar Accion
# 	2.1 - Con manejo de archivos
# 	2.2 - Sin manejo de archivos
# 3 - Top
# 5 - Consultar Agenda y Revisar historial de llamadas y SMS

class Proceso(object):

	def __init__(self,nombre_proceso,fecha_ejecucion,tipo_proceso,prioridad_base,opciones):
		self.nombre_proceso = nombre_proceso
		self.fecha_ejecucion = fecha_ejecucion
		self.tipo_proceso = tipo_proceso
		if(tipo_proceso == 1 or tipo_proceso == 2):
			self.numCola=0
		elif(tipo_proceso == 3 or tipo_proceso == 4):
			self.numCola=1
		else:
			self.numCola=2
		self.prioridad_base = prioridad_base
		self.opciones = opciones

		#Llamada
		if( tipo_proceso == 1 or tipo_proceso == 2):
			self.duracion = int(opciones[1])
			self.numeroTelefono = opciones[0]
		#Mensaje 
		elif( tipo_proceso == 3 or tipo_proceso == 4):
			self.duracion = int(math.ceil(len(self.opciones[1]) * 0.020))
			if(tipo_proceso == 3):
				self.receptor = opciones[0]
			elif(tipo_proceso == 4):
				self.emisor = opciones[0]
		#AgregarContacto
		elif( tipo_proceso == 5):
			self.duracion = 1
		#Procesos Cualquiera
		elif ( tipo_proceso == 6):
			self.duracion = int(opciones[0])
		#Mandar Ubicacion
		elif( tipo_proceso == 7):
			self.duracion = 2
		#Ver ubicacion
		elif (tipo_proceso == 8):
			self.duracion = int(opciones[0])
		#Jugar
		elif (tipo_proceso == 9):
			self.duracion = int(opciones[0])
		#Musica
		elif(tipo_proceso == 10):
			self.duracion = int(opciones[0])




	def getNombre(self):
		return self.nombre_proceso
	def getFecha(self):
		return self.fecha_ejecucion
	def getTipo(self):
		return self.tipo_proceso
	def getPrioridad(self):
		return self.prioridad_base
	def getNumCola(self):
		return self.numCola


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

	def ejecutarAccion(self,delta):
		if(self.duracion>0):
			self.duracion-=delta

		if(self.tipo_proceso == 1):
			a=1
		elif(self.tipo_proceso == 2):
			a=2
		elif(self.tipo_proceso == 3):
			a=2
		elif(self.tipo_proceso == 4):
			a=2
		elif(self.tipo_proceso == 5):
			a=2
		elif(self.tipo_proceso == 6):
			a=2
		elif(self.tipo_proceso == 7):
			a=2
		elif(self.tipo_proceso == 8):
			a=2
		elif(self.tipo_proceso == 9):
			a=2
		elif(self.tipo_proceso == 10):
			a=2

		print self.nombre_proceso + " " + str(self.duracion)

	def isAlive(self):
		return self.duracion>0


	
	
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


def topfunction(ejecutandose):
	print "Procesos Ejecutandose :"
	for i in range(0,3):
		for j in range(0,len(ejecutandose[i]):






def funcion(num,p,consola):
	global tiempoMaquina
	tiempoMaquina=0
	procesos = ProcessFile()
	procesos = sorted(procesos, key=lambda Proceso: Proceso.fecha_ejecucion) 



	# p1 = Process(target=funcion , args=(1,procesos))
	# p1.start()

	ejecutandose = [[],[],[]]

	deltaT=0.5

	while(True):
		print str(consola.value)
		# for p in procesos:
		# 	p.writeInfo()
		for x in range(0,int(1/deltaT)):
			if(procesos or ejecutandose):
				# Si hay elentos que agregar a ejecutando
				# if(procesos):
					# print str(procesos[0].getFecha())
				while(procesos and procesos[0].getFecha() <= tiempoMaquina):
					ejecutandose[procesos[0].getNumCola()].append(procesos[0])
					del procesos[0]
				# print "1"
				if(ejecutandose[0]):
					ejecutandose[0][0].ejecutarAccion(deltaT)
					if (not ejecutandose[0][0].isAlive()):
						del ejecutandose[0][0]


				elif(ejecutandose[1]):
					ejecutandose[1][0].ejecutarAccion(deltaT)
					if (ejecutandose[1][0].isAlive()):
						ejecutandose[1].append(ejecutandose[1][0])
					del ejecutandose[1][0]


				elif(ejecutandose[2]):
					ejecutandose[2][0].ejecutarAccion(deltaT)
					if (ejecutandose[2][0].isAlive()):
						ejecutandose[2].append(ejecutandose[2][0])
					del ejecutandose[2][0]

			time.sleep(deltaT)

		tiempoMaquina+=1
		print str(tiempoMaquina)



consola = Array('c', 'holaholahola')	

p1 = Process(target=funcion, args=(1,100,consola))
p1.start()

texto = ""
while(texto <> "s"):
	texto = raw_input("")
	consola.value = 'chaooo'
	print texto + "oliafadgwhtjefjdlgkdsgkgsjkfghjskfghskfhghsfkghsfkj"
# for p in procesos:
# 	p.writeInfo()
