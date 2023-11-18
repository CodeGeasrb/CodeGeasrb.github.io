import re, datetime
# Definición de la clase Asociación con su set (validación) y get (método)
class Trabajador():
    """
    Clase que representa un trabajador de una asociación determinada
    """
    def __init__(self, ine=None, nombre=None, fecha_ingreso=None, tipo=None, asociacion=None, proyecto = None):
        """
        Trabajador

        Args:
            ine (str): INE del socio constituido por 5 digitos. 
            nombre (str): nombre del socio.
            fecha_ingreso (str): fecha de ingreso con formato dd/mm/aaaa.
            tipo (str): tipo de trabajador (asalariado o voluntario). 
            asociacion (str): asociación a la que pertenece el trabajador.
            proyecto (str): ID único de proyecto asignado al trabajador de 13 digitos.
        """
        self.ine = ine
        self.nombre = nombre
        self.fecha_ingreso = fecha_ingreso
        self.tipo = tipo
        self.asociacion = asociacion
        self.proyecto = proyecto
 
   # ine
    def set_ine(self, ine):
        """Establece el número de INE del trabajador.

        Args:
            ine (str): El número de INE del trabajador (5 dígitos).
        """
        while True:
            pattern = r'^\s*([0-9]{5})\s*$'
            matches = re.match(pattern, ine)
            if matches:
                self.ine = ine
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente')
                ine = input('INE (5 dígitos): ')

    def get_ine(self):
        """
        Obtiene el número de INE del trabajador.

        Returns:
            str: El número de INE del trabajador.
        """
        return self.ine

    # denominación
    def set_nombre(self, nombre):
        """Establece el nombre del trabajador.

        Args:
            nombre (str): El nombre del trabajador.
        """
        while True:
            pattern= r'^\s*([a-záéíóú]{2,}\s*)+$'
            matches = re.match(pattern, nombre, re.IGNORECASE)
            if matches:
                self.nombre = nombre
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente')
                nombre = input('Nombre: ')

    def get_nombre(self):
        """
        Obtiene el nombre del trabajador.

        Returns:
            str: El nombre del trabajador.
        """
        return self.nombre

    # fecha_ingreso
    def set_fecha_ingreso(self, fecha_ingreso):
        """
        Establece la fecha de ingreso del trabajador.

        Args:
            fecha_ingreso (str): La fecha de ingreso del trabajador en el formato dd/mm/aaaa.
        """
        while True:
            pattern = r'^\s*([0][1-9]|[1-2][0-9]|[3][0-1])/([0][1-9]|[1][0-2])/[2][0][0-9][0-9]\s*$'
            matches = re.match(pattern, fecha_ingreso, re.IGNORECASE)
            if matches:
                self.fecha_ingreso = fecha_ingreso
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente')
                fecha_ingreso = input('Fecha de ingreso (dd/mm/aaaa): ')

    def get_fecha_ingreso(self):
        """
        Obtiene la fecha de ingreso del trabajador.

        Returns:
            str: La fecha de ingreso del trabajador en el formato dd/mm/aaaa.
        """
        return self.fecha_ingreso

    # tipo
    def set_tipo(self, tipo):
        """Establece el tipo de trabajador.

        Args:
            tipo (str): El tipo de trabajador (asalariado o voluntario).
        """
        self.tipo = tipo

    def get_tipo(self):
        """
        Obtiene el tipo de trabajador.

        Returns:
            str: El tipo de trabajador (asalariado o voluntario).
        """
        return self.tipo

    # asociacion
    def set_asociacion(self, asociacion):
        """
        Establece la asociación a la que pertenece el trabajador

        Args:
            asociacion (str): La asociación a la que pertenece el trabajador
        """
        while True:
            pattern = r'^[a-z][0-9]{4}$'
            matches = re.match(pattern, asociacion, re.IGNORECASE)
            if matches:
                self.asociacion = asociacion
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente')
                asociacion = input('CFI (una letra y cuatro digitos): ')
    def get_asociacion(self):
        """
        Obtiene la asociación a la que pertenece el trabajador

        Returns:
            str: La asociación a la que pertenece el trabajado
        """
        return self.asociacion

    # proyecto asignado
    def set_proyecto(self, proyecto):
        """
        Establece el ID del proyecto asignado al trabajador.

        Args:
            proyecto (str): Proyecto asignado al trabajador.
        """
        while True:
            pattern = r'^([0-9]{13})$'
            matches = re.match(pattern, proyecto)
            if matches:
                self.proyecto = proyecto
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente')
                proyecto = input('ID (13 dígitos): ')
    def get_proyecto(self):
        """
        Obtiene el ID del proyecto asignado al trabajador.

        Returns:
            str: Proyecto asignado al trabajador.
        """
        return self.proyecto

    





