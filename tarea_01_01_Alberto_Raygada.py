# Tarea 1.1 - Alberto Raygada
# Solicitar dos números que sean positivos, que el primero sea menor en 50
# con respecto al segundo, que calcule la suma de todos los números entre el rango
# que sean múltiplos de 5 y múltiplos de 3.
# -------------------------------------------------------------------------------------------------

message = "A continuación incluya dos números positivos, que el primero sea menor al segundo "
message += "por al menos una diferencia de 50"
print(message)

while True:
    num1 = 0
    num2 = 0
    num1 = int(input("Incluya el primer número: "))
    num2 = int(input("Incluya el segundo número: "))
    if (num1 < 0) or (num2 < 0):
        message = "Alguno de los números incluidos no es positivo."
        message += "Por favor intente de nuevo."
        print(message)
    elif (num2 - num1) < 50:
        message = "El primer número no es menor que el segundo por al menos 50. "
        message += "Por favor intente de nuevo."
        print(message)
    else:
        break

lista = [i for i in range(num1, num2) if (i%3 == 0) and (i%5 == 0)]
print("La lista de números múltiplos de 5 y múltiplos de 3 es:")
print(lista)
suma = 0
for i in lista:
    suma += i
print("La suma total de los números múltiplos de 5 y múltiplos de 3 es:")
print(suma)





