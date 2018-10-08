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
