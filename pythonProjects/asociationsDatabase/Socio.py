import re
# Definición de la clase Asociación con su set (validación) y get (método)
class Socio():
    """ 
    Clase que representa un socio de una determinada asociación.
    """
    def __init__(self, ine=None, nombre=None, direccion=None, provincia=None, fecha_alta=None, cuota_mensual=None,aportacion_anual = None, asociacion=None):
        """ 
        Socio

        Args:
            ine (str): INE del socio constituido por 5 digitos.
            nombre (str): nombre del socio.
            direccion (str): dirección del socio.
            provincia (str): provincia donde reside el socio.
            fecha_alta (str): fecha con formato dd/mm/aaaa.
            cuota_mensual (str): Digito entero.
            aportacion_anual (str): digito obtenido de multiplicar la cuota mensual por doce meses.
            asociacion (str): asociación de la cual es socio.
        """
        self.ine = ine
        self.nombre = nombre
        self.direccion = direccion
        self.provincia = provincia
        self.fecha_alta = fecha_alta
        self.cuota_mensual = cuota_mensual
        self.asociacion = asociacion
    # ine
    def set_ine(self, ine):
        """
        Establece el número de identificación electoral (INE) del miembro.

        Args:
            ine (str): El número de INE del miembro (5 dígitos).
        """
        while True:
            pattern = r'^\s*([0-9]{5})\s*$'
            matches = re.match(pattern, ine, re.IGNORECASE)
            if matches:
                self.ine = ine
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente.')
                ine = input('INE (5 dígitos): ')

    def get_ine(self):
        """
        Obtiene el número de identificación electoral (INE) del miembro.

        Returns:
            str: El número de INE del miembro.
        """
        return self.ine

    # nombre
    def set_nombre(self, nombre):
        """
        Establece el nombre del miembro.

        Args:
            nombre (str): El nombre del miembro.
        """
        while True:
            pattern = r'^\s*([a-záéíóú]{2,}\s*)+$'
            matches = re.match(pattern, nombre, re.IGNORECASE)
            if matches:
                self.nombre = nombre
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente.')
                nombre = input('Nombre: ')

    def get_nombre(self):
        """
        Obtiene el nombre del miembro.

        Returns:
            str: El nombre del miembro.
        """
        return self.nombre

    # direccion
    def set_direccion(self, direccion):
        """
        Establece la dirección del miembro.

        Args:
            direccion (str): La dirección del miembro.
        """
        while True:
            pattern = r'^\s*([a-záéíóú0-9.,]{2,},?\s*)+$'
            matches = re.match(pattern, direccion, re.IGNORECASE)
            if matches:
                self.direccion = direccion
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente.')
                direccion = input('Dirección: ')

    def get_direccion(self):
        """
        Obtiene la dirección del miembro.

        Returns:
            str: La dirección del miembro.
        """
        return self.direccion

    # provincia
    def set_provincia(self, provincia):
        """
        Establece la provincia del miembro.

        Args:
            provincia (str): La provincia del miembro.
        """
        while True:
            pattern = r'^\s*([a-záéíóú0-9]{2,},?\s*)+$'
            matches = re.match(pattern, provincia, re.IGNORECASE)
            if matches:
                self.provincia = provincia
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente.')
                provincia = input('Provincia: ')

    def get_provincia(self):
        """
        Obtiene la provincia del miembro.

        Returns:
            str: La provincia del miembro.
        """
        return self.provincia

    # fecha de alta
    def set_fecha_alta(self, fecha_alta):
        """
        Establece la fecha de alta del miembro.

        Args:
            fecha_alta (str): La fecha de alta del miembro en el formato dd/mm/aaaa.
        """
        while True:
            pattern = r'^\s*([0][1-9]|[1-2][0-9]|[3][0-1])/([0][1-9]|[1][0-2])/[2][0][0-9][0-9]\s*$'
            matches = re.match(pattern, fecha_alta)
            if matches:
                self.fecha_alta = fecha_alta
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente.')
                fecha_alta = input('Fecha de alta (dd/mm/aaaa): ')

    def get_fecha_alta(self):
        """
        Obtiene la fecha de alta del miembro.

        Returns:
            str: La fecha de alta del miembro en el formato dd/mm/aaaa.
        """
        return self.fecha_alta

    # cuota_mensual
    def set_cuota_mensual(self, cuota_mensual):
        """
        Establece la cuota mensual del miembro y calcula la aportación anual.

        Args:
            cuota_mensual (str): La cuota mensual del miembro (valor entero).
        """
        while True:
            pattern = r'^\s*[0-9]+\s*$'
            matches = re.match(pattern, cuota_mensual)
            if matches:
                self.cuota_mensual = cuota_mensual
                self.aportacion_anual = int(cuota_mensual) * 12
                break
            else:
                print('Error! Caracteres no válidos, ingresa nuevamente.')
                cuota_mensual = input('Cuota mensual (valores enteros): ')

    def get_cuota_mensual(self):
        """
        Obtiene la cuota mensual del miembro.

        Returns:
            str: La cuota mensual del miembro.
        """
        return self.cuota_mensual

    # asociacion
    def set_asociacion(self, asociacion):
        """
        Establece la asociación del miembro.

        Args:
            asociacion (str): La asociación del miembro en formato CFI (una letra seguida de cuatro dígitos).
        """
        while True:
            pattern = r'^[a-z][0-9]{4}$'
            matches = re.match(pattern, asociacion, re.IGNORECASE)
            if matches:
                self.asociacion = asociacion
                break
            else:
                print('Error! Favor de ingresar nuevamente.')
                asociacion = input('CFI (una letra seguida de cuatro dígitos): ')

    def get_asociacion(self):
        """
        Obtiene la asociación del miembro.

        Returns:
            str: La asociación del miembro.
        """
        return self.asociacion

        






