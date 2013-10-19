import os

global _dir_file_to_adress, _ram_size, _hdd_size, _ram_folder, _hdd_folder
global _ram_administrator
_dir_file_to_adress=1
_ram_size=1024
_hdd_size=512
_ram_folder='./ram/'
_hdd_folder='./hdd/'

_ram_administrator=list()
for i in range(1,ram_blocks+1):
	tmp=list()
	tmp.append(-1) #Ultima vez usado
	tmp.append()

def isInRAM(dir_ram_file):
	print 'Está en RAM'

def readRAM(position):
	print 'leyendo RAM'

def readFile(file_name):
	print 'Abriendo archivo'

def fileToRAMAdress(file_name):
	print 'Buscando file_name'

def bringPageFromHDDtoRAM(dir_hdd_file):
	print 'Page Replace'



#Iniciamos X bloques de ram e Y bloques de hdd, truncando si es que el tamaño es mayor
def __begin(ram_blocks,hdd_blocks):
	for i in range(1,ram_blocks+1):
		if (os.path.isfile(_ram_folder+str(i))):
			f = open(_ram_folder+str(i),'rw+')
			text = f.read()
			f.close()
			if(len(text)>_ram_size):
				f = open(_ram_folder+str(i),'rw+')
				f.truncate(_ram_size)
		else:
			open(_ram_folder+str(i),'a').close()

	# for i in range(1,hdd_blocks+1):
	if (os.path.isfile(_hdd_folder+str(i))):
		f = open(_hdd_folder+str(i),'rw+')
		text = f.read()
		f.close()
		if(len(text)>_hdd_size):
			f = open(_hdd_folder+str(i),'rw+')
			f.truncate(_hdd_size)
	else:
		open(_hdd_folder+str(i),'a').close()


__begin(20,800)





	# ¿Está el archivo file_to_adress en RAM?
		# Si: Abrirlo
		# No: pageReplace(file_to_adress) y abrirlo
	# Leer file_to_adress y obtener dirección de file_name
	# while_not ¿Está file_name en file_to_adress?
		# Si: ¿Está dir_file_name en RAM?
			# Si: Abrirlo
			# No: pageReplace(dir_file_name) y abrirlo
		# No: createFile(file_name)
	# while ¿Quedan lineas por leer de file_name?   (IMPORTANTE: Cada vez que se lea se debe cuidar de actualizar los parámetros para el pageReplace)
		#¿Es direccionamiento directo?
			#Si: ¿Está el archivo de la dirección en RAM?
				#Si: Leerlo
				#No: pageReplace(dir) y leerlo
		#¿Es direccionamiento indirecto primario?
			#Si: ¿Está el bloque en RAM?
				#Si: Abrirlo
				#No: pageReplace(dir) y abrirlo
				#Leerlo
				#while ¿Quedan lineas por leer de dir_file?
					#Si: ¿Está el archivo de la dirección en RAM?
						#Si: Abrirlo
						#No: pageReplace(dir) y Abrirlo
		#Press 'N' para leer el siguiente

