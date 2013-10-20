import os

global _dir_file_to_adress, _ram_size, _hdd_size, _ram_folder, _hdd_folder
global _ram_administrator, _lru, _directorio, _primer_indice
global _ram, _vacio, _directorio, _num_vacios
_num_vacios=0
_lru=0
_dir_file_to_adress=1
_ram_size=1024
_hdd_size=512
_ram_folder='./ram/'
_hdd_folder='./disco/'
_primer_indice=3
# _ram_administrator=list()
# for i in range(1,ram_blocks+1):
# 	tmp=list()
# 	tmp.append(-1) #Ultima vez usado
# 	tmp.append()


class bloqueRAM(object):
	def __init__(self,dir_ram):
		self._dir_hdd1=-1
		self._dir_hdd2=-1
		self._type=-1
		self._lru=-1
		self._dir_ram=dir_ram

	def leerBloqueDisco(self,dir_hdd1,dir_hdd2,_type):
		self._dir_hdd1=dir_hdd1
		self._dir_hdd2=dir_hdd2
		self._type=_type
		self.refreshLRU()
		#1: directorio
		#2: inodo
		#3: bloque de información
		if(_type==1):
			text = ''
			for i in range(1,3):
				if (os.path.isfile(_hdd_folder+str(i))):
					f = open(_hdd_folder+str(i),'rw+')
					text = text + f.read()
					f.close()
					# print "pasa por aqui"
			self._info=text
			if(os.path.isfile(_ram_folder+str(1))):
				f = open(_ram_folder+str(1),'rw+')
				f.truncate()
				f.write(self._info)
				f.close()
				# print "pasa por 2"



		if(_type==2):
			text = ''
			if (os.path.isfile(_hdd_folder+str(dir_hdd1))):
				f = open(_hdd_folder+str(dir_hdd1),'rw+')
				text = text + f.read()
				f.close()
			self._info=text
			if(os.path.isfile(_ram_folder+str(self._dir_ram))):
				f = open(_ram_folder+str(self._dir_ram),'rw+')
				f.truncate()
				f.write(self._info)
				f.close()
		
		if(_type==3):
			text = ''
			if (os.path.isfile(_hdd_folder+str(dir_hdd1))):
				f = open(_hdd_folder+str(dir_hdd1),'rw+')
				text = text + f.read()
				f.close()
			if(dir_hdd2!=-1):
				if (os.path.isfile(_hdd_folder+str(dir_hdd2))):
					f = open(_hdd_folder+str(dir_hdd2),'rw+')
					text = text + f.read()
					f.close()
			self._info=text
			if(os.path.isfile(_ram_folder+str(self._dir_ram))):
				f = open(_ram_folder+str(self._dir_ram),'rw+')
				f.truncate()
				f.write(self._info)
				f.close()


		if(_type==4):
			text = ''
			for i in range(3,5):
				if (os.path.isfile(_hdd_folder+str(i))):
					f = open(_hdd_folder+str(i),'rw+')
					text = text + f.read()
					f.close()
			self._info=text
			if(os.path.isfile(_ram_folder+str(2))):
				f = open(_ram_folder+str(2),'rw+')
				f.truncate()
				f.write(self._info)
				f.close()


	def saveToDisk(self):
		if(len(self._info)>512):
			if(os.path.isfile(_hdd_folder+str(self._dir_hdd1))):
				f = open(_hdd_folder+str(self._dir_hdd1),'rw+')
				f.truncate()
				f.write(self._info[0:512])
				f.close()
			if(os.path.isfile(_hdd_folder+str(self._dir_hdd2))):
				f = open(_hdd_folder+str(self._dir_hdd2),'rw+')
				f.truncate()
				f.write(self._info[512:len(self._info)])
				f.close()
		else:
			if(os.path.isfile(_hdd_folder+str(self._dir_hdd1))):
				f = open(_hdd_folder+str(self._dir_hdd1),'rw+')
				f.truncate()
				f.write(self._info[0:len(self._info)])
				f.close()


	def refreshLRU(self):
		global _lru
		self._lru=_lru
		_lru=_lru+1
		# print "lru: "+str(_lru)+ " vs lru_objeto: "+ str(self._lru)

	def addBloqueRAM(self,content,dir_hdd1,dir_hdd2,_type,refresh):
		if(_type==2):
			self._dir_hdd1=dir_hdd1
			self._dir_hdd2=dir_hdd2
			self._type=_type
			self._info=content
			if(os.path.isfile(_ram_folder+str(self._dir_ram))):
				f = open(_ram_folder+str(self._dir_ram),'rw+')
				f.truncate()
				f.write(self._info)
				f.close()

		if(_type==3):
			self._dir_hdd1=dir_hdd1
			self._dir_hdd2=dir_hdd2
			self._type=_type
			self._info=content
			if(os.path.isfile(_ram_folder+str(self._dir_ram))):
				f = open(_ram_folder+str(self._dir_ram),'rw+')
				f.truncate()
				f.write(self._info)
				f.close()
		if(refresh):
			self.refreshLRU()
		else:
			self._lru=-1



	def refreshContent(self,content):
		if(self._type==1):
			global _directorio
			tmp=[]
			for key in _directorio:
				tmp.append(key+" "+str(_directorio[key]))
			self._info='\n'.join(tmp)
		if(self._type==2):
			self._info='\n'.join(content)
		if(self._type==4):
			global _vacio
			self._info=''.join(str(x) for x in _vacio)
			# print "|--"+self._info+"--|"



