from Trabajador import Trabajador
import re
# Definición de la clase Asociación con su set (validación) y get (método)
class Asalariado(Trabajador):
    """_
    Clase que representa un trabajador de tipo asalariado.

    Args:
        Trabajador (Clase): clase que representa un trabajador dentro de una asociación.
    """
    def __init__(self, sueldo_mensual=None, cargo=None, paso_seguro_social=None, isr=None, ine=None, nombre=None, fecha_ingreso=None, tipo=None, asociacion=None,proyecto=None):
        """
        Asalariado

        Args:
            sueldo_mensual (str): sueldo mensual del trabajador en una cadena de números enteros.
            cargo (str): cargo del asalariado dentro de la empresa.
            paso_seguro_social (str): porcentaje del paso de seguro social en una cadena de números enteros.
            isr (str): porcentaje de ISR aplicado al salario del trabajador en una cadena de números enteros.
            ine (str): INE del socio constituido por 5 digitos. 
            nombre (str): nombre del socio.
            fecha_ingreso (str): fecha de ingreso con formato dd/mm/aaaa.
            tipo (str): trabajador tipo asalariado.
            asociacion (str): asociación a la que pertenece el trabajador.
        """
        super().__init__(ine=ine,nombre=nombre,fecha_ingreso=fecha_ingreso, tipo=tipo, asociacion=asociacion, proyecto=proyecto)
        self.sueldo_mensual = sueldo_mensual
        self.cargo = cargo
        self.paso_seguro_social = paso_seguro_social
        self.isr = isr
        self.tipo = "Asalariado"

    def set_sueldo_mensual(self, sueldo_mensual):
        """
        Establece el sueldo mensual del trabajador.

        Args:
            sueldo_mensual (str): sueldo mensual del trabajador en una cadena de números enteros.

        """
        while True:
            pattern = r'^\s*[0-9]+\s*$'
            matches = re.match(pattern, sueldo_mensual)
            if matches:
                self.sueldo_mensual = sueldo_mensual
                break
            else:
                print('Error! caracteres no válidos, ingresa nuevamente')
                sueldo_mensual = input('Sueldo (Valores enteros): ')

    def get_sueldo_mensual(self):
        """
        Obtiene el sueldo mensual del trabajador.

        Returns:
            str: sueldo mensual del trabajador.

        """
        return self.sueldo_mensual

    def set_cargo(self, cargo):
        """
        Establece el cargo del trabajador

        Args:
            cargo (str): el cargo del trabajador
        """
        while True:
            pattern = r'^\s*([a-záéíóú]{2,},?\s*)+$'
            matches = re.match(pattern, cargo, re.IGNORECASE)
            if matches:
                self.cargo = cargo
                break
            else:
                print('Error! caracteres no válidos, ingresa nuevamente')
                cargo = input('Cargo: ')

    def get_cargo(self):
        """
        Obtiene el cargo del asalariado dentro de la empresa.

        Returns:
            str: cargo del asalariado dentro de la empresa.

        """
        return self.cargo


    def set_paso_seguro_social(self, paso_seguro_social):
        """
        Establece el porcentaje del paso de seguro social.

        Args:
            paso_seguro_social (str): porcentaje del paso de seguro social en una cadena de números enteros.

        """
        while True:
            pattern = r'^\s*[0-9]+\s*$'
            matches = re.match(pattern, paso_seguro_social)
            if matches:
                self.paso_seguro_social = paso_seguro_social
                break
            else:
                print('Error! caracteres no válidos, ingresa nuevamente')
                paso_seguro_social = input('Paso de seguro social (porcentaje entero): ')

    def get_paso_seguro_social(self):
        """
        Obtiene el porcentaje del paso de seguro social.

        Returns:
            str: porcentaje del paso de seguro social.

        """
        return self.paso_seguro_social


    def set_isr(self, isr):
        """
        Establece el porcentaje de ISR aplicado al salario del trabajador de tipo asalariado.

        Args:
            isr (str): porcentaje del ISR aplicado en una cadena de números enteros.

        """
        while True:
            pattern = r'^\s*[0-9]+\s*$'
            matches = re.match(pattern, isr)
            if matches:
                self.isr = isr
                break
            else:
                print('Error! caracteres no válidos, ingresa nuevamente')
                isr = input('ISR (porcentaje entero): ')

    def get_isr(self):
        """
        Obtiene el porcentaje de ISR aplicado al salario del trabajador de tipo asalariado.

        Returns:
            str: porcentaje del ISR.

        """
        return self.isr





