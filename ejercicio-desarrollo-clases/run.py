#Se importa las clases que usamos
from paquete_archivo.archivos import *
from paquete_modelo.modelo import *

#Creamos dos objetos
m = MiArchivo()
m2 = MiArchivoEscribir()

#Lista separada con |
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]
#p= Persona(lista[1][1], lista[1][2],lista[1][3],lista[1][0])
for d in lista:
    # print(d)
    p = Persona(d[0],d[1], d[2], d[3])
    m2.agregar_informacion(p)
    #p = Persona(d[1], d[2], d[3], d[0])
    print(p)
#Cierra el archivo
m.cerrar_archivo()
m2.cerrar_archivo()