def editFile(file_name,add_content):
	global _directorio
	if(file_name in _directorio):
		#buscamos inodo
		dir_file_name=_directorio[file_name]

		global _ram
		encontrado=False
		dir_ram_rep=-1
		for i in range (1,len(_ram)):
			#ver si inodo esta en ram
			if(_ram[i]._dir_hdd1==dir_file_name and _ram[i]._type==2):
				dir_ram_rep=i
				encontrado=True
		#si no esta en ram, se le asigna una pagina y se lee el bloque de disco y se trae a ram
		if(not encontrado):
			dir_ram_rep=pageReplacement()
			_ram[dir_ram_rep].leerBloqueDisco(dir_file_name,-1,2)

		tmp=_ram[dir_ram_rep]._info.split("\n") #dir_ram_rep dir de inodo en ram

		largo_en_bloques=len(tmp)-3 #Le quitamos los 2 headers y el ultimo archivo que no sabemos si está completo
		i=len(tmp)-1 #el ultimo bloque de la wea
		sub_encontrado=False

		for j in range (1,len(_ram)):
			if((_ram[j]._dir_hdd1==int(tmp[i]) or _ram[j]._dir_hdd2==int(tmp[i])) and _ram[j]._type==3):
				sub_encontrado=True
				_ram[j].saveToDisk()
				_ram[j].addBloqueRAM("",-1,-1,-1,False)

		dir_ram_sub_rep=pageReplacement()
		_ram[dir_ram_sub_rep].leerBloqueDisco(int(tmp[i]),-1,3)


		tamano_archivo=largo_en_bloques*512+len(add_content)+len(_ram[dir_ram_sub_rep]._info)
		if(tamano_archivo>1024*5):
			print "No se puede agregar el contenido: Archivo excede tamaño máximo (5KB)"
		else:
			num_bloq_hdd=0
			tam=len(add_content)+len(_ram[dir_ram_sub_rep]._info)
			if(tam%512==0):
				num_bloq_hdd=int(tam/512)#Numero de bloques en disco
			else:
				num_bloq_hdd=int(tam/512)+1
			if(tam%1024==0):
				num_bloq_ram=int(tam/1024) #Numero de bloques en disco
			else:
				num_bloq_ram=int(tam/1024)+1 #Funcion Techo 



			if(num_bloq_hdd-1>_num_vacios):
				print "Sorry pero tu disco está lleno de weas, no cabe este archivo en disco. Borre el porno"
			else:

				lista_bloques_por_ocupar=[]
				lista_bloques_por_ocupar.append(_ram[dir_ram_sub_rep]._dir_hdd1)
				for i in range(0,num_bloq_hdd-1): #Sin el bloque que ya estoy ocupando
					lista_bloques_por_ocupar.append(nextEmpty(True))
				

				tmp[len(tmp)-1]=str(lista_bloques_por_ocupar[0]) #La ultima linea del inodo la actualizamos
				for i in range (1,len(lista_bloques_por_ocupar)): #Le agregamos el resto de las nuevas lineas
					tmp.append(str(lista_bloques_por_ocupar[i]))
				
				_ram[dir_ram_rep].refreshContent(tmp)

				content=_ram[dir_ram_sub_rep]._info+add_content

				lista_de_ram=[]
				for i in range(0,num_bloq_ram):
					next_p=0
					if(i==0):
						next_p=dir_ram_sub_rep
					else:
						next_p=pageReplacement()
					lista_de_ram.append(next_p)
					contenido=''
					bloq1=-1
					bloq2=-1
					if(len(content)>=(i+1)*1024):
						contenido=content[i*1024:(i+1)*1024]
						bloq1=lista_bloques_por_ocupar[i*2]
						bloq2=lista_bloques_por_ocupar[i*2+1]
					else:
						contenido=content[i*1024:len(content)]
						if(len(content)-i*1024>512):
							bloq1=lista_bloques_por_ocupar[i*2]
							bloq2=lista_bloques_por_ocupar[i*2+1]
						else:
							bloq1=lista_bloques_por_ocupar[i*2]

					_ram[next_p].addBloqueRAM(contenido,bloq1,bloq2,3,True)

				_ram[1].refreshContent(1)
				_ram[1].saveToDisk()
				_ram[2].refreshContent(1)
				_ram[2].saveToDisk()
				_ram[dir_ram_rep].saveToDisk()
				for i in range (0,len(lista_de_ram)):
					_ram[lista_de_ram[i]].saveToDisk()







