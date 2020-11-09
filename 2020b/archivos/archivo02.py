try:
    archivito = open('datos.txt','r')
except:
    print ('Error al intentar abrir el archivo')
    
#print( archivito.read() )

'''
i = 0
l = archivito.readline()
while l != '' :
    print (i,' - ',l,end='')
    i = i + 1
    l = archivito.readline()
'''

l = archivito.readlines()

i = 0
for x in l :
    print (i,'=',x, end='')
    i = i + 1

archivito.close()