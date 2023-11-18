from Trabajador import Trabajador
import re
# Definición de la clase Asociación con su set (validación) y get (método)
class Voluntario(Trabajador):
    """
    Esta clase representa un trabajador de tipo voluntario.

    Args:
        Trabajador (Clase): clase que representa un trabajador dentro de una asociación.
    """
    def __init__(self, edad=None, profesion=None, horas=None, ine=None, nombre=None, fecha_ingreso=None, tipo=None, asociacion=None):
        """
        Voluntario

        Args:
            edad (str): edad del voluntario.
            profesion (str): profesión del voluntario.
            horas (str): horas de voluntariado.
            ine (str): INE del socio constituido por 5 digitos. 
            nombre (str): nombre del socio.
            fecha_ingreso (str): fecha de ingreso con formato dd/mm/aaaa.
            tipo (str): trabajador tipo voluntario. 
            asociacion (str): asociación a la que pertenece el trabajador.
        """
        super().__init__(ine=ine,nombre=nombre,fecha_ingreso=fecha_ingreso, tipo=tipo, asociacion=asociacion)
        self.edad = edad
        self.profesion = profesion
        self.horas = horas
        self.tipo = "Voluntario"

    # edad
    def set_edad(self, edad):
        """
        Establece la edad del voluntario.

        Args:
            edad (str): Edad del voluntario (mayor a 18 años de edad).
        """
        while True:
            pattern = r'^\s*([1][8-9]|[2-9][0-9])\s*$'
            matches = re.match(pattern, edad)
            if matches:
                self.edad = edad
                break
            else:   
                print('Error! caracteres no válidos, ingresa nuevamente') 
                edad = input('Edad (sólo número): ')
    def get_edad(self):
        """
        Obtiene la edad del voluntario.

        Returns:
            str: Edad del voluntario.
        """
        return self.edad
    
    # profesión
    def set_profesion(self, profesion):
        """
        Establece la profesión del voluntario.

        Args:
            profesion (str): Profesión del voluntario.
        """
        while True:
            pattern = r'^\s*([a-záéíóú]{2,},?\s*)+$'
            matches = re.match(pattern, profesion, re.IGNORECASE)
            if matches:
                self.profesion = profesion
                break
            else:
                print('Error! caracteres no válidos, ingresa nuevamente')
                profesion = input('Profesión: ')
    def get_profesion(self):
        """
        Obtiene la profesión del voluntario.

        Returns:
            str: Profesión del voluntario.
        """
        return self.profesion

    # horas
    def set_horas(self, horas):
        """
        Establece las horas de trabajo del voluntario.

        Args:
            horas (str): Horas de trabajo del voluntario en números enteros.
        """
        while True:
            pattern = r'^\s*[0-9]+\s*$'
            matches = re.match(pattern, horas)
            if matches:
                self.horas = horas
                break
            else:
                print('Error! caracteres no válidos, ingresa nuevamente')    
                horas = input('Horas por semana (horas enteras): ')
    def get_horas(self):
        """
        Obtiene las horas de trabajo del voluntario.

        Returns:
            str: Horas de trabajo del voluntario.
        """
        return self.horas