def deleteFile(file_name):
	global _directorio, _vacio, _ram
	if(file_name in _directorio):
		dir_file_name=_directorio[file_name]
		del _directorio[file_name]

		dir_ram_rep=-1
		for i in range (1,len(_ram)):
			#ver si inodo esta en ram
			if(_ram[i]._dir_hdd1==dir_file_name and _ram[i]._type==2):
				dir_ram_rep=i
				encontrado=True
		#si no esta en ram, se le asigna una pagina y se lee el bloque de disco y se trae a ram
		if(not encontrado):
			dir_ram_rep=pageReplacement()
			_ram[dir_ram_rep].leerBloqueDisco(dir_file_name,-1,2)

		_vacio[dir_file_name-1]=0

		tmp=_ram[dir_ram_rep]._info.split("\n")

		for i in range (2,len(tmp)):
			print tmp[i]+": "+str(_vacio[int(tmp[i])-1])
			_vacio[int(tmp[i])-1]=0
			print tmp[i]+": "+str(_vacio[int(tmp[i])-1])

		_ram[1].refreshContent(1)
		_ram[1].saveToDisk()
		_ram[2].refreshContent(1)
		_ram[2].saveToDisk()

		print file_name+" borrado exitosamente"
	else:
		print "El archivo "+file_name+" no existe"



def readFile(file_name):
	global _directorio
	if(file_name in _directorio):
		#buscamos inodo
		dir_file_name=_directorio[file_name]

		global _ram
		encontrado=False
		dir_ram_rep=-1
		for i in range (1,len(_ram)):
			#ver si inodo esta en ram
			if(_ram[i]._dir_hdd1==dir_file_name and _ram[i]._type==2):
				dir_ram_rep=i
				encontrado=True
		#si no esta en ram, se le asigna una pagina y se lee el bloque de disco y se trae a ram
		if(not encontrado):
			dir_ram_rep=pageReplacement()
			_ram[dir_ram_rep].leerBloqueDisco(dir_file_name,-1,2)

		tmp=_ram[dir_ram_rep]._info.split("\n")

		for i in range (2,len(tmp)):
			if(i%2==0):
				if(i+1<len(tmp)):
					sub_encontrado=False
					for j in range (1,len(_ram)):
						if(_ram[j]._dir_hdd1==int(tmp[i]) and _ram[j]._dir_hdd2==int(tmp[i+1]) and _ram[j]._type==3):
							print _ram[j]._info
							sub_encontrado=True
					if(not sub_encontrado):
						dir_ram_sub_rep=pageReplacement()
						_ram[dir_ram_sub_rep].leerBloqueDisco(int(tmp[i]),int(tmp[i+1]),3)
						print _ram[dir_ram_sub_rep]._info
				else:
					sub_encontrado=False
					for j in range (1,len(_ram)):
						if(_ram[j]._dir_hdd1==int(tmp[i]) and _ram[j]._type==3):
							print _ram[j]._info
							sub_encontrado=True
					if(not sub_encontrado):
						dir_ram_sub_rep=pageReplacement()
						_ram[dir_ram_sub_rep].leerBloqueDisco(int(tmp[i]),-1,3)
						print _ram[dir_ram_sub_rep]._info

		return True
	else:
		return False


