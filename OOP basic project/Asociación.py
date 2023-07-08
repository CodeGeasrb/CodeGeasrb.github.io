import re
# Definición de la clase Asociación con su set (validación) y get (método)
class Asociacion():
    """ 
    Clase que representa una asociación dentro de las organizaciones no gurbenamentales.
    """
    def __init__(self, cfi=None, denominacion=None, direccion=None, provincia=None, tipo=None, declaracion=None, socios=[], trabajadores=[], proyectos=[]):
        """ 
        Asociación

        Args:
            cfi (str): CFI de la asociación, donde el primer caracter es una letra, seguido de 4 digitos.
            denominacion (str): denominación de la asociación.
            direccion (str): dirección de la asociación.
            provincia (str): provincia de la asociación.
            tipo (str): tipo de asociación.
            declaracion (str): declaración de la asociación.
            socios (list): lista que contiene los socios que pertenecen a la asociación.
            trabajadores (list): lista que contiene los trabajadores que pertenecen a la asociación.
            proyectos (list): lista que contiene los proyectos que pertenecen a la asociación.
        """
        self.cfi=cfi
        self.denominacion = denominacion
        self.direccion = direccion
        self.provincia = provincia
        self.tipo = tipo
        self.declaracion = declaracion
        self.socios = socios
        self.trabajadores = trabajadores
        self.proyectos = proyectos

    # cfi
    def set_cfi(self, cfi):
        """ 
        Establece el CFI de la asociación

        Args:
            cfi (str): CFI de la asociación (una letra seguida de cuatro dígitos)
        """
        while True:
            pattern = r'^[a-z][0-9]{4}$'
            matches = re.match(pattern, cfi, re.IGNORECASE)
            if matches:
                self.cfi = cfi
                break
            else:
                print('Error, favor de ingresar nuevamente')
                cfi = input('CFI (una letra seguido de cuatro digitos): ')
    def get_cfi(self):
        """ 
        Obtiene el CFI de la asociación

        Returns:
            str: CFI de la asociación
        """
        return self.cfi

    # denominación
    def set_denominacion(self, denominacion):
        """ 
        Establece la denominación de la asociación

        Args:
            denominacion (str): denominación de la asociación
        """
        while True:
            pattern = r'^\s*([a-záéíóú]{2,},?\s*)+$'
            matches = re.match(pattern,denominacion, re.IGNORECASE)   
            if matches:    
                self.denominacion = denominacion
                break
            else:
                print('Error, favor de ingresar nuevamente')
                denominacion = input('Denominación: ')
    def get_denominacion(self):
        """ 
        Obtiene la denominación de la asociación

        Returns:
            str: denominación de la asociación
        """
        return self.denominacion

    # direccion
    def set_direccion(self, direccion):
        """
        Establece la dirección de la asociación.

        Args:
            direccion (str): La dirección de la asociación.
        """
        while True:
            pattern = r'^\s*([a-záéíóú0-9.]{2,},?\s*)+$'
            matches = re.match(pattern, direccion, re.IGNORECASE)
            if matches:
                self.direccion = direccion
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente.')
                direccion = input('Dirección: ')

    def get_direccion(self):
        """
        Obtiene la dirección de la asociación.

        Returns:
            str: La dirección de la asociación.
        """
        return self.direccion

    # provincia
    def set_provincia(self, provincia):
        """
        Establece la provincia de la asociación.

        Args:
            provincia (str): La provincia de la asociación.
        """
        while True:
            pattern = r'^\s*([a-záéíóú]{2,},?\s*)+$'
            matches = re.match(pattern, provincia, re.IGNORECASE)
            if matches:
                self.provincia = provincia
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente.')
                provincia = input('Provincia: ')

    def get_provincia(self):
        """
        Obtiene la provincia de la asociación.

        Returns:
            str: La provincia de la asociación.
        """
        return self.provincia

    # tipo
    def set_tipo(self, tipo):
        """
        Establece el tipo de la asociación.

        Args:
            tipo (str): El tipo de la asociación.
        """
        while True:
            pattern = r'^\s*([a-záéíóú]{2,},?\s*)+$'
            matches = re.match(pattern, tipo, re.IGNORECASE)
            if matches:
                self.tipo = tipo
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente.')
                tipo = input('Tipo: ')

    def get_tipo(self):
        """
        Obtiene el tipo de la asociación.

        Returns:
            str: El tipo de la asociación.
        """
        return self.tipo

    # declaracion
    def set_declaracion(self, declaracion):
        """
        Establece la declaración de la asociación.

        Args:
            declaracion (str): La declaración de la asociación.
        """
        while True:
            pattern = r'^\s*([a-záéíóú]{2,},?\s*)+$'
            matches = re.match(pattern, declaracion, re.IGNORECASE)
            if matches:
                self.declaracion = declaracion
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente.')
                declaracion = input('Declaración: ')

    def get_declaracion(self):
        """
        Obtiene la declaración de la asociación.

        Returns:
            str: La declaración de la asociación.
        """
        return self.declaracion

    # socios
    def set_socios(self, socios):
        """
        Establece la lista de socios de la asociación

        Args:
            socios (list): Lista de socios de la asociación
        """
        if isinstance(socios, list):
            self.socios = socios
        else:
            print('Error en la lista de socios!, favor de ingresar nuevamente')
    def get_socios(self):
        """
        Obtiene la lista de socios de la asociación

        Returns:
            list: Lista de socios de la asociación
        """
        return self.socios
    
    # trabajadores
    def set_trabajadores(self, trabajadores):
        """
        Establece la lista de trabajadores de la asociación

        Args:
            trabajadores (list): Lista de trabajadores de la asociación
        """
        if isinstance(trabajadores, list):
            self.trabajadores = trabajadores
        else:
            print('Error en la lista de socios!, favor de ingresar nuevamente')
    def get_trabajadores(self):
        """
        Obtiene lista de trabajadores de la asociación

        Returns:
            list: Lista de trabajadores de la asociación
        """
        return self.trabajadores
    
    # proyectos
    def set_proyectos(self, proyectos):
        """
        Establece la lista de proyectos de la asociación

        Args:
            proyectos (list): Lista de proyectos de la asociación
        """
        if isinstance(proyectos, list):
            self.proyectos = proyectos
        else:
            print('Error en la lista de socios!, favor de ingresar nuevamente')
    def get_proyectos(self):
        """
        Obtiene la lista de proyectos de la asociación

        Returns:
            list: Lista de proyectos de la asociación
        """
        return self.proyectos








