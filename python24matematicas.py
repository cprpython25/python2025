#los import se realizan lo primero de nuestro codigo
#from libreria24matematicas import sumaNumeros, restarNumeros, mostrarMenu
import libreria24matematicas

#codigo logico
print("Calculadora métodos")
numero1 = 9
numero2 = 19
libreria24matematicas.mostrarMenu()
opcion = int(input())
resultado = 0
if (opcion == 1):
    resultado = libreria24matematicas.sumarNumeros(numero1 , numero2)
elif (opcion == 2):
    resultado = libreria24matematicas.restarNumeros(numero1 , numero2)
elif (opcion == 3):
    resultado = libreria24matematicas.multiplicarNumeros(numero1 , numero2)
else
    print("No ha seleccionado una opcion correcta")
print("Resultado", resultado)
print("fin de programa")