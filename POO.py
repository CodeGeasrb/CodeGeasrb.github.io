from Asociación import Asociacion
import pickle

def main():
    num = 1234
    asociacion = Asociacion(num, "Asociacion num 1", "direc 1", "prov 1", "comercial", True, ["socio 1", "socio 2", "socio 3"])
    print(asociacion.cfi)


# para llamar a varios modulos, y las funciones que vienen en ellas.

"""if "__name__" == "___main__":
    main()"""
main()


# Guarduar un objeto completo (con muchos atributos) en un archivo (hacemos persistentes los datos)
# 1 Crear un archivo con objetos
# 2 Leer el archivo

archivo_asoc = "asoc.dat"
with open(archivo_asoc, "wb") as f:
    pickle.dump()












