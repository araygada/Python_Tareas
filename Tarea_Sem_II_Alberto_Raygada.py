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


# Ejercicio 1.2 - Alberto Raygada
# Program que encuentre todos los numero primos entre 10 y 90
# ---------------------------------------------------------------------------------------

primos = [i for i in range(10,90) if (i%2!=0 or i ==2) and (i%3!=0 or i==3) and (i%5!=0 or i==5) and (i%7!=0 or i==7)]
print(primos)

# Ejercicio 1.3 - Alberto Raygada
# Programa que solicite su nombre, salude, pregunte si desea trabajar o ir de vacaciones, lista de
# destinos, elegir, mostrar precio. Si es trabajar, tipos de cafe y precios, elegir y precio
# --------------------------------------------------------------------------------------------------------------------------------

nombre = input("Cual es tu nombre: ")
nombre = nombre
print("Hola " + nombre)
deseo = int(input("Deseas vacacionar (1) o trabajar (2): (digita el número que corresponda): "))
if deseo == 1:
    destinos = ["Cancún", "Aruba", "Cartagena"]
    precios = ["$1.5 mil", "$1 mil", "$2 mil"]
    mensaje = "Ya que quieres vacacionar, tenemos los siguientes destinos y precios:"
    print(mensaje)
    n = 0
    for i in destinos:
        n = n + 1
        print(str(n) + " " + i + " " + precios[n -1])
    seleccion = int(input("¿A cuál destino te gustaría ir? (seleccione según el número que corresponda): "))
    mensaje="Feliz viaje a " + destinos[seleccion -1] + " " + nombre + ". Debes cancelar " + precios[seleccion-1] + "."
    print(mensaje)
elif deseo == 2:
    opciones = ["Café negro", "Café con leche", "Té"]
    precios = ["$1.50", "$2.00", "$1.00"]
    mensaje = "Ya que quieres trabajar, te ofrecemos las siguientes bebidas y precios a elegir:"
    print(mensaje)
    n = 0
    for i in opciones:
        n = n + 1
        print(str(n) + " " + i + " " + precios[n-1])
    seleccion = int(input("¿Cuál es la bebida que deseas? (seleccione según el número que corresponda): "))
    mensaje="Buen provecho con tu " + opciones[seleccion -1] + " " + nombre + ". Debes cancelar " + precios[seleccion-1] + "."
    print(mensaje)

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

# Tarea 1.2 - Alberto Raygada
# Cree un programa que imprima la tabla de multiplicación desde el 0 hasta el 20 mostrando el
# siguiente formato:  0 X 0 = 0
# -------------------------------------------------------------------------------------------------

rango = range(0,21)
for i in rango:
    for j in rango:
        resultado = i * j
        print(i, "x" ,j, "=", resultado)

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

# Tarea 1.4 - Alberto Raygada
# Cree un programa que solicite al usuario tres nombres y para cada uno de estos nombres,
# el programa indica la cantidad de vocales que hay en cada uno de ellos.
# -------------------------------------------------------------------------------------------------

message = "Por favor incluya tres nombres para indicarle cuántas vocales tiene cada palabra"
print(message)
name1 = input("Ingrese el primer nombre: ")
name2 = input("Ingrese el segundo nombre: ")
name3 = input("Ingrese el tercer nombre: ")

voc1 = 0; voc2 = 0; voc3 = 0

def contar(name):
    voc = 0
    name = name.lower()
    for i in name:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            voc = voc + 1
    return voc

voc1 = contar(name1); voc2 = contar(name2); voc3 = contar(name3)

message = "El primer nombre " + name1 + " tiene " + str(voc1) +" vocales. "
message += "El segundo nombre " + name2 + " tiene " + str(voc2) +" vocales. "
message += "El tercer nombre " + name3 + " tiene " + str(voc3) +" vocales."

print(message)


