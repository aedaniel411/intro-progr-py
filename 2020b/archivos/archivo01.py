try:
    archivito = open('datos.txt','w')
except:
    print ('Error al intentar abrir el archivo')

for i in range(10) :
    archivito.write ('Hola, hola!\n')
    #archivito.writelines('saluton!')

archivito.close()