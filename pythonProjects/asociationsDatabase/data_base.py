# Base de dato para inicializar archivos
from Asociación import Asociacion
from Asalariado import Asalariado
from Voluntario import Voluntario
from Proyecto import Proyecto
from Socio import Socio
import pickle

asoc_1 = Asociacion(cfi= 'A1010', denominacion='Asociación protectora de animales',  direccion='Calle Madrid 123', provincia='Ciudad Autónoma de buenos Aires', tipo='Organización sin fines de lucro', declaracion='Asociación para defender el derecho de los animales', socios=['91234'], trabajadores=['1684531622322', '1684531623321','1684531627098'], proyectos=['1684531625678'])
asoc_2 = Asociacion(cfi= 'B1011', denominacion='Asociación de emprendedores', direccion='Avenida Washington 456', provincia='Provincia de Buenos Aires', tipo='Asociación Civil', declaracion='Asociación para fomentar el espirítu emprendedor',socios=['34565'], trabajadores=['1684531616660'], proyectos=['1684531688793'])
asoc_3 = Asociacion(cfi='C1012', denominacion='Asociación de bienestar comunitario', direccion='calle del progreso 789', provincia='Provincia de Córdoba', tipo='sin fines de lucro', declaracion='Asociación para mejorar la calidad de vida', socios=['27896'], trabajadores=['1684531625941','1684531621985'], proyectos=['1684531666471'])
asociaciones_db = [asoc_1,asoc_2,asoc_3]
# socios
soc_1 = Socio(ine='91234', nombre='Jorge Pérez',direccion='calle de los olivos 123', provincia='Provincia de Valencia', fecha_alta='07/03/2019', cuota_mensual='25', aportacion_anual= 300, asociacion="A1010")
soc_2 = Socio(ine='34565', nombre='Pedro Gómez', direccion='Calle del Poeta 456', provincia='Provincia de Barcelona', fecha_alta='11/01/2018', cuota_mensual='50', aportacion_anual=600,asociacion="B1011")
soc_3 = Socio(ine='27896', nombre='María Rodríguez', direccion='Av. de la Tecnología 789', provincia='Provincia de Madrid', fecha_alta='28/06/2020', cuota_mensual='75', aportacion_anual=900,asociacion="C1012")
socios_db = [soc_1,soc_2,soc_3]
# asalariados
asal_1 = Asalariado(ine='68223', nombre='Ana María Acevedo', fecha_ingreso='01/01/2020', asociacion='C1012', sueldo_mensual='15000', cargo='Auxiliar administrativo', paso_seguro_social='3', isr='10')
asal_2 = Asalariado(ine='18755', nombre='Luis García', fecha_ingreso='15/02/2021', asociacion='A1010', sueldo_mensual='20000', cargo='Ingeniero de Sistemas', paso_seguro_social='4', isr='12')
asal_3 = Asalariado(ine='34890', nombre='Alberto Castro', fecha_ingreso='10/07/2019', asociacion='B1011', sueldo_mensual='10000', cargo='recepccionista', paso_seguro_social='2', isr='8')
asalariados_db = [asal_1,asal_2,asal_3]
# voluntarios
vol_1 = Voluntario(ine='00293',nombre='Ana González', fecha_ingreso='12/05/2020', edad='28', profesion='Abogada', horas='20', asociacion='C1012')
vol_2 = Voluntario(ine='50987', nombre='Carlos Rincón', fecha_ingreso='03/01/2022', edad='32', profesion='Ingeniero en sistemas', horas='15', asociacion='A1010')
vol_3 = Voluntario(ine='83745', nombre='Manuel Pineda', fecha_ingreso='22/11/2019', edad='45', profesion='Enfermero', horas='10', asociacion='A1010')
voluntarios_db = [vol_1,vol_2,vol_3]
# proyectos
proj_1 = Proyecto(pais='España', zona='Andalucía', objetivo='Construcción de un centro comunitario', num_benef='100', asociacion='A1010', ide='1684531625678', trabajadores=['18755', '83745','50987'])
proj_2 = Proyecto(pais='Argentina', zona='La plata', objetivo='Capacitación y emprendimiento para mujeres rurales', num_benef='50', asociacion='B1011', ide='1684531688793', trabajadores=['34890', ])
proj_3 = Proyecto(pais='Estados Unidos', zona='Costa este', objetivo='Construcción de reserva natural para la fauna silvestre', num_benef='75', asociacion='C1012', ide='1684531666471',trabajadores=['68223','00293'])
proyectos_db = [proj_1,proj_2,proj_3]

def DataBase():
    # crear archivos.dat con las listas
    asociaciones =asociaciones_db
    socios = socios_db
    asalariados = asalariados_db
    voluntarios = voluntarios_db
    proyectos = proyectos_db
    
    # asociaciones
    archivo_asoc = "ASOCIACIONES.dat"
    with open(archivo_asoc, "wb") as f:
        pickle.dump(asociaciones,f)
    # socios
    archivo_soc = "SOCIOS.dat"
    with open(archivo_soc,"wb") as f:
        pickle.dump(socios,f)
        f.close()
    # asalariados
    archivo_asal = "ASALARIADOS.dat"
    with open(archivo_asal, "wb") as f:
        pickle.dump(asalariados,f)
        f.close()
    # voluntarios
    archivo_vol = "VOLUNTARIOS.dat"
    with open(archivo_vol, "wb") as f:
        pickle.dump(voluntarios,f)
        f.close()
    # proyectos
    archivo_proj = "PROYECTOS.dat"
    with open(archivo_proj, "wb") as f:
        pickle.dump(proyectos, f)
        f.close()






























