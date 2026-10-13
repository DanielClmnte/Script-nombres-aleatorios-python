import os
import random

# Caracteres con los que se forma el nombre
CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%&-_+="

# Carpeta "nombres aleatorios" dentro del propio proyecto
CARPETA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nombres aleatorios")


def generar_nombre():
    nombre = ""
    for i in range(8):
        nombre += random.choice(CARACTERES)
    return nombre + ".txt"


def crear_archivo():
    if not os.path.exists(CARPETA):
        os.mkdir(CARPETA)

    # Se repite hasta encontrar un nombre que no exista
    creado = False
    while not creado:
        ruta = os.path.join(CARPETA, generar_nombre())
        if not os.path.exists(ruta):
            with open(ruta, "w"):
                pass
            creado = True
    return ruta


if __name__ == '__main__':
    ruta = crear_archivo()
    print(f"Archivo creado: {ruta}")
