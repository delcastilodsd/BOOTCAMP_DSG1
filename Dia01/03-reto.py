# ENTRADA
print("Calculadora de Tipo de Cambio")
operacion = input("Ingrese el tipo de moneda que quiere cambiar (soles|dolares): ")
#PROCESO
if(operacion == "soles"):
    soles = input("Ingrese la cantidad de soles:")
    resultado = float(soles)/3.65
    print("El cambio a dolares resulto en ",resultado, "dolares")
elif(operacion == "dolares"):
    dolares = input("Ingrese la cantidad de dolares:")
    resultado = float(dolares)*3.65
    print("El cambio a soles resulto en ",resultado, " soles")
else:
    print("La operación no existe...")
    exit()
#SALIDA
