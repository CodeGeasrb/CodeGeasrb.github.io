import pickle, os, data_base
from Asociación import Asociacion
from Socio import Socio
from Asalariado import Asalariado
from Voluntario import Voluntario
from Proyecto import Proyecto
class Gestor():
    """
    Clase Gestor que mantiene un control sobre la lógica y ejecución el programa.
    """
    def __init__(self, asociaciones=[], socios=[], asalariados=[], voluntarios=[],proyectos=[]):
        """
        Gestor

        Args:
            asociaciones (list): lista de asociaciones no gubernamentales.
            socios (list): lista de los socios.
            asalariados (list): lista de trabajadores tipo asalariado.
            voluntarios (list): lista de trabajadores tipo voluntario.
            proyectos (list): lista de proyectos.
        """
        self.asociaciones = asociaciones
        self.socios = socios
        self.asalariados = asalariados
        self.voluntarios = voluntarios
        self.proyectos = proyectos
        self.archivos = {"ASOCIACIONES.dat":self.asociaciones,"SOCIOS.dat":self.socios,"ASALARIADOS.dat":self.asalariados,"VOLUNTARIOS.dat":self.voluntarios,"PROYECTOS.dat":self.proyectos}
        self.clases = {Asociacion:self.asociaciones, Socio:self.socios, Asalariado:self.asalariados, Voluntario:self.voluntarios, Proyecto:self.proyectos}

    def Bienvenida(self):
        """
        Método que imprime el mensaje de bienvenida del programa.
        """
        os.system("cls")
        print("Bienvenido a la base de datos de las organizaciones no gubernamentales ONGs")
        input("Oprima Enter o ingrese cualquier tecla para avanzar: ")

    def MenuPrimario(self):
        """
        Método que imprimme el menú principal del programa.
        """
        print('**********************')
        print('**  MENÚ PRINCIPAL  **')
        print('**********************')
        menu = ["Crear",'Consultar', 'Actualizar','Borrar','Guardar','Salir']
        for number, message in enumerate(menu, start=1):
            print(f'{number}. {message}')

    def MenuSecundario(self):
        menu = ["Asociación",'Socio', 'Asalariado','Voluntario','Proyecto','Regresar']
        for number, message in enumerate(menu, start=1):
            print(f'{number}. {message}')

    def Cargar(self):
        """
        Método que permite crear archivos que contienen una lista de objetos creados de cada clase, o en caso de que ya existan los archivos, poder cargar los objetos en las listas correspondientes. 
        """
        for archivo in self.archivos.keys():
            if os.path.exists(archivo):
                with open(archivo, "rb") as f:
                    while True:
                        try:
                            lista_objetos = pickle.load(f)
                        except EOFError:
                            break
                        for objeto in lista_objetos:
                            for tipo, lista in self.clases.items():
                                if isinstance(objeto,tipo):
                                    lista.append(objeto)
                                    break
            else:
                data_base.DataBase()

    def Crear(self):
        """
        Método que permite crear nuevos objetos de cualquier clase y establecer el valor de sus atributos.
        """
        while True:
            print('**********************')
            print('**      CREAR       **')
            print('**********************')
            self.MenuSecundario()
            print('')
            option_crear = input('¿Que desea crear?: ')
        # 1. Asociación crear e ingresar sus atributos
            if option_crear == '1':
                os.system("cls")
                print('NUEVA ASOCIACIÓN\n')
                new_asoc = Asociacion()
                while True:
                    cfi = input('CFI (una letra seguido de cuatro digitos): ')
                    cfi_exists = any(asoc.get_cfi() == cfi for asoc in self.asociaciones)
                    if not cfi_exists:
                        new_asoc.set_cfi(cfi)
                        break
                    else:
                        print('El CFI ya está siendo utilizado en otra asociación. Inténtelo nuevamente.')
                new_asoc.set_denominacion(input('Denominación: '))
                new_asoc.set_direccion(input('Dirección: '))
                new_asoc.set_provincia(input('Provincia: '))
                new_asoc.set_tipo(input('Tipo: '))
                new_asoc.set_declaracion(input('Declaración: '))    
                self.asociaciones.append(new_asoc)
                os.system("cls")
                print('ÉXITO! asociación creada correctamente')
                continue
        # 2. Socio, crear y agregar sus atributos
            if option_crear == '2':
                os.system("cls")
                print('NUEVO SOCIO\n')
                new_soc = Socio()
                while True:
                    ine = input('INE (5 digitos): ')
                    ine_exists_soc = any(soc.get_ine() == ine for soc in self.socios)
                    ine_exist_asal = any(asal.get_ine() == ine for asal in self.asalariados)
                    ine_exist_vol  = any(vol.get_ine() == ine for vol in self.voluntarios)
                    if not ine_exists_soc and not ine_exist_asal and not ine_exist_vol:
                        new_soc.set_ine(ine)
                        break
                    else:
                        print('La INE ingresada ya fue registrada anteriormente. Inténtelo nuevamente.')
                new_soc.set_nombre(input('Nombre: '))
                new_soc.set_direccion(input('Dirección: '))
                new_soc.set_provincia(input('Provincia: '))
                new_soc.set_fecha_alta(input('Fecha de alta (dd/mm/aaaa): '))
                new_soc.set_cuota_mensual(input('Cuota mensual (valores enteros): '))
                print('Ingrese el CFI de la asociación a la que pertenece el socio o "s" para salir')
                while True:
                    cfi = input('CFI (una letra seguido de cuatro digitos): ')
                    cfi_exists = any(asoc.get_cfi() == cfi for asoc in self.asociaciones)
                    if cfi_exists:
                        new_soc.set_asociacion(cfi)
                        for asoc in self.asociaciones:
                            if asoc.get_cfi() == cfi:
                                asoc.get_socios().append(new_soc.get_ine())
                        break
                    elif cfi.lower() == 's':
                        break
                    else:
                        print('El CFI ingresado no se encuentra vinculado a alguno existente. Inténtelo nuevamente.')
                        continue
                self.socios.append(new_soc)
                os.system("cls")
                print('ÉXITO! socio creado correctamente')
                continue
        # 3. asalariados, crear e ingresar atributos
            if option_crear == '3':
                os.system("cls")
                print('NUEVO TRABAJADOR TIPO ASALARIADO\n')
                new_asal = Asalariado()
                while True:
                    ine = input('INE (5 digitos): ')
                    ine_exists_asal = any(asal.get_ine() == ine for asal in self.asalariados)
                    ine_exist_soc = any(soc.get_ine() == ine for soc in self.socios)
                    if not ine_exists_asal and not ine_exist_soc:
                        new_asal.set_ine(ine)
                        break
                    else:
                        print('La INE ingresada ya fue registrada anteriormente. Inténtelo nuevamente.')
                new_asal.set_nombre(input('Nombre: '))
                new_asal.set_fecha_ingreso(input('Fecha de ingreso (dd/mm/aaaa): '))
                new_asal.set_sueldo_mensual(input('Sueldo mensual (valores enteros): '))
                new_asal.set_cargo(input('Cargo: '))
                new_asal.set_paso_seguro_social(input('Paso de seguro social (porcentaje entero): '))
                new_asal.set_isr(input('ISR (porcentaje entero): '))
                print('Ingrese el CFI de la asociación a la que pertenece el trabajador  o "s" para salir')
                while True:
                    cfi = input('CFI (una letra seguido de cuatro digitos): ')
                    cfi_exists = any(asoc.get_cfi() == cfi for asoc in self.asociaciones)
                    if cfi_exists:
                        new_asal.set_asociacion(cfi)
                        for asoc in self.asociaciones:
                            if asoc.get_cfi() == cfi:
                                asoc.get_trabajadores().append(new_asal.get_ine())
                        break
                    elif cfi.lower() == 's':
                        break
                    else:
                        print('El CFI ingresado no se encuentra vinculado a alguna asociación existente. Inténtelo nuevamente.')
                print('Ingrese el ID del proyecto asignado al trabajador o "s" para salir')
                while True:
                    ide = input('ID (13 digitos): ')
                    ide_exist = any(proj.get_ide()== ide and proj.get_asociacion() == new_asal.get_asociacion() for proj in self.proyectos)
                    if ide_exist:
                        new_asal.set_proyecto(ide)
                        for proj in self.proyectos:
                            if proj.get_ide() == ide:
                                proj.get_trabajadores().append(new_asal.get_ine())
                        break
                    elif ide.lower() == 's':
                        break
                    else:
                        print('ERROR!, proyecto no existente o no pertenece a la misma asociación que el trabajador. Inténtelo nuevamente.')
                self.asalariados.append(new_asal)
                os.system("cls")
                print('ÉXITO! asalariado creado correctamente')
                continue
        # 4. voluntarios, crear, ingresar atributos y añadir a la lista de voluntarios
            if option_crear == '4':
                os.system("cls")
                print('NUEVO TRABAJADOR TIPO VOLUNTARIO\n')
                new_vol = Voluntario()
                while True:
                    ine = input('INE (5 digitos): ')
                    ine_exists_asal = any(vol.get_ine() == ine for vol in self.voluntarios)
                    ine_exist_soc = any(soc.get_ine() == ine for soc in self.socios)
                    if not ine_exists_asal and not ine_exist_soc:
                        new_vol.set_ine(ine)
                        break
                    else:
                        print('La INE ingresada ya fue registrada anteriormente. Inténtelo nuevamente.')
                new_vol.set_nombre(input('Nombre: '))
                new_vol.set_fecha_ingreso(input('Fecha de ingreso (dd/mm/aaaa): '))
                new_vol.set_edad(input('Edad (sólo número): '))
                new_vol.set_profesion(input('Profesión: '))
                new_vol.set_horas(input('Horas por semana (horas enteras): '))
                print('Ingrese el CFI de la asociación a la que pertenece el trabajador  o "s" para salir')
                while True:
                    cfi = input('CFI (una letra seguido de cuatro digitos): ')
                    cfi_exists = any(asoc.get_cfi() == cfi for asoc in self.asociaciones)
                    if cfi_exists:
                        new_vol.set_asociacion(cfi)
                        for asoc in self.asociaciones:
                            if asoc.get_cfi() == cfi:
                                asoc.get_trabajadores().append(new_vol.get_ine())
                        break
                    elif cfi.lower() == 's':
                        break
                    else:
                        print('El CFI ingresado no se encuentra vinculado a alguna asociación existente. Inténtelo nuevamente.')
                print('Ingrese el ID del proyecto asignado al trabajador o "s" para salir')
                while True:
                    ide = input('ID (13 digitos): ')
                    ide_exist = any(proj.get_ide()== ide and proj.get_asociacion() == new_vol.get_asociacion() for proj in self.proyectos)
                    if ide_exist:
                        new_vol.set_proyecto(ide)
                        for proj in self.proyectos:
                            if proj.get_ide() == ide:
                                proj.get_trabajadores().append(new_vol.get_ine())
                        break
                    elif ide.lower() == 's':
                        break
                    else:
                        print('ERROR!, proyecto no existente o no pertenece a la misma asociación que el trabajador. Inténtelo nuevamente.')
                self.voluntarios.append(new_vol)
                os.system("cls")
                print('ÉXITO! voluntario creado correctamente')
                continue
            # 5. proyectos, crear e ingresar atributos
            if option_crear =='5':
                os.system("cls")
                print('NUEVO PROYECTO\n')
                new_proj = Proyecto()
                new_proj.set_ide(id) 
                new_proj.set_pais(input('País: '))
                new_proj.set_zona(input('Zona: '))
                new_proj.set_objetivo(input('Objetivo: '))
                new_proj.set_num_benef(input('Número de beneficiarios del proyecto (sólo números enteros): '))
                print('Ingrese el CFI de la asociación a la que pertenece el proyecto o "s" para salir')
                while True:
                    cfi = input('CFI (una letra seguido de cuatro digitos): ')
                    cfi_exists = any(asoc.get_cfi() == cfi for asoc in self.asociaciones)
                    if cfi_exists:
                        new_proj.set_asociacion(cfi)
                        for asoc in self.asociaciones:
                            if asoc.get_cfi() == cfi:
                                asoc.get_proyectos().append(new_proj.get_ide())
                        break
                    elif cfi.lower() == 's':
                        break
                    else:
                        print('El CFI ingresado no se encuentra vinculado a algún proyecto existente. Inténtelo nuevamente.')
                        continue      
                print('Ingrese el ID del proyecto padre o "s" para salir')
                while True:
                    ide = input('ID (13 digitos): ')
                    ide_exist = any(proj.get_ide() == ide for proj in self.proyectos)
                    if ide_exist:
                        for proj in self.proyectos:
                            if proj.get_ide() == ide:
                                new_proj.set_proyecto_padre(ide)
                                proj.set_sub_proyectos([new_proj.get_ide()])
                                break
                        break
                    if ide.lower() == 's':
                        break
                    else:
                        print('El ID ingresado no se encuentra vinculado a algún proyecto  existente. Inténtelo nuevamente.')
                self.proyectos.append(new_proj)
                os.system("cls")
                print('ÉXITO! proyecto creado correctamente')
                continue
            # 6. Regresar
            if option_crear == '6':
                break
            else:
                os.system("cls")
                print('ERROR!, seleccione una opción válida para continuar')
                continue

    def Consultar(self):
        """
        Método que permite consultar los valores actuales de los atributos de los cualquier objeto de cualquier clase.
        """
        while True:
            print('**********************')
            print('**     Consultar    **')
            print('**********************')
            self.MenuSecundario()
            print("")
            option_consultar = input('Qué desea consultar?: ')
            number = 1
        # 1. Asociaciones
            if option_consultar == '1':
                os.system("cls")
                print("ASOCIACIONES: \n")
                for elem in self.asociaciones:
                    print(f'{number}. Declaración: {elem.get_declaracion().lower()}, CFI: {elem.get_cfi()}')
                    number += 1
                print("")
                consultar = input('¿Qué asociación desea consultar? (Seleccione un número o "s" para salir): ')
                os.system("cls")
                if consultar.isdigit():
                    if 1 <= int(consultar) <= len(self.asociaciones):
                        atributos = vars(self.asociaciones[int(consultar)-1])
                        for key,value in atributos.items():
                            print(f'{key}: {value}')
                        input('Oprima Enter o ingrese cualquier tecla para salir:  ')
                        os.system("cls")
                        continue
                elif consultar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
        # 2. Socios
            if option_consultar == '2':
                os.system("cls")
                print("SOCIOS: \n")
                for elem in self.socios:
                    print(f'{number}. Nombre:{elem.get_nombre()} INE:{elem.get_ine()}')
                    number += 1
                print("")
                consultar = input('¿Qué socio desea consultar? (Seleccione un número o "s" para salir): ')
                os.system("cls")
                if consultar.isdigit():
                    if 1 <= int(consultar) <= len(self.socios):
                        atributos = vars(self.socios[int(consultar)-1])
                        for key,value in atributos.items():
                            print(f'{key}: {value}')
                        input('Oprima Enter o ingrese cualquier tecla para salir:  ')
                        os.system("cls")
                        continue
                elif consultar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
        # 3. Asalariados
            if option_consultar == '3':
                os.system("cls")
                print("ASALARIADOS: \n")
                for elem in self.asalariados:
                    print(f'{number}. Nombre:{elem.get_nombre()} INE:{elem.get_ine()}')
                    number += 1
                print("")
                consultar = input('¿Qué asalariado desea consultar? (Seleccione un número o "s" para salir): ')
                os.system("cls")
                if consultar.isdigit():
                    if 1 <= int(consultar) <= len(self.asalariados):
                        atributos = vars(self.asalariados[int(consultar)-1])
                        for key,value in atributos.items():
                            print(f'{key}: {value}')
                        input('Oprima Enter o ingrese cualquier tecla para salir:  ')
                        os.system("cls")
                        continue
                elif consultar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
        # 4. Voluntarios
            if option_consultar == '4':
                os.system("cls")
                print("VOLUNTARIOS: \n")
                for elem in self.voluntarios:
                    print(f'{number}. Nombre:{elem.get_nombre()} INE:{elem.get_ine()}')
                    number += 1
                print("")
                consultar = input('¿Qué voluntario desea consultar? (Seleccione un número o "s" para salir): ')
                os.system("cls")
                if consultar.isdigit():
                    if 1 <= int(consultar) <= len(self.voluntarios):
                        atributos = vars(self.voluntarios[int(consultar)-1])
                        for key,value in atributos.items():
                            print(f'{key}: {value}')
                        input('Oprima Enter o ingrese cualquier tecla para salir:  ')
                        os.system("cls")
                        continue
                elif consultar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
        # 5. Proyectos
            if option_consultar == '5':
                os.system("cls")
                print("PROYECTOS: \n")
                for elem in self.proyectos:
                    print(f'{number}. Objetivo:{elem.get_objetivo().lower()} ID:{elem.get_ide()}')
                    number += 1
                print("")
                consultar = input('¿Qué proyecto desea consultar? (Seleccione un número o "s" para salir): ')
                os.system("cls")
                if consultar.isdigit():
                    if 1 <= int(consultar) <= len(self.proyectos):
                        atributos = vars(self.proyectos[int(consultar)-1])
                        for key,value in atributos.items():
                            print(f'{key}: {value}')
                        input('Oprima Enter o ingrese cualquier tecla para salir:  ')
                        os.system("cls")
                        continue
                elif consultar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
                    continue
            # Regresar
            if option_consultar == '6':
                break
            else:
                os.system("cls")
                print('ERROR!, seleccione una opción válida para continuar')

    def Actualizar(self):
        """
        Método que permite actualizar los valores de los atributos de cualquier objeto de cualquier clase.
        """
        while True:
            print('**********************')
            print('**    Actualizar    **')
            print('**********************')
            self.MenuSecundario()
            print("")
            option_actualizar = input('Qué desea actualizar?: ')
            number = 1
        # 1. Asociaciones
            if option_actualizar == '1':
                os.system("cls")
                print("ASOCIACIONES: \n")
                for elem in self.asociaciones:
                    print(f'{number}. Declaración: {elem.get_declaracion().lower()}, CFI: {elem.get_cfi()}')
                    number += 1
                print("")
                actualizar = input('¿Qué asociación desea actualizar? (Seleccione un número o "s" para salir): ')
                os.system("cls")
                if actualizar.isdigit():
                    if 1 <= int(actualizar) <= len(self.asociaciones):
                        objeto = self.asociaciones[int(actualizar)-1]
                        objeto.set_denominacion(input('Denominación: '))
                        objeto.set_direccion(input('Dirección: '))
                        objeto.set_provincia(input('Provincia: '))
                        objeto.set_tipo(input('Tipo: '))
                        objeto.set_declaracion(input('Declaración: '))
                elif actualizar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente') 
                os.system("cls")
                print('ÉXITO! asociación actualizada correctamente')
                continue
        # 2. Socios
            if option_actualizar == '2':
                os.system("cls")
                print("SOCIOS: \n")
                for elem in self.socios:
                    print(f'{number}. Nombre:{elem.get_nombre()} INE:{elem.get_ine()}')
                    number += 1
                print("")
                actualizar = input('¿Qué socio desea consultar? (Seleccione un número o "s" para salir): ')
                os.system("cls")
                if actualizar.isdigit():
                    if 1 <= int(actualizar) <= len(self.socios):
                        objeto = self.socios[int(actualizar)-1]
                        objeto.set_direccion(input('Dirección: '))
                        objeto.set_provincia(input('Provincia: '))
                        objeto.set_fecha_alta(input('Fecha de alta (dd/mm/aaaa): '))
                        objeto.set_cuota_mensual(input('Cuota mensual (valores enteros): '))
                        print('Ingrese el CFI de la asociación a la que pertenece el socio o "s" para salir')
                        while True:
                            cfi = input('CFI (una letra seguido de cuatro digitos): ')
                            cfi_exists = any(asoc.get_cfi() == cfi for asoc in self.asociaciones)
                            if cfi_exists:
                                objeto.set_asociacion(cfi)
                                for asoc in self.asociaciones:
                                    if asoc.get_cfi() == cfi:
                                        asoc.get_socios().append(objeto.get_ine())
                                break
                            elif cfi.lower() == 's':
                                break
                            else:
                                print('El CFI ingresado no se encuentra vinculado a alguno existente. Inténtelo nuevamente.')
                                continue
                elif actualizar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
                os.system("cls")
                print('ÉXITO! socio actualizado correctamente')
                continue
        # 3. Asalariado
            if option_actualizar == '3':
                os.system("cls")
                print("ASALARIADOS: \n")
                for elem in self.asalariados:
                    print(f'{number}. Nombre:{elem.get_nombre()} INE:{elem.get_ine()}')
                    number += 1
                print("")
                actualizar = input('¿Qué asalariado desea consultar? (Seleccione un número o "s" para salir): ')
                os.system("cls")
                if actualizar.isdigit():
                    if 1 <= int(actualizar) <= len(self.asalariados):
                        objeto = self.asalariados[int(actualizar)-1]
                        objeto.set_fecha_ingreso(input('Fecha de ingreso (dd/mm/aaaa): '))
                        objeto.set_sueldo_mensual(input('Sueldo mensual (valores enteros): '))
                        objeto.set_cargo(input('Cargo: '))
                        objeto.set_paso_seguro_social(input('Paso de seguro social (porcentaje entero): '))
                        objeto.set_isr(input('ISR (porcentaje entero): '))
                        print('Ingrese el CFI de la asociación a la que pertenece el trabajador  o "s" para salir')
                        while True:
                            cfi = input('CFI (una letra seguido de cuatro digitos): ')
                            cfi_exists = any(asoc.get_cfi() == cfi for asoc in self.asociaciones)
                            if cfi_exists:
                                objeto.set_asociacion(cfi)
                                for asoc in self.asociaciones:
                                    if asoc.get_cfi() == cfi:
                                        asoc.get_trabajadores().append(objeto.get_ine())
                                break
                            elif cfi.lower() == 's':
                                break
                            else:
                                print('El CFI ingresado no se encuentra vinculado a alguna asociación existente. Inténtelo nuevamente.')
                        print('Ingrese el ID del proyecto asignado al trabajador o "s" para salir')
                        while True:
                            ide = input('ID (13 digitos): ')
                            ide_exist = any(proj.get_ide()== ide and proj.get_asociacion() == objeto.get_asociacion() for proj in self.proyectos)
                            if ide_exist:
                                objeto.set_proyecto(ide)
                                for proj in self.proyectos:
                                    if proj.get_ide() == ide:
                                        proj.get_trabajadores().append(objeto.get_ine())
                                break
                            elif ide.lower() == 's':
                                break
                            else:
                                print('ERROR!, proyecto no existente o no pertenece a la misma asociación que el trabajador. Inténtelo nuevamente.')
                elif actualizar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
                os.system("cls")
                print('ÉXITO! asalariado actualizado correctamente')
                continue
        # 4. Voluntarios
            if option_actualizar == '4':
                os.system("cls")
                print("VOLUNTARIOS: \n")
                for elem in self.voluntarios:
                    print(f'{number}. Nombre:{elem.get_nombre()} INE:{elem.get_ine()}')
                    number += 1
                print("")
                actualizar = input('¿Qué voluntario desea consultar? (Seleccione un número o "s" para salir): ')
                os.system("cls")
                if actualizar.isdigit():
                    if 1 <= int(actualizar) <= len(self.voluntarios):
                        objeto = self.voluntarios[int(actualizar)-1]
                        objeto.set_fecha_ingreso(input('Fecha de ingreso (dd/mm/aaaa): '))
                        objeto.set_edad(input('Edad (sólo número): '))
                        objeto.set_profesion(input('Profesión: '))
                        objeto.set_horas(input('Horas por semana (horas enteras): '))
                        print('Ingrese el CFI de la asociación a la que pertenece el trabajador  o "s" para salir')
                        while True:
                            cfi = input('CFI (una letra seguido de cuatro digitos): ')
                            cfi_exists = any(asoc.get_cfi() == cfi for asoc in self.asociaciones)
                            if cfi_exists:
                                objeto.set_asociacion(cfi)
                                for asoc in self.asociaciones:
                                    if asoc.get_cfi() == cfi:
                                        asoc.get_trabajadores().append(objeto.get_ine())
                                break
                            elif cfi.lower() == 's':
                                break
                            else:
                                print('El CFI ingresado no se encuentra vinculado a alguna asociación existente. Inténtelo nuevamente.')
                        print('Ingrese el ID del proyecto asignado al trabajador o "s" para salir')
                        while True:
                            ide = input('ID (13 digitos): ')
                            ide_exist = any(proj.get_ide()== ide and proj.get_asociacion() == objeto.get_asociacion() for proj in self.proyectos)
                            if ide_exist:
                                objeto.set_proyecto(ide)
                                for proj in self.proyectos:
                                    if proj.get_ide() == ide:
                                        proj.get_trabajadores().append(objeto.get_ine())
                                break
                            elif ide.lower() == 's':
                                break
                            else:
                                print('ERROR!, proyecto no existente o no pertenece a la misma asociación que el trabajador. Inténtelo nuevamente.')
                elif actualizar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
                os.system("cls")
                print('ÉXITO! voluntario actualizado correctamente')
                continue
        # 5. Proyectos
            if option_actualizar == '5':
                os.system("cls")
                print("PROYECTOS: \n")
                for elem in self.proyectos:
                    print(f'{number}. Objetivo:{elem.get_objetivo().lower()} ID:{elem.get_ide()}')
                    number += 1
                print("")
                actualizar = input('¿Qué proyecto desea consultar? (Seleccione un número o "s" para salir): ')
                os.system("cls")
                if actualizar.isdigit():
                    if 1 <= int(actualizar) <= len(self.proyectos):
                        objeto = self.proyectos[int(actualizar)-1]
                        objeto.set_pais(input('País: '))
                        objeto.set_zona(input('Zona: '))
                        objeto.set_objetivo(input('Objetivo: '))
                        objeto.set_num_benef(input('Número de beneficiarios del proyecto (sólo números enteros): '))
                        print('Ingrese el CFI de la asociación a la que pertenece el proyecto o "s" para salir')
                        while True:
                            cfi = input('CFI (una letra seguido de cuatro digitos): ')
                            cfi_exists = any(asoc.get_cfi() == cfi for asoc in self.asociaciones)
                            if cfi_exists:
                                objeto.set_asociacion(cfi)
                                for asoc in self.asociaciones:
                                    if asoc.get_cfi() == cfi:
                                        asoc.get_proyectos().append(objeto.get_ide())
                                break
                            elif cfi.lower() == 's':
                                break
                            else:
                                print('El CFI ingresado no se encuentra vinculado a algún proyecto existente. Inténtelo nuevamente.')
                                continue                
                    print('Ingrese el ID del proyecto padre o "s" para salir')
                    ide_exist = None
                    ide = ""
                    while True:
                        ide = input('ID (13 digitos): ')
                        ide_exist = any(proj.get_ide() == ide for proj in self.proyectos)
                        if ide_exist:
                            for proj in self.proyectos:
                                if proj.get_ide() == ide:
                                    objeto.set_proyecto_padre(ide)
                                    proj.set_sub_proyectos([objeto.get_ide()])
                                    break
                            break
                        if ide.lower() == 's':
                            break
                        else:
                            print('El ID ingresado no se encuentra vinculado a algún proyecto  existente. Inténtelo nuevamente.')
                    objeto.set_proyecto_padre(ide)
                elif actualizar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
                os.system("cls")
                print('ÉXITO! proyecto actualizado correctamente')
                continue
        # 6. Regresar
            if option_actualizar == '6':
                break
            else:
                os.system("cls")
                print('ERROR!, seleccione una opción válida para continuar')
                continue

    def Borrar(self):
        """
        Método que permite borrar cualquier objeto creado.
        """
        while True:
            print('**********************')
            print('**      Borrar      **')
            print('**********************')
            self.MenuSecundario()
            print("")
            option_borrar = input('Qué desea borrar?: ')
            number = 1
        # 1. Asociaciones
            if option_borrar == '1':
                os.system("cls")
                print("Asociaciones: \n")
                for elem in self.asociaciones:
                    print(f'{number}. Declaración: {elem.get_declaracion().lower()}, CFI: {elem.get_cfi()}')
                    number += 1
                print("")
                borrar = input('¿Qué asociación deseas borrar? (Seleccione un número o "s" para salir): ')
                if borrar.isdigit():
                    if 1 <= int(borrar) <= len(self.asociaciones):
                        del self.asociaciones[int(borrar)-1]
                        os.system("cls")
                        print('ÉXITO!, se ha borrado la asociación correctamente')
                        continue
                    else:
                        os.system("cls")
                        print('El número de asociación no es válido!')
                        continue
                elif borrar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
        # 2. Socios
            if option_borrar == '2':
                os.system("cls")
                print("Socios: \n")
                for elem in self.socios:
                    print(f'{number}. Nombre:{elem.get_nombre()} INE:{elem.get_ine()}')
                    number += 1
                print("")
                borrar = input('¿Qué socio deseas borrar? (Seleccione un número o "s" para salir): ')
                if borrar.isdigit():
                    if 1 <= int(borrar) <= len(self.socios):
                        del self.socios[int(borrar)-1]
                        os.system("cls")
                        print('ÉXITO!, se ha borrado el socio correctamente')
                        continue
                    else:
                        os.system("cls")
                        print('El número de socio no es válido!')
                        continue
                elif borrar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
        # 3. Asalariados
            if option_borrar == '3':
                os.system("cls")
                print("Asalariados: \n")
                for elem in self.asalariados:
                    print(f'{number}. Nombre:{elem.get_nombre()} INE:{elem.get_ine()}')
                    number += 1
                print("")
                borrar = input('¿Qué asalariado deseas borrar? (Seleccione un número o "s" para salir): ')
                if borrar.isdigit():
                    if 1 <= int(borrar) <= len(self.asalariados):
                        del self.asalariados[int(borrar)-1]
                        os.system("cls")
                        print('ÉXITO!, se ha borrado el asalariado correctamente')
                        continue
                    else:
                        os.system("cls")
                        print('El número de asalariado no es válido!')
                        continue
                elif borrar.lower() =='s':
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
        # 4. Voluntarios
            if option_borrar == '4':
                os.system("cls")
                print("Voluntarios: \n")
                for elem in self.voluntarios:
                    print(f'{number}. Nombre:{elem.get_nombre()} INE:{elem.get_ine()}')
                    number += 1
                print("")
                borrar = input('¿Qué voluntario deseas borrar? (Seleccione un número o "s" para salir): ')
                if borrar.isdigit():
                    if 1 <= int(borrar) <= len(self.voluntarios):
                        del self.voluntarios[int(borrar)-1]
                        os.system("cls")
                        print('ÉXITO!, se ha borrado el voluntario correctamente')
                        continue
                    else:
                        os.system("cls")
                        print('El número de voluntario no es válido!\n')
                        continue
                elif borrar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente')
        # 5. Proyectos
            if option_borrar == '5':
                os.system("cls")
                print("Proyectos: \n")
                for elem in self.proyectos:
                    print(f'{number}. Objetivo:{elem.get_objetivo().lower()} ID:{elem.get_ide()}')
                    number += 1
                print("")
                borrar = input('¿Qué proyecto deseas borrar? (Seleccione un número o "s" para salir): ')
                if borrar.isdigit():
                    if 1 <= int(borrar) <= len(self.proyectos):
                        del self.proyectos[int(borrar)-1]
                        os.system("cls")
                        print('ÉXITO!, se ha borrado el proyecto correctamente')
                        continue
                    else:
                        os.system("cls")
                        print('El número de proyecto no es válido!')
                        continue
                elif borrar.lower() == 's':
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print('ERROR!, caracteres no válidos, intente nuevamente') 
        # 6. Regresar
            if option_borrar == '6':
                break
            else:
                print('ERROR!, seleccione una opción válida para continuar')
                  
    def Guardar(self):
        """
        Método que permite guardar las listas que contienen los objetos de cada clase en los archivos, de manera que estos se mantengan al ejecutar nuevamente el programa.
        """
        for archivo, lista in self.archivos.items():
            with open(archivo, "wb") as f:
                pickle.dump(lista, f)
                f.close()

    def Ejecutar(self):
        """
        Método Ejecutar que contiene la lógica principal del programa, basado el uso de todos los métodos creados en la clase Gestor.
        """
        self.Cargar()
        self.Bienvenida()
        os.system("cls")
        while True:
            self.MenuPrimario()
            print('')
            option_user = input('Seleccione una opción para continuar (número): ')
            if option_user == '1':
                os.system("cls")
                self.Crear()
                os.system("cls")
                continue
            elif option_user == '2':
                os.system("cls")
                self.Consultar()
                os.system("cls")
                continue
            elif option_user == '3':
                os.system("cls")
                self.Actualizar()
                os.system("cls")
                continue
            elif option_user == '4':
                os.system("cls")
                self.Borrar()
                os.system("cls")
                continue
            elif option_user == '5':
                self.Guardar()
                os.system("cls")
                print('SE HAN GUARDADO TODOS LOS DATOS CON ÉXITO!')
                continue
            elif option_user == '6':
                os.system("cls")
                break
            else:
                os.system("cls")
                print('ERROR!, seleccione una opción válida para continuar')



































