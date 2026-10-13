import os
import random
import sys

CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%&-_+="
LONGITUD = 8


def generar_nombre():
    nombre = ""
    for i in range(LONGITUD):
        nombre += random.choice(CARACTERES)
    return nombre + ".txt"


def crear_archivo(carpeta):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    creado = False
    while not creado:
        ruta = os.path.join(carpeta, generar_nombre())
        if not os.path.exists(ruta):
            with open(ruta, "w"):
                pass
            creado = True
    return ruta


def crear_archivos(carpeta, cantidad):
    for i in range(cantidad):
        ruta = crear_archivo(carpeta)
        print(f"Archivo creado: {ruta}")


if __name__ == '__main__':
    crear_archivos(sys.argv[1], int(sys.argv[2]))
