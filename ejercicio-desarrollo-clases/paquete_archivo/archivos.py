
import codecs

class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        # Le damos la direccion del archivo donde se encuentra la informacion
        self.archivo = codecs.open("data/informacion.csv", "r")

    #Leemos el archivo 
    def obtener_informacion(self):
        return self.archivo.readlines()
    #Este metodo cierra el archivo
    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:
    def cerrar_archivo(self):
       self.archivo.close()
    """
    """
    #Constructor
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/segunda_informacion.csv", "a")
        #self.archivo.white("%s|%s\n"%("alumno","Promedio"))
    #Metodo para editar archivo
    def agregar_informacion(self, p):
        self.archivo.write("Nombre del alumno: %s - Promedio: %f\n" % (p.nombre, p.promedio())
    #Metodo para cerrar archivo
    
