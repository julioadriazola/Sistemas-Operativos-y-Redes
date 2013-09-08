def hacer(consola):
    
    try :
        variable = consola.split(";")
    except :
        pass

    if(len>=5):
        #Crear un proceso a partir de las componentes de la linea
        print "Proceso por comando"
        opciones = []
        for x in range(4,len(variable)):
            opciones.append(variable[x])
        #Crear un proceso a partir de las componentes de la linea
        p = Proceso(variable[0], int(variable[1]), int(variable[2]), int(variable[3]), opciones)
        procesos.append(p)

    elif(consola=="agenda"):
        #aqui hay que imprimir la agenda y despues agregar la llamada elegida a la clase proceso
        print "revisando agenda"

    elif(consola=="historial"):
        #aqui hay que imprimir el archivo de historial de llamadas y mensajes
        print "revisando historial"