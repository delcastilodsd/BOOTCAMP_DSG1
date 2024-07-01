# ENTRADA
print("Mi calculadora")
numero1 = input("Número 1: ")
numero2 = input("Número 2: ")
operacion = input("Ingrese el tipo de operación(suma|resta): ")
#PROCESO
if(operacion == "suma"):
    resultado = int(numero1) + int(numero2)
elif(operacion == "resta"):
    resultado = int(numero1) - int(numero2)
else:
    print("La operación no existe")
    exit()
#SALIDA
print(f"El resultado es {resultado}")
