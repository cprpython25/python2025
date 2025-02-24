print ("Ejemplo mayor de 3 numeros")
print ("introduzca el numero 1")
numero1 = int(input())
print ("introduzca el numero 2")
numero2 = int(input())
print ("introduzca el numero 3")
numero3 = int(input())
mayor = 0
menor = 0
intermedio = 0
#comparamos cada numero con los otros dos
if (numero1 >= numero2 and numero1 >= numero3):
    mayor = numero1
elif (numero2 >= numero1 and numero2 >= numero3):
    mayor = numero2
else:
    mayor = numero3
#MISMA PREGUNTA PERO CAMBIANDO A SIMBOLO MENOR
if (numero1 ≤= numero2 and numero1 ≤= numero3):
    menor = numero1
elif (numero2 ≤= numero1 and numero2 ≤ numero3):
    menor