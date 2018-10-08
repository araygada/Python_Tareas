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

