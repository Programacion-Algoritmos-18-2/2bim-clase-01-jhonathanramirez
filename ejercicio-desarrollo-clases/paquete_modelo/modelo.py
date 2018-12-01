"""
    creación de clases
"""

class Persona(object):
    """
    """
    #Constructor
    def __init__(self, n, nota1, nota2, nota3):
        """
        """
        self.nombre = n
        self.notas = float(nota1)
        self.notas2 = float(nota2)
        self.notas3 = float(nota3)
    # Metodos get y set
    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_notas(self, nota1):
        """
        """
        self.notas = float(nota1)

    def obtener_notas(self):
        """
        """
        return self.notas
    
    def agregar_notas2(self, nota2):
        """
        """
        self.notas2 = float(nota2)

    def obtener_notas2(self):
        """
        """
        return self.notas2
    
    def agregar_notas3(self, nota3):
        """
        """
        self.notas3 = float(nota3)
    
    def obtener_notas3(self):
        """
        """
        return self.notas3
    # Calculo de promedio
    def promedio(self):
        promedio = (self.notas1 + self.notas2 +self.notas3)/3
        return promedio

    
    def __str__(self):
        """
        """
        return "Nombre del alumno: %s - Promedio: %f\n" % (self.nombre, self.promedio())
