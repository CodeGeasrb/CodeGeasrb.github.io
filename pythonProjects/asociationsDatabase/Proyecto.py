import re, datetime
# Definición de la clase Asociación con su set (validación) y get (método)
class Proyecto():
    """
    Clase que representa un proyecto implmentado en una asociación.
    """
    def __init__(self,ide=None, pais=None, zona=None, objetivo=None, num_benef=None,asociacion = None, proyecto_padre=None, sub_proyectos=[], trabajadores = []):
        """
        Proyecto

        Args:
            ide (str): ID único del proyecto generado como cadena de texto de 13 digitos.
            pais (str): país donde se desarrolla el proyecto.
            zona (str): zona deel país donde se desarrolla el proyecto.
            objetivo (str): objetivo general del proyecto.
            num_benef (str): número de beneficiarios del proyecto en una cadena de texto de números enteros.
            proyecto_padre (str): ID del proyecto padre como una cadena de texto de 13 digitos.
            sub_proyectos (list): lista que contiene los IDs de los subproyectos que dependen de un proyecto padre.
            trabajadores (list): lista que contiene las INEs de los trabajadores del proyecto.
        """
        self.pais = pais
        self.zona = zona
        self.objetivo = objetivo
        self.num_benef = num_benef
        self.asociacion = asociacion
        self.proyecto_padre = proyecto_padre
        self.sub_proyectos = sub_proyectos
        self.trabajadores = trabajadores
        self.ide = ide
    
    # denominación
    def set_pais(self, pais):
        """
        Establece el país en que se desarrolla el proyecto.

        Args:
            pais (str): País en el que se desarrolla el proyecto.
        """
        while True:
            pattern = r'^\s*([a-záéíóú]{2,},?\s*)+$'
            matches = re.match(pattern, pais, re.IGNORECASE)
            if matches:
                self.pais = pais
                break
            else:
                print('Error! caracteres no válidos, ingresa nuevamente')
                pais = input('País: ')
    def get_pais(self):
        """
        Obtiene el pais en el que se desarrolla el proyecto.

        Returns:
            str: País en el que se desarrolla el proyecto.
        """
        return self.pais

    # zona
    def set_zona(self, zona):
        """
        Establece la zona en del país en la que se desarrolla el proyecto.

        Args:
            zona (str): Zona del país en la que se desarrolla el proyecto.
        """
        while True:
            pattern = r'^\s*([a-záéíóú]{2,},?\s*)+$'
            matches = re.match(pattern, zona, re.IGNORECASE)
            if matches:
                self.zona = zona
                break
            else:
                print('Error! caracteres no válidos, ingresa nuevamente')
                zona = input('Zona: ')
    def get_zona(self):
        """
        Obtiene la zona del país en la que se desarrolla el proyecto.

        Returns:
            str: Zona del país en la que se desarrolla el proyecto.
        """
        return self.zona

    # objetivo
    def set_objetivo(self, objetivo):
        """
        Establece el objetivo del proyecto.

        Args:
            objetivo (str): Objetivo del proyecto.
        """
        while True:
            pattern = r'^\s*([a-záéíóú]{2,},?\s*)+$'
            matches = re.match(pattern, objetivo, re.IGNORECASE)
            if matches:
                self.objetivo = objetivo
                break
            else:
                print('Error! caracteres no válidos, ingresa nuevamente')
                objetivo = input('Objetivo: ')
    def get_objetivo(self):
        """
        Obtiene el objetivo del proyecto.

        Returns:
            str: Objetivo del proyecto.
        """
        return self.objetivo

    # num_benef
    def set_num_benef(self, num_benef):
        """
        Establece el número de beneficiarios del proyecto.

        Args:
            num_benef (str): Número de beneficiarios del proyecto en una cadena de texto de números enteros.
        """
        while True:
            pattern = r'^\s*[0-9]+\s*$'
            matches = re.match(pattern, num_benef)
            if matches:
                self.num_benef = num_benef
                break
            else:
                print('Error! caracteres no válidos, ingresa nuevamente')
                num_benef = input('Número de beneficiarios del proyecto: ') 
    def get_num_benef(self):
        """
        Obtiene el número de beneficiarios del proyecto.

        Returns:
            str: Número de beneficiarios del proyecto.
        """
        return self.num_benef


    # asociacion
    def set_asociacion(self, asociacion):
        """
        Establece la asociación a la que pertenece el proyecto.

        Args:
            asociación (str): asociación a la que pertenece el proyecto.
        """
        while True:
            pattern = r'^[a-z][0-9]{4}$'
            matches = re.match(pattern, asociacion, re.IGNORECASE)
            if matches:
                self.asociacion = asociacion
                break
            else:
                print('Error, favor de ingresar nuevamente')
                asociacion = input('CFI (una letra y cuatro digitos): ')
    def get_asociacion(self):
        """
        Obtiene la asociación a la que pertebece el proyecto.

        Returns:
            str: Asociación a la que pertenece el proyecto.
        """
        return self.asociacion
    

    # sub_proyectos
    def set_sub_proyectos(self, sub_proyectos):
        """
        Establece la lista de IDs de subproyectos vinculados a un proyecto.

        Args:
            sub_proyectos (list): Lista de IDs (13 digitos) de subproyectos.
        """
        if isinstance(sub_proyectos, list):
            self.sub_proyectos = sub_proyectos
            #self.sub_proyectos.extend(sub_proyectos)
        else:
            print('Error en la lista de subproyectos!, favor de ingresar nuevamente')
    def get_sub_proyectos(self):
        """
        Obtiene la lista de IDs de subproyectos vinculados a un proyecto.

        Returns:
            list: Lista de IDs de subproyectos.
        """
        return self.sub_proyectos

    # proyecto_padre
    def set_proyecto_padre(self, proyecto_padre):
        """
        Establece el ID del proyecto padre en caso de que se defina un subproyecto.

        Args:
            proyecto_padre (str): ID de proyecto padre.
        """
        while True:
            pattern = r'^([0-9]{13})$'
            matches = re.match(pattern, proyecto_padre)
            if matches:
                self.proyecto = proyecto_padre
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente')
                proyecto_padre = input('ID (13 dígitos): ')
    def get_proyecto_padre(self):
        """
        Obtiene el ID del proyecto padre en caso de que se defina un subproyecto.

        Returns:
            str: Proyecto padre.
        """
        return self.proyecto_padre
    
    # trabajadores
    def set_trabajadores(self, trabajadores):
        """
        Establece la lista de INEs de los trabajadores vinculados al proyecto.

        Args:
            trabajadores (str): Lista de las INEs de los trabajadores vinculados al proyecto.
        """
        if isinstance(trabajadores, list):
            self.trabajadores = trabajadores
        else:
            print('Error en la lista de trabajadores!, favor de ingresar nuevamente')
    def get_trabajadores(self):
        """
        Obtiene la lista de INEs de los trabajadores vinculados al proyecto.

        Returns:
            str: Lista de INEs de los trabajadores del proyecto.
        """
        return self.trabajadores
    
    # ID
    def set_ide(self, ide):
        """
        Establece el ID único del proyecto.

        Args:
            ide (str): ID único de 13 digitos generado automáticamente con Timestamp.
        """
        ide = str(int(datetime.datetime.now().timestamp()*1000))
        self.ide = ide
    def get_ide(self):
        """
        Obtiene el ID del proyecto.

        Returns:
            str: ID del proyecto.
        """
        return self.ide
    


    

