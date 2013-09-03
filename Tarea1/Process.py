

class Process():

	def __init__(self,inputText):
		self._arrive_time = len(inputText)
		# Aquí se debiera analizar todo el input del texto 
		# y pasarlo a las distintas variables de interés

	def getArriveTime(self):
		return self._arrive_time

a=Process("Holiiafdaií")
print a.getArriveTime()