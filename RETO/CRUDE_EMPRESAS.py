import os
import tabulate
import time
from librerias.lib_empresas import *

f = open('empresas.txt','r')
str_empresas = f.read()
f.close()

lista_empresas = cargar_datos(str_empresas)
ANCHO = 50
opcion = 0

while(opcion < 5):
    os.system("clear")
    mostrar_menu(ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if(opcion == 1):
        print("="*ANCHO)
        print(" " * 10 + "[1] REGISTRAR EMPRESA")
        print("="*ANCHO)
        ruc = input("RUC : ")
        razonsocial = input("Razon Social: ")
        direccion = input("Domicilio Fiscal: ")
        fechainicio = input("Fecha de Inicio (DD/MM/AAAA): ")
        dic_nueva_empresa = {
            'ruc':ruc,
            'razonsocial':razonsocial,
            'direccion':direccion,
            'fechainicio':fechainicio
        }
        lista_empresas.append(dic_nueva_empresa)
        print(" EMPRESA REGISTRADO CON EXITO")
    elif(opcion == 2):
        print("="*ANCHO)
        print(" " * 10 + "[2] MOSTRAR EMPRESAS")
        print("="*ANCHO)
        cabeceras = ["RUC","RAZON SOCIAL","DIRECCION","FECHA DE INICIO DE ACTIVIDADES"]
        tabla = [empresa.values() for empresa in lista_empresas]
        print(tabulate.tabulate(tabla,headers=cabeceras,tablefmt="grid"))
        input("Press ENTER to continue...")
    elif(opcion == 3):
        print("="*ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE RAZON SOCIAL DEL EMPRESA A ACTUALIZAR :')
        posicion_busqueda = buscar_empresa(valor_busqueda,lista_empresas)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO LA EMPRESA SOLICITADA")
        else:
            print(f' EMPRESA A ACTUALIZAR : {lista_empresas[posicion_busqueda].get("razonsocial")}')
            nuevo_ruc = input("RUC : ")
            nueva_rs = input("Razon Social : ")
            nueva_direccion = input("Direccion : ")
            nueva_fechainicio = input("Fecha de Inicio de Actividades (DD/MM/AAAA): ")
            dic_actualizar_empresa = {
                'ruc': nuevo_ruc,
                'razonSocial': nueva_rs,
                'direccion': nueva_direccion,
                'fechainicio': nueva_fechainicio
            }
            lista_empresas[posicion_busqueda] = dic_actualizar_empresa
        print("EMPRESA ACTUALIZADA CON EXITO")
    elif(opcion == 4):
        print("="*ANCHO)
        print(" " * 10 + "[4] ELIMINAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE RAZON SOCIAL DE LA EMPRESA A ELIMINAR :')
        posicion_busqueda = buscar_empresa(valor_busqueda,lista_empresas)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO LA EMPRESA SOLICITADA")
        else:
            lista_empresas.pop(posicion_busqueda)
            print('EMPRESA ELIMINADA')
    elif(opcion == 5):
        print("="*ANCHO)
        print(" " * 10 + "[5] SALIR")
        str_empresas = grabar_datos(lista_empresas)
        fsalida = open('empresas.txt','w')
        fsalida.write(str_empresas)
        fsalida.close()
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" " * 10 + "OPCIÓN NO VALIDA")
        print("="*ANCHO)
        
    time.sleep(1)