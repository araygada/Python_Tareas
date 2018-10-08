# Ejercicio 1.4 - Alberto Raygada
# Escriba un programa que solicite dos números, verifique que el primero es estrictamente
# menor que el segundo y calcula la suma de todos los números impares que se encuentran
# entre el primero número y el segundo número.
# -------------------------------------------------------------------------------------------------------------------------

message = "Se le va a solictar que ingrese dos números para conformar un rango y "
message = message + "listar los números impares dentro del mismo."
print(message)

def suma(lista):
    total = 0
    for i in lista:
        total += i
    return total

while True:
    num1 = 0
    num2 = 0
    num1 = int(input("Incluya el primer numero del rango: "))
    num2 = int(input("Incluya el segundo numero del rango: "))
    if num1 < num2:
        lista = [i for i in range(num1, num2) if (i%2!=0)]
        message = "La lista de números impares en el rango de " + str(num1) + " a " + str(num2) + " es: " +  str(lista)
        message += "\ny la suma de esos números impares es: " + str(suma(lista))
        print(message)
        break
    elif num2 < num1:
        message = "El primer número incluido debe ser menor al segundo. Intente de nuevo."
        print(message)