def createFile(content,file_name):
	global _directorio,_num_vacios
	if(file_name in _directorio):
		print "Lamentamos el inconveniente, el nombre del archivo ya existe :("
	else:
		if(len(content)>10*512):
			print "Su archivo es demasiado pesado para este sistema, Tamaño max: 5KB"
		else:
			num_bloq_hdd=0
			num_bloq_ram=0
			if(len(content)%512==0):
				num_bloq_hdd=int(len(content)/512) +1#Numero de bloques en disco
			else:
				num_bloq_hdd=int(len(content)/512)+1 + 1 #Funcion Techo + 1 del inodo
			if(len(content)%1024==0):
				num_bloq_ram=int(len(content)/1024) #Numero de bloques en disco
			else:
				num_bloq_ram=int(len(content)/1024)+1 #Funcion Techo 


			if(num_bloq_hdd>_num_vacios):
				print "Sorry pero tu disco está lleno de weas, no cabe este archivo en disco. Borre el porno"
			else:
				next_empty_hdd=nextEmpty(True)
				_directorio[file_name]=next_empty_hdd
				ram_page=pageReplacement()

				lista_bloques_por_ocupar=[]
				for i in range(0,num_bloq_hdd-1): #Sin el Inodo
					lista_bloques_por_ocupar.append(nextEmpty(True))
					# print "Bloques a usar: "+str(lista_bloques_por_ocupar[i])

				contenido_inodo="Tiempo creado\nTiempo editado\n"+'\n'.join(str(x) for x in lista_bloques_por_ocupar)
				# print "|--"+contenido_inodo+"--|"

				_ram[ram_page].addBloqueRAM(contenido_inodo,next_empty_hdd,-1,2,True)


				lista_de_ram=[]
				for i in range(0,num_bloq_ram):
					next_p=pageReplacement()
					lista_de_ram.append(next_p)
					contenido=''
					bloq1=-1
					bloq2=-1
					if(len(content)>=(i+1)*1024):
						contenido=content[i*1024:(i+1)*1024]
						bloq1=lista_bloques_por_ocupar[i*2]
						bloq2=lista_bloques_por_ocupar[i*2+1]
					else:
						contenido=content[i*1024:len(content)]
						if(len(content)-i*1024>512):
							bloq1=lista_bloques_por_ocupar[i*2]
							bloq2=lista_bloques_por_ocupar[i*2+1]
						else:
							bloq1=lista_bloques_por_ocupar[i*2]

					_ram[next_p].addBloqueRAM(contenido,bloq1,bloq2,3,True)
				_ram[1].refreshContent(1)
				_ram[1].saveToDisk()
				_ram[2].refreshContent(1)
				_ram[2].saveToDisk()
				_ram[ram_page].saveToDisk()
				for i in range (0,len(lista_de_ram)):
					_ram[lista_de_ram[i]].saveToDisk()


def nextEmpty(replace):
	global _vacio
	for i in range (0,len(_vacio)):
		if(_vacio[i]==0):
			if(replace):
				_vacio[i]=1
			return i+1 #Está desfasado, por eso i+1

def shutDown():
	print "oli"


def pageReplacement():
	global _ram
	min_lru=_ram[_primer_indice]._lru
	min_pos=_primer_indice
	for i in range(_primer_indice,len(_ram)):
		# print str(i)+": "+str(_ram[i]._lru) + "vs " +str(min_pos)+": "+str(_ram[min_pos]._lru)
		if(min_lru > _ram[i]._lru):
			min_lru=_ram[i]._lru
			min_pos=i
	if(_ram[min_pos]._type>0):
		_ram[min_pos].saveToDisk()
	return min_pos



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

	for i in range(1,hdd_blocks+1):
		if (os.path.isfile(_hdd_folder+str(i))):
			f = open(_hdd_folder+str(i),'rw+')
			text = f.read()
			f.close()
			if(len(text)>_hdd_size):
				f = open(_hdd_folder+str(i),'rw+')
				f.truncate(_hdd_size)
		else:
			open(_hdd_folder+str(i),'a').close()


	global _ram, _vacio, _directorio, _num_vacios
	_ram=[] #Creamos el arreglo de ram
	_ram.append(0) #Direccion 0 no existe y 1 está reservada para directorio y 2 para bloques_disco vacios
	for i in range(1,21):
		_ram.append(bloqueRAM(i))


	#Cargamos directorio

	_ram[1].leerBloqueDisco(1,2,1)
	_directorio=dict() #Creamos el diccionario de directorio
	if(len(_ram[1]._info)>0):
		tmp=_ram[1]._info.split("\n")
		for i in range(len(tmp)):
			tmp1=tmp[i].split(" ")
			_directorio[tmp1[0]]=tmp1[1]

	#Cargamos página de bloques vacíos
	_ram[2].leerBloqueDisco(3,4,4)
	_vacio=[] #Creamos el arreglo de posiciones vacías
	tmp=_ram[2]._info
	for i in range(len(tmp)):
		if(int(tmp[i])==0):
			_num_vacios=_num_vacios+1
		_vacio.append(int(tmp[i]))



#Cuando se prende el sistema
__begin(20,800)

createFile("1","Hola")

editFile("Hola","Vamos a fallar. Sorry pero tu disco está lleno de weas, no cabe este archivo en disco. Borre el porno\n")

# createFile("k3t09itqieojgoeqihg\n\nsdasdsad\nojda i hqeojoqj ogjqogh qghqogjqei gjqigpqoj gpqgpoid","adsad1")

# deleteFile("adsad1")
# deleteFile("oli")
