import Process

class OperativeSystem():

	def __init__(self,inputText):

		self._waitForStarting=[] #Arreglo de los que esperan por iniciarse, en relación al archivo de entrada

		inp=inputText.split('\n')

		for strInp in inp:
			self._waitForStarting += [Process.Process(strInp)]
			#Los agregamos a la cola de espera

		#Ordenamos _waitForStarting según tiempos de llegada de los eventos