# Ejercicio 1.1 - Alberto Raygada
# Crear un programa que tome dos numeros y devuelva el mayor de ellos
# -------------------------------------------------------------------------------------------------

num1 = int(input("Incluya el primer numero: "))
num2 = int(input("Incluya el segundo numero: "))

if num1 > num2:
    mensaje = "El primer numero incluido (" + str(num1) + ") es el mayor."
    print(mensaje)
else:
    mensaje = "El segundo numero incluido (" + str(num2) + ") es el mayor."
    print(mensaje)


