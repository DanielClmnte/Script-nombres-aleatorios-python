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
    if len(sys.argv) != 3:
        print("Uso: python3 nombre_aleatorio.py <ruta> <cantidad>")
        sys.exit(1)

    ruta = sys.argv[1]
    cantidad = sys.argv[2]

    if ruta == "":
        print("Tienes que introducir una ruta")
        sys.exit(1)

    if not cantidad.isdigit():
        print("La cantidad tiene que ser un número")
        sys.exit(1)

    crear_archivos(ruta, int(cantidad))
