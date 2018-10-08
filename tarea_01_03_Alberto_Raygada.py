# Tarea 1.3 - Alberto Raygada
# Cree un programa que solicite al usuario un número entre 0 y 30. El programa debe calcular el
# factorial (N!) del número ingresado por el usuario.
# -------------------------------------------------------------------------------------------------

while True:
    numero = int(input("Ingrese un número entre 1 y 30: "))
    if numero > 30 or numero < 0:
        message = "El número incluido debe ser mayor a 0 y menor a 30."
        message += "\nPor favor intente de nuevo."
        print(message)
    else:
         break

factorial = 1

for i in range(1, numero + 1):
            factorial = factorial * i

message = "El factorial de " + str(numero) + " es " + str(factorial)
print(message)

