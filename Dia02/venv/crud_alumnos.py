import os
import tabulate
import time

lista_alumnos = [
    {
        'nombre':'Diego del Castillo',
        'email':'delcastillodsd@gmail.com',
        'celular':'993694448'
    }
]
ANCHO = 50
opcion = 0
while(opcion < 5):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "Crud de Alumnos")
    print("="*ANCHO)
    print("""
            [1] REGISTRAR ALUMNO
            [2] MOSTRAR ALUMNOS
            [3] ACTUALIZAR ALUMNO
            [4] ELIMINAR ALUMNO
            [5] SALIR
            """)
    print("="*ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    print(f"selecciono opcion {opcion}")
    time.sleep(1)
